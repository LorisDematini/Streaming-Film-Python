import tkinter as tk
from tkinter import messagebox
import requests
import json
import webbrowser

def open_video():
    nameFilm = entry.get()
    if not nameFilm:
        messagebox.showwarning("Erreur", "Veuillez entrer le nom d'un film.")
        return

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkZDIxYzJkZjE1ZmEzZjFjODY2MzhmNzhkMTc3NWVmMCIsInN1YiI6IjYzMzY5YmU1Y2JhMzZmMDA5YTQxOTE3YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.RI7HArwasRdK7Db92106s4Th6dq-SeI0rn73vN5Olgw"
    }

    urlFilm = "https://api.themoviedb.org/3/search/movie?query=" + nameFilm
    filmResponse = requests.get(urlFilm, headers=headers)

    parsedData = json.loads(filmResponse.text)
    if not parsedData.get('results'):
        messagebox.showerror("Erreur", "Aucun film trouvé.")
        return

    firstId = parsedData['results'][0]['id']
    urlVideo = "https://vidsrc.cc/embed/movie/" + str(firstId)
    webbrowser.open(urlVideo)

# Créer la fenêtre Tkinter
root = tk.Tk()
root.title("Chercher un film")
root.geometry("400x200")

# Ajouter un label et un champ de saisie
label = tk.Label(root, text="Entrez le nom du film voulu:", font=("Times", 20))
label.pack(pady=20)

entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)

# Ajouter un bouton pour déclencher la recherche
button = tk.Button(root, text="Rechercher", command=open_video, font=("Arial", 12))
button.pack(pady=20)

# Lancer la boucle principale
root.mainloop()