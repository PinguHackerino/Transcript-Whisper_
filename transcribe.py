import whisper
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import time
import torch
import traceback
import subprocess
import sys
"""""
def check_ffmpeg(): # funzione per verificare l'installazione di ffmpeg
    check = False
   
    i = 0
    try:
        return_code = subprocess.run(["ffmpeg"], shell= False, text=True)
        if(return_code == 0):
            print("ffmpeg is intalled")
            return True
        else:
            while i < 3:
                choice = input("ffmpeg isn't install, if you want i can install it for you y/n: ")
                if(choice == "y"):
                    print("great i will start now....")
                    #install_ffmpeg
                    return True
                elif(choice == "n"):
                    sys.exit("ok, i think you would install by yourself, see you soon")
                else:
                    print("sorry, but you have to write Y for yes or N for no")
                    i += 1
            sys.exit("sorry too many attempt, you have 3 attempt")
                
    except Exception as e:
        print("ffmpeg has some problems")

def install_ffmpeg():
    try:
        pass
    except Exception as e:
        print("various problem")
    pass

def check_torch():
    pass
"""""
# funzione per il dialogo di selezione del file audio
def file_dialog(window):
    file_path = filedialog.askopenfilename(title="Select an audio file",filetypes=(("Audio Files", "*.mp3;*.wav;*.m4a;*.mp4"), ("All Files", "*.*")))
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
# esegui la trascrizione
    risultato = model.transcribe(path_file, language="it")
# stampa il risultato della trascrizione
    return risultato["text"]

# funzione per salvare la trascrizione su file
def save_transcription(root, text_transcripted, path_output=None):
    if not path_output:
        path_output = filedialog.asksaveasfilename(
            title="Salva trascrizione come...",
            defaultextension=".txt",
            filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
        )
        if not path_output:
            print("Salvataggio annullato.")
            return None
    with open(path_output, "w", encoding="utf-8") as f:
        f.write(text_transcripted)
    return path_output

# Funzione principale
def main():
    window = tk.Tk()    
    window.withdraw()
    window.update()  #forza aggiornamento

    ##check_ffmpeg()

    try:
#carica il modello Whisper (questa operazione può richiedere tempo)
        print("Caricamento del modello Whisper...")
        model = whisper.load_model("medium")
        
        if torch.cuda.is_available():
            model = model.to(torch.device("cuda"))
            print("Modello spostato sulla GPU.")
        else:
            model = model.to(torch.device("cpu"))
            print("CUDA non disponibile, utilizzando la CPU.")

        print("Modello caricato.")
        
        print("Seleziona un file audio...")
        percorso_file = file_dialog(window)
        if not percorso_file:
            print("Nessun file selezionato.")
            return

        start_time = time.time() # serve per dare un feedback di quanto ci metta a fare la trascrizi
 
        print(f"Trascrizione del file {percorso_file} in corso...") # messaggio di feedback
        testo_trascritto = transcribe_file(percorso_file, model)
        print("Trascrizione completata.")

        end_time = time.time() #fine del timer
        elapsed_time = end_time - start_time # calcolo del tempo trascorso
        print(f"Tempo di trascrizione: {elapsed_time:.2f} secondi.") # output

        percorso_output = save_transcription(window, testo_trascritto)
        if percorso_output:
            print(f"Trascrizione salvata in '{percorso_output}'.")
            messagebox.showinfo("Completato", f"Trascrizione completata e salvata in '{percorso_output}'.")
        
    except Exception as e:
        error_message = f"Errore: {str(e)}\n{traceback.format_exc()}"
        print(error_message)
        with open("error_log.txt", "w", encoding="utf-8") as f:
            f.write(error_message)
        messagebox.showerror("Errore", f"Si è verificato un errore:\n{str(e)}\n\nDettagli salvati in 'error_log.txt'")
        input("Premi Invio per uscire...")

if __name__ == "__main__":
    main()