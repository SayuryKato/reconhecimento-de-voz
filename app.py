from flask import Flask, request, render_template, jsonify, redirect, url_for
import speech_recognition as sr
from gtts import gTTS
import pickle

app = Flask(__name__)
## carregando o modelo para o código
with open("reconehcimentoVoz.pickle", "rb") as file:
    modelo_carregado = pickle.load(file)

# Função para pré-processar o espectrograma para o modelo
def preprocess_spectrogram_for_model(spectrogram):
    try:
        # Redimensione o espectrograma para o tamanho esperado pelo modelo
        input_size = (model_input_height, model_input_width)  # Substitua pelos valores reais
        preprocessed_spectrogram = resize_spectrogram(spectrogram, input_size)

        # Realize a normalização, se necessário
        preprocessed_spectrogram = normalize_spectrogram(preprocessed_spectrogram)

        return preprocessed_spectrogram
    except Exception as e:
        raise Exception(f"Erro ao pré-processar o espectrograma para o modelo: {str(e)}")

# Função para redimensionar o espectrograma para o tamanho esperado
import numpy as np
import cv2  # Certifique-se de ter a biblioteca OpenCV instalada

# Função para redimensionar o espectrograma para o tamanho esperado
def resize_spectrogram(spectrogram, target_size):
    try:
        # Redimensione o espectrograma usando bibliotecas como OpenCV
        # Implemente a lógica de redimensionamento aqui
        # Certifique-se de redimensionar corretamente o espectrograma para o tamanho esperado pelo modelo
        preprocessed_spectrogram = cv2.resize(spectrogram, target_size, interpolation=cv2.INTER_LINEAR)

        return preprocessed_spectrogram
    except Exception as e:
        raise Exception(f"Erro ao redimensionar o espectrograma: {str(e)}")

# Função para normalizar o espectrograma, se necessário
# Função para normalizar o espectrograma, se necessário
def normalize_spectrogram(spectrogram):
    try:
        # Implemente a lógica de normalização aqui
        # Você pode realizar normalização min-max, z-score, ou outro método apropriado
        # Certifique-se de que o espectrograma esteja normalizado no intervalo esperado pelo modelo

        # Exemplo de normalização min-max:
        min_value = np.min(spectrogram)
        max_value = np.max(spectrogram)
        normalized_spectrogram = (spectrogram - min_value) / (max_value - min_value)

        return normalized_spectrogram
    except Exception as e:
        raise Exception(f"Erro ao normalizar o espectrograma: {str(e)}")

def preprocess_audio(audio_data):
    try:
        # Converta o áudio em um espectrograma usando a biblioteca librosa
        y, sr = librosa.load(io.BytesIO(audio_data), sr=None)
        spectrogram = librosa.feature.melspectrogram(y, sr=sr)
        # Realize o pré-processamento adicional, como normalização, redimensionamento, etc.
        return spectrogram
    except Exception as e:
        raise Exception(f"Erro ao pré-processar o áudio: {str(e)}")



# Função para fazer previsões com base no modelo carregado
def model_predict(spectrogram):
    try:
        # Realize qualquer processamento adicional necessário para alimentar o espectrograma no modelo
        # Suponha que você tenha um modelo carregado em 'modelo_carregado'
        # Certifique-se de que o modelo esperado esteja configurado corretamente
        # Por exemplo, converta o espectrograma para o formato de entrada esperado pelo modelo
        input_data = preprocess_spectrogram_for_model(spectrogram)

        # Faça previsões com base no modelo
        predictions = modelo_carregado.predict(input_data)

        # Retorne as previsões
        return predictions
    except Exception as e:
        raise Exception(f"Erro ao fazer previsões: {str(e)}")



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if "audio" in request.files:
            try:
                # Receba um arquivo de áudio do formulário
                audio_file = request.files["audio"]

                # Realize a conversão de áudio para texto usando o modelo
                audio_data = audio_file.read()

                # Faça o pré-processamento dos dados de áudio, converta para espectrograma, etc.
                spectrogram = preprocess_audio(audio_data)

                # Faça previsões usando o modelo carregado
                predictions = model_predict(spectrogram)

                return render_template('result2.html',transcript=predictions)
            except Exception as e:
                return jsonify({"error": str(e)})

    return render_template('index.html')

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


# transcribed_text = transcribe_audio(audio_file)
# def transcribe_audio(audio_file):
#     try:
#         transcript = recognizer.recognize_google(audio_data)  # Usando o reconhecimento de fala do Google
#         transcript = model

#         return transcript
#     except sr.UnknownValueError:
#         return "Não foi possível reconhecer a fala"
#     except sr.RequestError as e:
#         return f"Erro ao se conectar ao serviço de reconhecimento de fala: {e}"