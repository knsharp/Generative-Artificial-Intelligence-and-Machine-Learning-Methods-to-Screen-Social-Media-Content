import os
import whisper
import csv

# Load the Whisper model
model = whisper.load_model("base")

# Specify the directory containing your video files
video_directory = "./Largest-dataset/Large_data/"
# Specify the output CSV file
output_csv_file = "./transcriptions_large_data.csv"

# Function to transcribe a video file
def transcribe_video(video_path):
    result = model.transcribe(video_path)
    return result["text"]

# Check if the output CSV file already exists
if os.path.exists(output_csv_file):
    # If it exists, load existing filenames into a set
    existing_filenames = set()
    with open(output_csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            existing_filenames.add(row[0])

# Process all video files in the directory and write results to a CSV file
with open(output_csv_file, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    if os.path.getsize(output_csv_file) == 0:  # If the file is empty, write header
        writer.writerow(["Video File", "Transcription"])
    
    for filename in os.listdir(video_directory):
        if filename.endswith((".mp4", ".avi", ".mov")):  # Add or remove file extensions as needed
            if filename not in existing_filenames:  # Check if the file has already been processed
                video_path = os.path.join(video_directory, filename)
                try:
                    print(f"Processing {filename}...")
                    transcription = transcribe_video(video_path)
                    writer.writerow([filename, transcription])
                    print(f"Finished processing {filename}.")
                except Exception as e:
                    print(f"Error processing {filename}: {e}")
            else:
                print(f"Skipping {filename} as it already exists in the CSV.")

print("All videos have been processed and results are saved in", output_csv_file)
