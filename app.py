from flask import Flask, request, render_template, jsonify, redirect, url_for
import speech_recognition as sr
from gtts import gTTS

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
    try:
        transcript = recognizer.recognize_google(audio_data)  # Usando o reconhecimento de fala do Google
        return transcript
    except sr.UnknownValueError:
        return "Não foi possível reconhecer a fala"
    except sr.RequestError as e:
        return f"Erro ao se conectar ao serviço de reconhecimento de fala: {e}"

@app.route('/result', methods=['POST'])
def result():
    if request.form.get('audio'):
        audio_file = request.form['audio']
        transcribed_text = transcribe_audio(audio_file)
        return render_template('result.html',result=transcribed_text)

    elif request.form.get('text'):
        text = request.form['text']
        tts = gTTS(text)
        tts.save('static/output.mp4')  # Salve o arquivo no diretório 'static'
        return render_template('result.html', result="Áudio gerado")

if __name__ == '__main__':
    app.run(debug=True)

#teste
# @app.route('/api/asr', methods=['POST'])
# def asr():
#     audio_data = request.files['audio']
#     # Chame o modelo ASR para processar o áudio e obter o texto reconhecido
#     recognized_text = process_audio_with_asr(audio_data)
#     return jsonify({'text': recognized_text})

# def process_audio_with_asr_model(audio_file):
#     # Carregar o modelo ASR
#     model = tf.saved_model.load("caminho_para_o_modelo_salvo")
#     # Faça a inferência com o modelo ASR
#     recognized_text = model.infer(audio_file)
#     return recognized_text

# @app.route('/upload', methods=['POST'])
# def upload():
#     if 'audio_file' not in request.files:
#         return "Nenhum arquivo de áudio enviado"

#     audio_file = request.files['audio_file']
    
#     # Chame a função que processa o áudio com o modelo ASR
#     recognized_text = process_audio_with_asr_model(audio_file)

#     return render_template('result.html', result=recognized_text)

# if __name__ == '__main__':
#     app.run(debug=True)






# @app.route('/', methods=['GET', 'POST'])
# def index():
#     

#     return render_template('index.html')

# def transcribe_audio(audio_file):
#     recognizer = sr.Recognizer()

#     with sr.AudioFile(audio_file) as source:
#         audio_data = recognizer.record(source)

#     try:
#         transcript = recognizer.recognize_google(audio_data)  # Usando o reconhecimento de fala do Google
#         return transcript
#     except sr.UnknownValueError:
#         return "Não foi possível reconhecer a fala"
#     except sr.RequestError as e:
#         return f"Erro ao se conectar ao serviço de reconhecimento de fala: {e}"



    # if request.method == 'POST':
    #     audio_file = request.files['audio']  # Obter o arquivo de áudio do formulário

    #     if audio_file:
    #         transcribed_text = transcribe_audio(audio_file)
    #         return render_template('result.html', transcript=transcribed_text)