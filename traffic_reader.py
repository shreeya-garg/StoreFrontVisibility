import pandas as pd  

def traffic_for_osm(osm_id):
    median = 3118.0
    #csv_file = "/Users/shreeyagarg/spring2024/StoreFrontVisibility/traffic_data_sample.csv"   ##NEED TO CONVERT THIS TO NOT BE COMPLETE PATH
    csv_file = "traffic_data_sample.csv"

    # Process in chunks (e.g., 100,000 rows at a time)  
    chunk_size = 100000  
    chunks = []  
    for chunk in pd.read_csv(csv_file, chunksize=chunk_size):  
        filtered_chunk = chunk[chunk['osm_id'] == osm_id]
        chunks.append(filtered_chunk)  
    
    # Combine filtered chunks  
    filtered_df = pd.concat(chunks)  

    if filtered_df.empty:
        direction_1 = median
        direction_2 = median
        direction_3 = median
    
    # Compute the mean per direction  
    else: 
        traffic_by_direction = filtered_df.groupby("match_dir")["trips_volume_masked"].mean()

        
        direction_1 = traffic_by_direction.get(1, None)
        direction_2  = traffic_by_direction.get(2, None)
        direction_3 = traffic_by_direction.get(3, None)
    
        #Handle Missing Scenarios 
        if(direction_1 == None and direction_2 == None and direction_3 ==None) :
            direction_1 = median
            direction_2 = median
            direction_3 = median 
        elif(direction_1 == None and direction_2 == None): 
            direction_1 = direction_3
            direction_2 = direction_3
        elif(direction_1 == None) :
            direction_1 = direction_2 
        elif(direction_2 ==None):
            direction_2 = direction_1
    

    print(direction_1)
    print(direction_2)
    print(direction_3)
    filtered_df.to_csv("filtered_traffic_data.csv", index=False)  
    print("Saved as traffic_report.csv — Open in Excel for better viewing!")
    return(direction_1, direction_2, direction_3)

    # Save to a smaller file  



#traffic_for_osm("245700194")



def road_name_csv(road_name):
    csv_file = "/Users/shreeyagarg/spring2024/StoreFrontVisibility/traffic_data_sample.csv"   ##NEED TO CONVERT THIS TO NOT BE COMPLETE PATH

    # Process in chunks (e.g., 100,000 rows at a time)  
    chunk_size = 100000  
    chunks = []  
    for chunk in pd.read_csv(csv_file, chunksize=chunk_size):  
        filtered_chunk = chunk[chunk["segment_name"].astype(str).str.contains(str(road_name), na=False, case=False)]
        chunks.append(filtered_chunk)  
    filtered_df = pd.concat(chunks)  
    filtered_df.to_csv("filtered_traffic_data.csv", index=False)  
    print("Saved as traffic_report.csv — Open in Excel for better viewing!")

#road_name_csv("Techwood")