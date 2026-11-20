import sounddevice as sd
import soundfile as sf
import numpy as np
import os
import asyncio
from playsound import playsound
from groq import Groq
import edge_tts

# Inicializa o cliente Groq (não esqueça de setar a variável de ambiente GROQ_API_KEY)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def ouvir_usuario(duracao_segundos=5, taxa_amostragem=44100):
    print("\n🎤 Robô ouvindo (fale agora por 5 segundos)...")
    
    # Grava o áudio
    gravacao = sd.rec(int(duracao_segundos * taxa_amostragem), 
                      samplerate=taxa_amostragem, 
                      channels=1, 
                      dtype='float32')
    
    # Espera a gravação terminar
    sd.wait() 
    print("⏳ Processando...")
    
    nome_arquivo = "temp_gravacao.wav"
    # Salva o arquivo WAV
    sf.write(nome_arquivo, gravacao, taxa_amostragem)
    
    return nome_arquivo

def transcrever_audio(audio_path):
    try:
        with open(audio_path, "rb") as file:
            transcription = client.audio.transcriptions.create(
              file=(audio_path, file.read()),
              model="whisper-large-v3-turbo",
            )
        return transcription.text
    finally:
        # Limpa o arquivo temporário de áudio
        if os.path.exists(audio_path):
            os.remove(audio_path)

def gerar_resposta(texto):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Você é um robô de companhia amigável e conciso. Responda em no máximo duas frases."},
            {"role": "user", "content": texto}
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

async def falar_resposta(texto):
    arquivo_resposta = "resposta.mp3"
    communicate = edge_tts.Communicate(texto, "pt-BR-AntonioNeural")
    await communicate.save(arquivo_resposta)
    
    # Toca o áudio
    playsound(arquivo_resposta)
    
    # Limpa o arquivo mp3
    if os.path.exists(arquivo_resposta):
        os.remove(arquivo_resposta)

async def main():
    print("Iniciando sistema de voz... (Pressione Ctrl+C para sair)")
    while True:
        try:
            # 1. Ouvir
            audio_file = ouvir_usuario(duracao_segundos=5) # Você pode ajustar o tempo aqui
            
            # 2. Transcrever
            texto_usuario = transcrever_audio(audio_file)
            if not texto_usuario.strip():
                continue
            print(f"👤 Você: {texto_usuario}")
            
            # 3. Pensar
            resposta = gerar_resposta(texto_usuario)
            print(f"🤖 Robô: {resposta}")
            
            # 4. Falar
            await falar_resposta(resposta)
            
        except KeyboardInterrupt:
            print("\nEncerrando...")
            break
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    asyncio.run(main())