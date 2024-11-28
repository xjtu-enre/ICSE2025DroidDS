import csv
import json
import os
from typing import List

import pandas as pd


def write_dict_to_csv(out_path: str, name: str, data: List[dict], mode: str, write_header=True):
    print(f'start write {name}')
    os.makedirs(out_path, exist_ok=True)
    file_path = os.path.join(out_path, name + '.csv')
    headers = []
    if data:
        headers = [item for item in data[0].keys()]
    if not write_header and not os.path.exists(file_path):
        write_header = True
    with open(file_path, mode, newline='') as f:
        f_writer = csv.DictWriter(f, headers)
        if write_header:
            f_writer.writeheader()
        f_writer.writerows(data)
    print(f'write {name} success')


def read_base_json(file_path: str):
    print('reading json file')
    try:
        with open(file_path, encoding='utf-8') as f:
            res = json.load(f, strict=False)
            return res
    except Exception as e:
        print(e)


class MitigableFilter:
    file_path: str
    out_path: str

    def __init__(self, file_path: str, out_path: str):
        self.file_path = file_path
        self.out_path = out_path

    def load_total_anti_patterns(self):
        res: dict = read_base_json(self.file_path)['res']['values']
        return res

    def load_metric_anti_patterns(self):
        dict_res = {}
        res = read_base_json(self.file_path)['res']
        for item in res:
            dict_res.update(item)
        return dict_res

    def handle_count(self, patterns: List[str], proj: str):
        res = self.load_metric_anti_patterns()
        count_res = {"project": proj}
        data = []
        for pattern in patterns:
            method = getattr(self, f'handle_count_{pattern}', None)
            count_res.update(method(res[pattern]))

        count_res_df = pd.DataFrame(count_res, index=[0])
        for _, row in count_res_df.iterrows():
            ID2_mitigable = row['native_method_add_parameter_up'] + row['native_method_add_parameter_no']
            ID2_notMitigable = row['native_method_add_parameter_down']
            CD1_mitigable = row['native_class_inherit_extensive_class_no_inherit']
            CD1_notMitigable = row['native_class_inherit_extensive_class_is_inherit']
            UD1_mitigable = row['call_native_hidden_method_no_acceptable'] + row[
                'use_native_hidden_variable_no_acceptable']
            UD1_notMitigable = row['call_native_hidden_method_all_acceptable'] + \
                                row['call_native_hidden_method_mix_acceptable'] + \
                                row['use_native_hidden_variable_all_acceptable'] + \
                                row['use_native_hidden_variable_mix_acceptable']
            UD3_mitigable = row['native_class_access_modify_useless'] + row['native_method_access_modify_useless']
            UD3_notMitigable = row['native_class_access_modify_useful'] + row['native_method_access_modify_useful']
            UD4_mitigable = row['del_native_class_final_is_inherit'] + row['del_native_method_final_no_override']
            UD4_notMitigable = row['del_native_class_final_no_inherit'] + row['del_native_method_final_is_override']
            UD5_mitigable = row['extensive_method_reflect_native_class_mix_in_sdk'] + \
                            row['extensive_method_reflect_native_class_all_in_sdk'] + \
                            row['extensive_method_reflect_native_method_mix_in_sdk'] + \
                            row['extensive_method_reflect_native_method_all_in_sdk']
            UD5_notMitigable = row['extensive_method_reflect_native_class_all_not_in_sdk'] + \
                            row['extensive_method_reflect_native_method_all_not_in_sdk']
            data.append([proj,ID2_mitigable, ID2_notMitigable, CD1_mitigable, CD1_notMitigable,
                         UD1_mitigable, UD1_notMitigable, UD3_mitigable, UD3_notMitigable,
                         UD4_mitigable, UD4_notMitigable, UD5_mitigable, UD5_notMitigable])

        output_df = pd.DataFrame(data,
                                 columns=["project","ID2_mitigable", "ID2_notMitigable", "CD1_mitigable", "CD1_notMitigable",
                                          "UD1_mitigable", "UD1_notMitigable", "UD3_mitigable", "UD3_notMitigable",
                                          "UD4_mitigable", "UD4_notMitigable", "UD5_mitigable", "UD5_notMitigable"])
        output_file = "mitigable_count.csv"
        output_df.to_csv(output_file, index=False)


    def handle_count_FinalDel(self, pattern_info: dict):
        res = {}
        for key, val in pattern_info.items():
            if "res" in val.keys():
                if "is_inherit" in val['res'].keys():
                    metric = val['res']["is_inherit"]
                    try:
                        res.update({
                            f"{key}_is_inherit": metric['is_inherit'],
                            f"{key}_no_inherit": metric['no_inherit']
                        })
                    except Exception:
                        res.update({
                            f"{key}_is_inherit": 0,
                            f"{key}_no_inherit": 0
                        })
                elif "is_override" in val['res'].keys():
                    metric = val['res']["is_override"]
                    try:
                        res.update({
                            f"{key}_is_override": metric['is_override'],
                            f"{key}_no_override": metric['no_override']
                        })
                    except Exception:
                        res.update({
                            f"{key}_is_override": 0,
                            f"{key}_no_override": 0
                        })

                else:
                    res.update({})

        return res

    def handle_count_mc_FinalDel(self, pattern_info: dict, styles):
        res = {}
        for key, val in pattern_info["res"].items():
            if key not in styles:
                continue
            res[f"{key}_major"] = set()
            res[f"{key}_minor"] = set()
            for exa in val["res"]:
                mc = exa["metrics"]
                if "is_inherit" in mc.keys():
                    m = {True: "major", False: "minor"}
                    try:
                        res[f'{key}_{m[len(mc["is_inherit"]) <= 0]}'].add(
                            mc["stability"]["maintenance_cost"]["extensive"]["filename"])
                    except Exception:
                        pass
                elif "is_override" in mc.keys():
                    m = {True: "major", False: "minor"}
                    try:
                        res[f'{key}_{m[len(mc["is_override"]) <= 0]}'].add(
                            mc["stability"]["maintenance_cost"]["extensive"]["filename"])
                    except Exception:
                        pass
        return res

    def handle_count_AccessibilityModify(self, pattern_info: dict):
        res = {}
        for key, val in pattern_info.items():
            try:
                if val['res']:
                    metric = val['res']["native_used_effectiveness"]
                    useful = 0
                    useless = 0
                    for num, cou in metric.items():
                        if num == '0':
                            useless += cou
                        else:
                            useful += cou
                    res.update({
                        f"{key}_useful": useful,
                        f"{key}_useless": useless
                    })
                else:
                    res.update({
                        f"{key}_useful": 0,
                        f"{key}_useless": 0
                    })
            except KeyError:
                if val['res']:
                    metric = val['res']["native_used_frequency"]
                    useful = 0
                    useless = 0
                    for num, cou in metric.items():
                        if "e0" in num:
                            useless += cou
                        else:
                            useful += cou
                    res.update({
                        f"{key}_useful": useful,
                        f"{key}_useless": useless
                    })
                else:
                    res.update({
                        f"{key}_useful": 0,
                        f"{key}_useless": 0
                    })
        return res

    def handle_count_mc_AccessibilityModify(self, pattern_info: dict, styles):
        res = {}
        for key, val in pattern_info["res"].items():
            if key not in styles:
                continue
            res[f"{key}_major"] = set()
            res[f"{key}_minor"] = set()
            for exa in val["res"]:
                mc = exa["metrics"]
                if "native_used_effectiveness" in mc.keys():
                    m = {True: "major", False: "minor"}
                    yx = sum([int(item) for _, item in mc["native_used_effectiveness"].items()])
                    try:
                        res[f'{key}_{m[yx <= 0]}'].add(mc["stability"]["maintenance_cost"]["extensive"]["filename"])
                    except Exception:
                        pass
        return res

    def handle_count_HiddenApi(self, pattern_info: dict):
        res = {}
        for key, val in pattern_info.items():
            if val['res']:
                metric = val['res']["acceptable_hidden"]
                res.update({
                    f"{key}_all_acceptable": metric['all_acceptable_hidden'],
                    f"{key}_mix_acceptable": metric['mix_acceptable_hidden'],
                    f"{key}_no_acceptable": metric['no_acceptable_hidden']
                })
            else:
                res.update({
                    f"{key}_all_acceptable": 0,
                    f"{key}_mix_acceptable": 0,
                    f"{key}_no_acceptable": 0
                })
        return res

    def handle_count_mc_HiddenApi(self, pattern_info: dict, styles):
        res = {}
        for key, val in pattern_info["res"].items():
            if key not in styles:
                continue
            res[f"{key}_major"] = set()
            res[f"{key}_minor"] = set()
            for exa in val["res"]:
                mc = exa["metrics"]
                if "acceptable_hidden" in mc.keys():
                    m = {True: "major", False: "minor"}
                    try:
                        res[f'{key}_{m[False in mc["acceptable_hidden"]]}'].add(
                            mc["stability"]["maintenance_cost"]["extensive"]["filename"])
                    except Exception:
                        pass
        return res

    def handle_count_ParameterListModifyDep(self, pattern_info: dict):
        res = {}
        for key, val in pattern_info.items():
            if val['res']:
                metric = val['res']["native_used_frequency"]
                res.update({
                    f"{key}_down": metric['n0_e1'] + metric['n1_e1'],
                    f"{key}_up": metric['n1_e0'],
                    f"{key}_no": metric['n0_e0']
                })
            else:
                res.update({
                    f"{key}_down": 0,
                    f"{key}_up": 0,
                    f"{key}_no": 0
                })
        return res

    def handle_count_mc_ParameterListModifyDep(self, pattern_info: dict, styles):
        res = {}
        for key, val in pattern_info["res"].items():
            if key not in styles:
                continue
            res[f"{key}_major"] = set()
            res[f"{key}_minor"] = set()
            for exa in val["res"]:
                mc = exa["metrics"]
                if "native_used_frequency" in mc.keys():
                    m = {True: "major", False: "minor"}
                    try:
                        res[f'{key}_{m[int(mc["native_used_frequency"]["used_by_extension"]) <= 0]}'].add(
                            mc["stability"]["maintenance_cost"]["extensive"]["filename"])
                    except Exception:
                        pass
        return res

    def handle_count_InheritExtension(self, pattern_info: dict):
        res = {}
        for key, val in pattern_info.items():
            if val['res']:
                metric = val['res']["is_inherit"]
                res.update({
                    f"{key}_is_inherit": metric['is_inherit'],
                    f"{key}_no_inherit": metric['no_inherit']
                })
            else:
                res.update({
                    f"{key}_is_inherit": 0,
                    f"{key}_no_inherit": 0
                })
        return res

    def handle_count_mc_InheritExtension(self, pattern_info: dict, styles):
        res = {}
        for key, val in pattern_info["res"].items():
            if key not in styles:
                continue
            res[f"{key}_major"] = set()
            res[f"{key}_minor"] = set()
            for exa in val["res"]:
                mc = exa["metrics"]
                if "is_inherit" in mc.keys():
                    m = {True: "major", False: "minor"}
                    try:
                        res[f'{key}_{m[len(mc["is_inherit"]) == 0]}'].add(
                            mc["stability"]["maintenance_cost"]["extensive"]["filename"])
                    except Exception:
                        pass
        return res

    def handle_count_ImplementExtension(self, pattern_info: dict):
        res = {}
        for key, val in pattern_info.items():
            if val['res']:
                metric = val['res']["is_new_implement"]
                res.update({
                    f"{key}_new_implement": metric['new_add_implement'],
                    f"{key}_modify_implement": metric['modify_implement']
                })
            else:
                res.update({
                    f"{key}_new_implement": 0,
                    f"{key}_modify_implement": 0
                })
        return res

    def handle_count_ReflectUse(self, pattern_info: dict):
        res = {}
        for key, val in pattern_info.items():
            if val['res']:
                metric = val['res']["open_in_sdk"]
                res.update({
                    f"{key}_all_not_in_sdk": metric['all_not_in_sdk'],
                    f"{key}_mix_in_sdk": metric['mix_in_sdk'],
                    f"{key}_all_in_sdk": metric['all_in_sdk']
                })
            else:
                res.update({
                    f"{key}_all_not_in_sdk": 0,
                    f"{key}_mix_in_sdk": 0,
                    f"{key}_all_in_sdk": 0
                })
        return res

    def handle_count_mc_ReflectUse(self, pattern_info: dict, styles):
        res = {}
        for key, val in pattern_info["res"].items():
            if key not in styles:
                continue
            res[f"{key}_major"] = set()
            res[f"{key}_minor"] = set()
            for exa in val["res"]:
                mc = exa["metrics"]
                if "open_in_sdk" in mc.keys():
                    m = {True: "major", False: "minor"}
                    try:
                        res[f'{key}_{m[len(mc["open_in_sdk"]["in_sdk"]) > 0]}'].add(
                            mc["stability"]["maintenance_cost"]["extensive"]["filename"])
                    except Exception:
                        pass
        return res


if __name__ == '__main__':
    patterns = ["FinalDel", "AccessibilityModify", "HiddenApi",
                "ParameterListModifyDep", "InheritExtension", "ReflectUse"]
    styles = [
        'del_native_class_final', 'del_native_method_final',
        'native_class_access_modify', 'native_method_access_modify',
        'call_native_hidden_method', 'use_native_hidden_variable',
        'native_method_add_parameter',
        'native_class_inherit_extensive_class',
        'extensive_method_reflect_native_method', 'extensive_method_reflect_native_class']

    MitigableFilter("../../../Data/Methodology/DroidDS-sample/output/res_metric_statistic.json", "./").handle_count(
        patterns, "L-18.1")
