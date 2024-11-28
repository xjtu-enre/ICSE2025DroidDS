import numpy as np
import pandas as pd
from scipy.stats import wilcoxon


def compute_avg_merged_mc(aff_files_csv_filepath, mc_csv_filepath):
    all_pro_metric = pd.DataFrame()
    aff_files_df = pd.read_csv(aff_files_csv_filepath)
    aff_files_df = aff_files_df.query('aff_files_count != 0')
    for _, row in aff_files_df.iterrows():
        project = row['project']
        aff_files = row['aff_files']
        mc_csv_df = pd.read_csv(mc_csv_filepath)
        # Split aff_files into a list of files
        aff_files_set = set(aff_files.strip("").split(","))
        aff_files_list = list(aff_files_set)
        # Extract 'filename' column and convert to list
        all_filename_list = mc_csv_df['filename'].tolist()
        non_aff_files_list = list(set(all_filename_list) - set(aff_files_list))
        # Split based on values in the filename column
        aff_files_mc_csv = mc_csv_df[mc_csv_df['filename'].isin(aff_files_list)]
        non_aff_files_mc_csv = mc_csv_df[mc_csv_df['filename'].isin(non_aff_files_list)]

        single_metric_data = {
            'project': project,
            'avg_#author_aff': aff_files_mc_csv['#author'].mean(),
            'avg_#author_nonaff': non_aff_files_mc_csv['#author'].mean(),
            'avg_#changeCmt_aff': aff_files_mc_csv['#cmt'].mean(),
            'avg_#changeCmt_nonaff': non_aff_files_mc_csv['#cmt'].mean(),
            'avg_#changeLoc_aff': aff_files_mc_csv['changeloc'].mean(),
            'avg_#changeLoc_nonaff': non_aff_files_mc_csv['changeloc'].mean(),
            'avg_#issue_aff': aff_files_mc_csv['#issue'].mean(),
            'avg_#issue_nonaff': non_aff_files_mc_csv['#issue'].mean(),
            'avg_#issueCmt_aff': aff_files_mc_csv['#issue-cmt'].mean(),
            'avg_#issueCmt_nonaff': non_aff_files_mc_csv['#issue-cmt'].mean(),
            'avg_#issueLoc_aff': aff_files_mc_csv['issueLoc'].mean(),
            'avg_#issueLoc_nonaff': non_aff_files_mc_csv['issueLoc'].mean()
        }
        sig_pro_metric = pd.DataFrame([single_metric_data])
        all_pro_metric = pd.concat([all_pro_metric, sig_pro_metric], ignore_index=True)

    all_pro_metric.to_csv("sample-metrics.csv", index=False)
    print(f"output metrics")

if __name__ == '__main__':
    # single project test
    sample_aff_files_csv = "../../../Data/Methodology/DroidDS-sample/output/all_aff_files.csv"
    sample_mc_csv = "../../../Data/Methodology/DroidDS-sample/output/file-mc_ext.csv"

    compute_avg_merged_mc(sample_aff_files_csv, sample_mc_csv)
