import os
import sys
import time
import shutil
import traceback
import tkinter as tk
from tkinter import filedialog, messagebox
import torch
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


def file_dialog(window):
    """Apre una finestra di dialogo per permettere all'utente di selezionare un file audio."""
    file_path = filedialog.askopenfilename(
        title="Seleziona un file audio",
        filetypes=(("Audio Files", "*.mp3;*.wav;*.m4a;*.mp4"), ("All Files", "*.*"))
    )
    return file_path

# funzione per controllare che il file audio esista
def check_input(input_user, model):
    if os.path.exists(input_user):
        result = model.transcribe(input_user, language="it")
        # stampa il risultato della trascrizione
        return result["text"]
    else:
        raise FileNotFoundError(f"The file {input_user} does not exist.")  

# funzione per la trascrizione
def transcribe_file(path_file, model):
    """Esegue la trascrizione del file audio utilizzando il modello Whisper specificato."""
    print(f"Trascrizione del file '{os.path.basename(path_file)}' in corso...")
    
    # Esegue la trascrizione forzando la lingua italiana
    result = model.transcribe(path_file, language="it")
    return result["text"]


def save_transcription(text_transcripted):
    """Apre una finestra di dialogo per salvare il testo in un file .txt."""
    path_output = filedialog.asksaveasfilename(
        title="Salva trascrizione come...",
        defaultextension=".txt",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    
    # Se l'utente annulla il salvataggio
    if not path_output:
        print("Salvataggio annullato dall'utente.")
        return None
        
    # Scrive il testo nel file specificato
    with open(path_output, "w", encoding="utf-8") as f:
        f.write(text_transcripted)
        
    return path_output


def main():
    # Inizializza la finestra nascosta di Tkinter per i dialoghi GUI
    window = tk.Tk()    
    window.withdraw()
    window.update()  # Forza l'aggiornamento per evitare bug visivi
    
    # Controlla se FFmpeg è disponibile prima di iniziare le operazioni pesanti
    check_ffmpeg()

    try:
        # Carica il modello Whisper
        print("Caricamento del modello Whisper 'medium'...")
        model = whisper.load_model("medium")
        
        # Gestione hardware (Sposta il calcolo su GPU se disponibile)
        if torch.cuda.is_available():
            model = model.to(torch.device("cuda"))
            print("Modello caricato con successo sulla GPU (CUDA).")
        else:
            model = model.to(torch.device("cpu"))
            print("CUDA non disponibile. Utilizzo della CPU.")

        # Selezione del file audio tramite interfaccia grafica
        print("In attesa della selezione del file audio...")
        percorso_file = file_dialog(window)
        
        if not percorso_file:
            print("Nessun file selezionato. Uscita.")
            return

        # Avvio del processo di trascrizione con misurazione del tempo
        start_time = time.time()
        testo_trascritto = transcribe_file(percorso_file, model)
        elapsed_time = time.time() - start_time
        
        print("Trascrizione completata con successo!")
        print(f"Tempo impiegato: {elapsed_time:.2f} secondi.")

        # Salvataggio del file
        percorso_output = save_transcription(testo_trascritto)
        
        if percorso_output:
            print(f"Trascrizione salvata in:\n{percorso_output}")
            messagebox.showinfo(
                "Operazione completata",
                f"Trascrizione completata e salvata in:\n{percorso_output}"
            )
        
    except Exception as e:
        # Gestione degli errori: salva i dettagli in un file di log e mostra un popup
        error_message = f"Errore: {str(e)}\n{traceback.format_exc()}"
        print(error_message)
        
        with open("error_log.txt", "w", encoding="utf-8") as f:
            f.write(error_message)
            
        messagebox.showerror(
            "Errore durante l'esecuzione", 
            f"Si è verificato un errore imprevisto:\n{str(e)}\n\nI dettagli completi sono stati salvati in 'error_log.txt'"
        )


if __name__ == "__main__":
    main()