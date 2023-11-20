# Assuming 'source_data' is the DataFrame from the previous step
source_data['text_column'] = source_data['text_column'].str.upper()

# Print the transformed data
print(source_data)
