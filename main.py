from flask import Flask, jsonify, request

app = Flask(__name__)

paises = [
    {
        'nome': 'Brasil',
        'sigla': 'BRA',
        'continente': 'América do Sul'
    },
    {
        'nome': 'Estados Unidos',
        'sigla': 'EUA',
        'continente': 'América do Norte'
    }
]


@app.route('/pais')
def get_paises():
    return jsonify({'paises': paises})


@app.route('/pais', methods=['POST'])
def post_pais():
    requisicao = request.get_json()
    for pais in paises:
        if pais['nome'].lower() == requisicao['nome'].lower():
            return jsonify({'mensagem': 'País já cadastrado'})

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


@app.route('/pais/<string:nome>', methods=['DELETE'])
def delete_pais_by_nome(nome):
    for pais in paises:
        if pais['nome'].lower() == nome.lower():
            paises.remove(pais)
            return jsonify({'mensagem': 'País deletado com sucesso'})
    return jsonify({'mensagem': 'País de nome -' + nome + '- nao encontrado'})


app.run()
