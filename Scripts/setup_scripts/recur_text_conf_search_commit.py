import os
import json
import csv
from collections import defaultdict
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# determines if there are duplicates
def is_duplicate(entry, existing_entries):
    for existing_entry in existing_entries:
        if (sorted(entry["merge_commitid"]) == sorted(existing_entry["merge_commitid"]) and
            #sorted(entry["recurBlockSrc"]) == sorted(existing_entry["recurBlockSrc"]) and
            entry["file"] == existing_entry["file"] and
            sorted(entry["Loc_details"]) == sorted(existing_entry["Loc_details"]) and
            sorted(entry["proportion"]) == sorted(existing_entry["proportion"])):
            return True
    return False

def main():
    directory = './conf_text2/omnirom-11-block_text/'
    files = [f for f in os.listdir(directory) if f.endswith('.json')]

    data = {}
    for file in files:
        with open(os.path.join(directory, file), 'r') as f:
            data[file] = json.load(f)

    results = []
    id_counter = 1

    for file1, content1 in data.items():
        for file2, content2 in data.items():
            if file1 == file2:
                continue

            for entity1 in content1:
                for entity2 in content2:
                    if entity1["name"] == entity2["name"] and entity1["File"] == entity2["File"]:
                        for block1 in entity1["block_details"]:
                            for block2 in entity2["block_details"]:
                                if not block1["block_text"] or not block2["block_text"]:
                                    continue
                                
                                similarity = similar(block1["block_text"], block2["block_text"])
                                if similarity >= 0.5:
                                    loc_details = [(block1["loc"]["startLine"], block1["loc"]["endLine"], block1["loc"]["confLOC"]),
                                                   (block2["loc"]["startLine"], block2["loc"]["endLine"], block2["loc"]["confLOC"])]
                                    block_texts = [block1["block_text"], block2["block_text"]]
                                    recur_segment = SequenceMatcher(None, block1["block_text"], block2["block_text"]).find_longest_match(0, len(block1["block_text"]), 0, len(block2["block_text"]))
                                    common_segment = block1["block_text"][recur_segment.a:recur_segment.a + recur_segment.size]
                                    proportions = [round(len(common_segment) / len(block1["block_text"]), 3), round(len(common_segment) / len(block2["block_text"]), 3)]
                                    
                                    # Only add to results if at least one proportion value is >= 0.5
                                    if all(p >= 0.5 for p in proportions):
                                        result = {
                                            "id": id_counter,
                                            "merge_commitid": [entity1["merge_commitid"], entity2["merge_commitid"]],
                                            "file": entity1["File"],
                                            "Loc_details": loc_details,
                                            "recur_segment": common_segment,
                                            "proportion": proportions
                                        }
                                        
                                        # Split block_texts into separate fields
                                        for idx, text in enumerate(block_texts):
                                            result[f"block_text_{idx + 1}"] = text
                                        
                                        # Check if the result is a duplicate before adding
                                        if not is_duplicate(result, results):
                                            results.append(result)
                                            id_counter += 1

    # Define csv fieldnames dynamically based on results
    fieldnames = ["id", "merge_commitid", "file", "Loc_details"]
    max_block_text_fields = max([len([key for key in res.keys() if key.startswith("block_text_")]) for res in results])
    for i in range(max_block_text_fields):
        fieldnames.append(f"block_text_{i + 1}")
    fieldnames.extend(["recur_segment", "proportion"])

    with open('./recur-block/text/diff-commit/omnirom-11-recur_textblock.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)

if __name__ == "__main__":
    main()
