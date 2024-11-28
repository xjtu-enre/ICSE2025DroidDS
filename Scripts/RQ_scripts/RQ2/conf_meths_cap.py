import pandas as pd

meths = pd.read_csv('./conf_meths/honor-u-meths.csv')
all_aff_files = pd.read_csv('all_aff_files-honor.csv')

# Filter out entries for the UMagicOS version
filtered_aff_files = all_aff_files[(all_aff_files['project'] == 'MagicOS') & (all_aff_files['version'] == 'UMagicOS')]

aff_files_list = []
for files in filtered_aff_files['aff_files'].str.split(','):
    aff_files_list.extend(files)

# check if the file path in meths exists in aff_files_list
meths['is_in_aff_files'] = meths['Conf_details'].apply(lambda x: x in aff_files_list)

# Keep the entries existing in aff_files_list
final_data = meths[meths['is_in_aff_files']]

# optionally print or save final_data
print(final_data)

# Save the processed data to a new CSV file
final_data.to_csv('./conf_meths_cap/honor-u-SAP-meths.csv', index=False)
