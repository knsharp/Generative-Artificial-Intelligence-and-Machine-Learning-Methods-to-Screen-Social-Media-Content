import os
import json

# Folder containing the NDJSON files
folder_path = './dataset'
# Output file for unique video IDs
output_file_path = 'unique_video_ids2.ndjson'

# Dictionary to hold unique video IDs and their data
unique_videos = {}
count=0
# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.ndjson'):
        file_path = os.path.join(folder_path, filename)
        # Open and read each line of the NDJSON file
        with open(file_path, 'r') as file:
            count=count+1
            for line in file:
                try:
                    # Parse the JSON object from the line
                    video_data = json.loads(line)
                    # Extract the video ID
                    video_id = video_data['item_id']
                    # If the video ID is not already in the dictionary, add it
                    if video_id not in unique_videos:
                        unique_videos[video_id] = video_data
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from file {filename} in line: {line}")

# Write the unique video entries to a new file
with open(output_file_path, 'w') as output_file:
    for video_data in unique_videos.values():
        # Convert the JSON object to a string and write it to the output file
        output_file.write(json.dumps(video_data) + '\n')
print(count)
print(f"Unique video IDs have been consolidated into {output_file_path}")
