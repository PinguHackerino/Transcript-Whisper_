import sys
import shutil
from tkinter import filedialog, messagebox
import torch
import os
import whisper


def check_ffmpeg():
    """Verifica se FFmpeg è installato nel sistema.""" 
    if shutil.which("ffmpeg") is None:
        # Mostra un messaggio di errore all'utente se FFmpeg non è trovato
        messagebox.showerror(
            "Errore dipendenze",
            "FFmpeg non è installato o non è nel PATH di sistema.\n"
            "Whisper richiede FFmpeg per funzionare. Per favore, installalo."
        )
        sys.exit("FFmpeg mancante. Chiusura del programma.")

def check_gpu():
    if torch.cuda.is_available():
        print("GPU NVIDIA rilevata. Utilizzo della GPU per la trascrizione.")
        return True
    else:
        print("Nessuna GPU NVIDIA rilevata. Utilizzo della CPU per la trascrizione.")
        return False

# funzione per controllare che il file audio esista
def check_input(input_user, model):
    if os.path.exists(input_user):
     print(f"File '{input_user}' trovato. Inizio trascrizione...")
    else:
        raise FileNotFoundError(f"The file {input_user} does not exist.")  

