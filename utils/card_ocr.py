import re

from .google_cloud import get_image_entity, get_text_annotations
from .image_processing import resize_image


def is_matches_digit_group(string):
    return re.match('^\d\d\d\d$', string) is not None


def extract_card_number(texts):
    for i in range(len(texts) - 3):
        texts_slice = [t.description for t in texts[i:i+4]]
        if all(is_matches_digit_group(text) for text in texts_slice):
            return ' '.join(texts_slice)
        
        
def get_card_number(image):
    image_entity = get_image_entity(image)
    tries = (
        get_text_annotations(image_entity),
        get_text_annotations(image_entity, is_handwritten=True)
    )
    for card_number_opt in map(extract_card_number, tries):
        if card_number_opt is not None:
            return card_number_opt
