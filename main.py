from flask import Flask, jsonify, request

app = Flask(__name__)

paises = [
    {
        'nome': 'Brasil',
        'sigla': 'BRA',
        'continente': 'América'
    }
]


@app.route('/pais')
def get_paises():
    return jsonify({'paises': paises})


@app.route('/pais', methods=['POST'])
def post_pais():
    requisicao = request.get_json()
    novo_pais = {
        'nome': requisicao['nome'],
        'sigla': requisicao['sigla'],
        'continente': requisicao['continente']
    }
    paises.append(novo_pais)
    return jsonify(novo_pais)


@app.route('/pais/<string:sigla>')
def get_pais_by_sigla(sigla):
    for pais in paises:
        if pais['sigla'].lower() == sigla.lower():
            return jsonify(pais)
    return jsonify({'mensagem': 'País de sigla -' + sigla + '- nao encontrado'})


app.run()
