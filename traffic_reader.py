import pandas as pd  

csv_file = "/Users/shreeyagarg/spring2024/StoreFrontVisibility/traffic_data_sample.csv"

# Process in chunks (e.g., 100,000 rows at a time)  
chunk_size = 100000  
state_code = "CA"  
#segment_id = "10756719610000001"
chunks = []  
for chunk in pd.read_csv(csv_file, chunksize=chunk_size):  
    filtered_chunk = chunk[chunk["state_code"].str.contains(state_code, na=False, case=False)]  
    chunks.append(filtered_chunk)  

# Combine filtered chunks  
filtered_df = pd.concat(chunks)  

# Save to a smaller file  
filtered_df.to_csv("filtered_traffic_data.csv", index=False)  
pd.set_option("display.max_columns", None)
print("Saved as traffic_report.csv — Open in Excel for better viewing!")

print(filtered_df.head())  