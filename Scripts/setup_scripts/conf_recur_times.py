import pandas as pd
from ast import literal_eval

encoding = 'ISO-8859-1'

# Step 1: Read the CSV file
input_file = './diffProgect-sap-recur_textblock-<name>.csv'
df = pd.read_csv(input_file, encoding=encoding)


df['merge_commitid'] = df['merge_commitid'].apply(literal_eval)
df['recurBlockSrc'] = df['recurBlockSrc'].apply(literal_eval)

# Convert string representations of lists and tuples back into Python objects
groups = df.groupby(['file', 'recur_segment'])

# A list to store the final results
results = []

# Step 3: Loop through each group
for (file, recur_segment), group in groups:
    # Merge the 'merge_commitid' list and remove duplicates
    merged_commitids = set()
    for commitids in group['merge_commitid']:
        merged_commitids.update(commitids)

    # Merge the 'recurBlockSrc' list and remove duplicates
    recurBlockSrcs = set()
    for recurBlockSrc in group['recurBlockSrc']:
        recurBlockSrcs.update(recurBlockSrc)
    
    # Add to the result list
    results.append({
        'file': file,
        'merge_commitid': list(merged_commitids),
        'recurBlockSrc': list(recurBlockSrcs),
        'recur_segment': recur_segment,
        'times': len(merged_commitids)
    })

# Convert result list to DataFrame
results_df = pd.DataFrame(results)

results_df.reset_index(inplace=True, drop=True)
results_df.index += 1
results_df.reset_index(inplace=True)
results_df.rename(columns={'index': 'id'}, inplace=True)

# Step 4: Save the processed data to a new CSV file
output_file = './diffProgect-sap-recur_textblock-<name>_times.csv'
results_df.to_csv(output_file, index=False, encoding=encoding)

print(f'Processed data has been saved to {output_file}.')
