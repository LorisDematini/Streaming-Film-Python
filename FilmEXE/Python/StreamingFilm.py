import requests
import json
import webbrowser

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkZDIxYzJkZjE1ZmEzZjFjODY2MzhmNzhkMTc3NWVmMCIsInN1YiI6IjYzMzY5YmU1Y2JhMzZmMDA5YTQxOTE3YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.RI7HArwasRdK7Db92106s4Th6dq-SeI0rn73vN5Olgw"
}

nameFilm = input("Tapez le nom du film (le plus précisement possible) : ")
urlFilm = "https://api.themoviedb.org/3/search/movie?query="+nameFilm
filmResponse = requests.get(urlFilm, headers=headers)

parsedData = json.loads(filmResponse.text)
firstId = parsedData['results'][0]['id']

print("Le premier id est :", firstId)

urlVideo = "https://vidsrc.cc/embed/movie/"+str(firstId)
webbrowser.open(urlVideo)