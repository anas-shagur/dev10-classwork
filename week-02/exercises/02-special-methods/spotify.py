class Track:
    def __init__(self, data: dict):
        self.artist: str = data["Artist Name"]
        self.track: str = data["Track Name"]
        self.genres: list[str] = data["Genres"].split(",")
        self.danceability: float = float(data["danceability"])
        self.energy: float = float(data["energy"])
        self.key: int = int(data["key"])
        self.tempo: float = float(data["tempo"])
        self.id: str = data["id"]
        self.duration_ms: int = int(data["duration_ms"])

    def __str__(self):
        return f"{self.track} by {self.artist} ({self.duration_ms} ms)"
    
    def __repr__(self):
        return f"Track(track='{self.track}', artist='{self.artist} 'id='{self.id}')"

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.track < other.track
    
    