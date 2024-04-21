from flask import Flask, jsonify, request
from bayeta import frotar, insertar_frases

app = Flask(__name__)

@app.route('/')
def mostrar_frase_auspiciosa():
    frase = frotar(1)[0]
    return frase

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def obtener_frases_auspiciosas(n_frases):
    frases = frotar(n_frases)
    return jsonify(frases)

@app.route('/frotar/add', methods=['POST'])
def agregar_frases():
    frases_nuevas = request.get_json()
    insertar_frases(frases_nuevas)
    return '', 200

if __name__ == '__main__':
    app.run()


