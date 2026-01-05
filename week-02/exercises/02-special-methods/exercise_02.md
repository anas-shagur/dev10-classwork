# Exercise 02

1. Create a module named `spotify.py`.

2. Add a class named `Track`.

3. Our csv file has headers:

    > Artist Name,Track Name,Popularity,Genres,Playlist,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,id,uri,track_href,analysis_url,duration_ms,time_signature

    Add attributes to `Track`:

    - artist: str
    - track: str
    - genres: list[str]
    - danceability: float
    - energy: float
    - key: int
    - tempo: float
    - id: str
    - duration_ms: int

    Our `__init__` method should either use a list or a dictionary to assign attributes.

4. Add a second function to `spotify_extractor.py` that utilizes the first function to create a `list[Track]`.

5. Create a file, `exercise_02.py`, import the second `spotify_extractor` function, and print the results.

    You'll notice that these are the results:

    ```
    <spotify.Track object at 0x1010b89b0>
    <spotify.Track object at 0x1011804b0>
    <spotify.Track object at 0x1010b89b0>
    <spotify.Track object at 0x1011804b0>
    <spotify.Track object at 0x1010b89b0>
    etc...
    ```

    We'll follow up soon.
