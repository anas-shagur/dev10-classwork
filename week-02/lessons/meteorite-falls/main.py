import statistics as stats
import os
from extractor import extract


def is_na(value):
    return value is None or len(value) == 0


def map_lat_long(ml):
    ml.latitude = float(ml.latitude)
    ml.longitude = float(ml.longitude)
    return ml


meteorite_csv_path = os.path.join(os.path.dirname(__file__), "Meteorite_Landings.csv")


def main():
    meteorite_landings = extract(meteorite_csv_path)
    print(f"All records: {len(meteorite_landings)}")

    geolocation_meteorites = [
        map_lat_long(ml)
        for ml in meteorite_landings
        if not (is_na(ml.latitude) and is_na(ml.longitude))
    ]
    print(f"Geolocation records: {len(geolocation_meteorites)}")

    masses = [float(ml.mass) for ml in geolocation_meteorites if not is_na(ml.mass)]
    print(f"Valid masses: {len(masses)}")

    print(f"Mass mean: {stats.mean(masses)}")
    print(f"Mass median: {stats.median(masses)}")
    print(f"Mass mode: {stats.mode(masses)}")
    print(f"Mass variance: {stats.variance(masses)}")
    print(f"Mass standard deviation: {stats.stdev(masses)}")


if __name__ == "__main__":
    main()
