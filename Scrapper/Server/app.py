from flask import Flask, jsonify
import word_map

app = Flask(__name__)

@app.route('/rhyme/<word>', methods=['GET'])
def rhyme(word):
    result = word_map.ler_rimas(word)
    return jsonify(result)

# @app.route('/', methods=['GET'])
# def hello():
#     return "hello"

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
    # app.run(port=8000, debug=True)