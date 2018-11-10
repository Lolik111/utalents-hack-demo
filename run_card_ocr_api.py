#!/usr/bin/env python3

from flask import Flask, request, jsonify

from utils.card_ocr import get_card_number


app = Flask(__name__)


@app.route('/get_card_number', methods=['POST'])
def _():
    image_link = request.json.get('image_link')
    if image_link is None:
        return jsonify({'success': False})
    card_number_opt = get_card_number(image_link)
    if card_number_opt is None:
        return jsonify({'success': False})
    else:
        return jsonify({'success': True, 'card_number': card_number_opt})
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='7979')
    