# TikTok Pregnancy-Vape Data Collection README

## Introduction
This repository contains scripts for collecting data from TikTok, including videos, metadata, and visual insights. The data collection process involves several steps, each outlined below along with instructions for setup and usage.

## Requirements
- Python 3.x
- Required Python packages: `pyktok`, `opencv-python`, `requests`
- Oracle Cloud Vision API credentials (for visual insights extraction)

## Data Collection Steps
### 1. Metadata Extraction
- Search for hashtags on tiktok and the use zeeschuimer extension from https://github.com/digitalmethodsinitiative/zeeschuimer 

### 2. Deduplication
- Combine metadata from multiple hashtag pairs into a single dataset.
- Use the provided Python script for deduplication based on unique video IDs.
- Run combineHashtagMetadata.py

### 3. Video Download
- Utilize the `pyktok` library to download TikTok videos based on video IDs extracted during metadata collection.
- Modify the script to specify the desired video download settings and output directory.
- Run pyktokVideoCollection.py

### 4. Transcript Generation
- Extract text overlays and descriptions from videos.
- Transcribe files using OpenAI's Whisper.
- Set up whisper according to https://github.com/openai/whisper
- Run whisperTranscriptGenerator

### 5. Visual Insights Extraction
- Extract image frames from videos at regular intervals.
- Run framesGeneration.py
- Analyze frames using Oracle Cloud Vision API to identify objects, text, faces, and other visual elements.
- Record attributes such as detected faces, errors, image classification labels, and object detection model versions.
- This script in oracleFramefeatureExtractor.py

## Usage
- Run each script sequentially, following the instructions provided within the scripts.
- Customize script parameters as needed to suit specific data collection requirements.
- Ensure proper API credentials, permissions and setup Oracle Cloud Vision API according to Oracle documentation.

## Contributors
- Rujula Singh Rajendra Singh
- rujulasinghr@utexas.edu


