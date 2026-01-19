import csv
import os

from spotify import Track

def extract_spotify():
    file_path = os.path.join(os.path.dirname(__file__), "blues_music_data.csv")
    
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)
    

def extract_tracks():
    rows = extract_spotify()
    tracks = []

    for row in rows:
        tracks.append(Track(row))

    # print(tracks)

    return tracks
