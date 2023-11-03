from flask import Flask, request, jsonify

# app = Flask("meu app")
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, world"










# def reconhecimento_fala(audio_file, idioma):
#     # Implemente a lógica de reconhecimento de fala aqui
#     # Pode envolver a identificação do idioma, seleção do modelo e transcrição do áudio
#     # Retorne a transcrição como uma string
#     # Substitua esta função pelo seu código de reconhecimento de fala real
#     transcricao = f"Transcrição do áudio em {idioma}: {audio_file}"
#     return transcricao

# @app.route('/reconhecer_fala', methods=['POST'])
# def reconhecer_fala():
#     try:
#         arquivo_audio = request.files['audio']
#         idioma = request.form['idioma']

#         # Verifique se o arquivo de áudio e o idioma foram fornecidos
#         if not arquivo_audio or not idioma:
#             return jsonify({'erro': 'Arquivo de áudio e idioma são obrigatórios'}), 400

#         # Chame a função de reconhecimento de fala
#         transcricao = reconhecimento_fala(arquivo_audio, idioma)

#         return jsonify({'transcricao': transcricao}), 200

#     except Exception as e:
#         return jsonify({'erro': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
