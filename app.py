from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def mostrar_frase_auspiciosa():
    frase = frotar(1)[0]
    return frase

@app.route('/frotar/<int:n_frases>', methods=['GET'])
def obtener_frases_auspiciosas(n_frases):
    frases = frotar(n_frases)
    return jsonify(frases)

if __name__ == '__main__':
    app.run()


