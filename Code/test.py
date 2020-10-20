import io
import os
import pdb

# Imports the Google Cloud client library
from google.cloud import vision
from google.oauth2 import service_account

pdb.set_trace()

credentials = service_account.Credentials.from_service_account_file('Project-491c3b474809.json')
client = vision.ImageAnnotatorClient(credentials=credentials)

# The name of the image file to annotate
file_name = os.path.abspath('result.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

pdb.set_trace()

print('Labels:')
for label in labels:
    print(label.description)
