
#data (vision) format
import base64
import json
import os
import oci
#request, io

#Oracle Vision configurations
config = oci.config.from_file('./home/ubuntu/.oci/config')
ai_service_vision_client = oci.ai_vision.AIServiceVisionClient(config=config)
analyze_image_details = oci.ai_vision.models.AnalyzeImageDetails()
inline_image_details = oci.ai_vision.models.InlineImageDetails()
image_object_detection_feature = oci.ai_vision.models.ImageObjectDetectionFeature()
image_text_detection_feature = oci.ai_vision.models.ImageTextDetectionFeature()

#creating a csv file to write the result text inside
f = open('/mnt/tiktok-pregnancy/features_text.csv', 'w')

#list the screenshots
image_files = os.listdir('./mnt/tiktok-pregnancy/frames/')
#img_file = '../02-Screenshot/Screenshots/vd#3EeEQLZgEVQ.mp4_frame_at_00_00_04.jpg'

#loop through all the screenshots in the folder
for img_file in image_files:
    #check if they end with jpg
    if img_file.endswith('.jpg'):
        #reading each image
        with open(f'./mnt/tiktok-pregnancy/frames/{img_file}', "rb") as image_file:
            #converting the image data to the base64 format that works with oracle
            encoded_string = base64.b64encode(image_file.read())
            features = [image_object_detection_feature, image_text_detection_feature]
            inline_image_details.data = encoded_string.decode('utf-8')
            analyze_image_details.image = inline_image_details
            analyze_image_details.features = features

            res = ai_service_vision_client.analyze_image(analyze_image_details=analyze_image_details)
            #the json result
            res_json = json.loads(repr(res.data))
            #print(len(res_json))
 
            # Write the detected objects to the CSV file
            f.write(f"{img_file}, {json.dumps(res_json)}\n")
f.close()
