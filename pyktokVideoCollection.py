# import pyktok as pyk
# import os


# pyk.specify_browser('firefox')


# save_directory = './downloaded_tiktoks'
# os.makedirs(save_directory, exist_ok=True)


# with open('tiktok_urls.txt', 'r') as file:
#     urls = file.readlines()

# for url in urls:
#     url = url.strip() 
#     video_id = url.split('/')[-1].split('?')[0]  

#     try:
#         pyk.save_tiktok(url, 
#                         True, 
#                         f'{video_id}_video_data.csv',
#                         'firefox')
#         print(f"Downloaded video and metadata for: {video_id}")
#     except Exception as e:
#         print(f"Failed to download video and metadata for {video_id}: {e}")

# print("All videos and metadata processed.")

import json
import os
import pyktok  

pyktok.specify_browser('firefox')


# Function to download the video and metadata
def download_tiktok_video(video_id):
    # Construct the TikTok URL
    video_url = f"https://www.tiktok.com/@tiktok/video/{video_id}"
    
    try:
        pyktok.save_tiktok(video_url, 
                        True, 
                        'video_data.csv',
                        'firefox')
        print(f"Downloaded video and metadata for: {video_id}")
    except Exception as e:
        print(f"Failed to download video and metadata for {video_id}: {e}")

# Read the NDJSON file and process each line
index = 0
with open('unique_video_ids2.ndjson', 'r') as file:
    for line in file:
        # Increment index
        index += 1
        # Replace 'your_folder_path' with the path to your folder
        folder_path = './Large_data/'
        data_point = json.loads(line)
        video_id = data_point['item_id']
        # Replace 'target_video_name.ext' with the name of the video file you're looking for, including its extension
        target_video_name = f"@tiktok_video_{video_id}.mp4"
        print(target_video_name)

        # List all files in the directory
        files_in_folder = os.listdir(folder_path)
        
        if target_video_name in files_in_folder:
            print("YAY")
        else:
            download_tiktok_video(video_id)
            
    

print("All videos and metadata processed.")
