from dataclasses import dataclass, field

@dataclass
class Player:
    player_name: str
    club: str
    nationality: str
    height_cm: int
    avg_goals_per_game: float
    id: int = field(default=None)