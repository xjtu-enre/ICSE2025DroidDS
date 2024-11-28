import csv
import json
import os
import subprocess

def execute_command(command):
    return subprocess.check_output(command, shell=True).decode('utf-8').strip()

def get_parent_commit_id(commit_id):
    cmd_show = f"git show {commit_id}"
    output = execute_command(cmd_show)
    for line in output.split('\n'):
        if line.startswith("Merge:"):
            return line.split()[1]
    return None

def get_code_block(filepath, loc_range):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        start, end, _ = loc_range
        return ''.join(lines[start-1:end])

def main():
    OUTPUT_DIR = "D:/Master1-group/conflict_record/conf_text/lineage-17.1-block_text/" # folder to store all json files
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open("D:/Master1-group/conflict_record/conf_meths/lineage-17.1-meths.csv", "r") as file: 
        csv_reader = csv.reader(file)
        next(csv_reader)  # skip header

        data_dict = {}

        for index, row in enumerate(csv_reader):
            merge_commitid = row[1]
            file_path = row[2]
            loc_details_str = row[6]

            os.chdir("Lineage")
            parent_commitid = get_parent_commit_id(merge_commitid)
            print("merge_commitid:", merge_commitid)
            print("parent_commitid:", parent_commitid)
            execute_command(f"git reset --hard {parent_commitid}")
            
            locs = eval(loc_details_str)
            full_file_path = os.path.join(os.getcwd(), file_path)
            code_blocks = [get_code_block(full_file_path, loc) for loc in locs]

            entry = {
                "id": index + 1,
                "name": os.path.basename(file_path),
                "merge_commitid": merge_commitid,
                "File": file_path,
                "block_details": [{"loc": {"startLine": loc[0], "endLine": loc[1], "confLOC": loc[2]}, "block_text": block} for loc, block in zip(locs, code_blocks)]
            }

            if merge_commitid not in data_dict:
                data_dict[merge_commitid] = []

            data_dict[merge_commitid].append(entry)
            os.chdir("..")

        for commit_id, entries in data_dict.items():
            with open(os.path.join(OUTPUT_DIR, f"{commit_id}.json"), "w") as out_file:
                json.dump(entries, out_file, indent=4)

if __name__ == "__main__":
    main()
