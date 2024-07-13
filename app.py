from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

# Cargar frases desde el archivo JSON
with open('frases_benedetti.json', 'r', encoding='utf-8') as file:
    frases = json.load(file)['frases']

@app.route('/frases', methods=['GET'])
def obtener_frase():
    # Obtener una frase aleatoria
    frase = random.choice(frases)
    return jsonify(frase)

if __name__ == '__main__':
    app.run(debug=True)
