import cv2
import os

# Define the directory path that contains the videos
video_directory = './Large_dataset/Large_data'
frame_directory = './frames'

def is_video_processed(video_file, frame_directory):
    # Check if any frame exists for this video
    video_base_name = os.path.splitext(video_file)[0]
    for frame_file in os.listdir(frame_directory):
        if frame_file.startswith(video_base_name):
            return True
    return False

# Create the frame directory if it does not exist
if not os.path.exists(frame_directory):
    os.makedirs(frame_directory)

# Iterate over all files in the video directory
for video_file in os.listdir(video_directory):
    if video_file.endswith(('.mp4', '.avi', '.mov')):  # Add or remove video formats as needed
        if is_video_processed(video_file, frame_directory):
            print(f"Skipping {video_file}, already processed.")
            continue  # Skip this video
        
        video_path = os.path.join(video_directory, video_file)
        cap = cv2.VideoCapture(video_path)

        fps = cap.get(cv2.CAP_PROP_FPS)  # Get the frames per second of the video
        frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            # Extract frames every second based on the video's FPS
            if frame_count % int(fps) == 0:
                frame_time = int(frame_count / fps)
                frame_filename = os.path.join(frame_directory, f"{os.path.splitext(video_file)[0]}_sec{frame_time}.jpg")
                cv2.imwrite(frame_filename, frame)
                print(f"Saved {frame_filename}")

            frame_count += 1

        cap.release()

print("Frame extraction is complete.")
