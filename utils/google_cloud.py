import cv2
import numpy as np

from google.cloud import vision_v1p3beta1 as vision
from google.oauth2 import service_account


credentials = service_account.Credentials.from_service_account_file('./google-api-credential.json')
client = vision.ImageAnnotatorClient(credentials=credentials)


def get_image_entity(image):
    if isinstance(image, str):
        image_entity = vision.types.Image()
        image_entity.source.image_uri = image
    elif isinstance(image, np.ndarray):
        cv2.imwrite('temp.jpg', image)
        with open('temp.jpg', 'rb') as file:
            image_content = file.read()
        image_entity = vision.types.Image(content=image_content)
    else:
        raise Exception('No parser found')
    return image_entity


def get_text_annotations(image_entity, is_handwritten=False):
    if is_handwritten:
        context = vision.types.ImageContext(language_hints=['en-t-i0-handwrit'])
        response = client.document_text_detection(image=image_entity, image_context=context)
    else:
        response = client.document_text_detection(image=image_entity)
    return response.text_annotations
