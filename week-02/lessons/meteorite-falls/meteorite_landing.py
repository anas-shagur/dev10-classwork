from dataclasses import dataclass, field


@dataclass
class MeteoriteLanding:
    name: str
    id: int
    name_type: str
    rec_class: str
    mass: float = field(metadata={"units": "grams"})
    fall: str
    year: int
    latitude: float = field(metadata={"units": "decimal degrees"})
    longitude: float = field(metadata={"units": "decimal degrees"})
