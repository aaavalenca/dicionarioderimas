from flask import Flask, jsonify, request
from collections import defaultdict

app = Flask(__name__)

word_map = defaultdict(list)

@app.route('/get_associated_words', methods=['GET'])

def get_associated_words():
    word = request.args.get('word')
    associated_words = word_map.get(word, [])
    return jsonify({'palavra': word, 'rimas': associated_words})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)