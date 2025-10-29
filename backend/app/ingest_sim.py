# ingest_sim.py - Nagpur-only simulation positions
import random, time, json

# Nagpur coordinates (lat, lon) - Sitabuldi / Civil Lines area and surroundings
nagpur_coords = [
    (21.1498, 79.0806),  # Sitabuldi - City Center
    (21.1458, 79.0897),  # Dharampeth
    (21.1389, 79.0730),  # Civil Lines
    (21.1611, 79.0712),  # Sadar
    (21.1460, 79.1042),  # Itwari
    (21.1333, 79.1075),  # Gandhibagh
    (21.1770, 79.0617),  # Seminary Hills
    (21.1286, 79.0803),  # Mahal
    (21.1308, 79.0639),  # Mankapur
    (21.1635, 79.0942),  # Koradi Road
    (21.1089, 79.0894),  # Wardhaman Nagar
    (21.1201, 79.0669),  # Ajni
]

CITIES = {
    "nagpur": nagpur_coords,
}

def random_bus_position():
    # pick a random coordinate and jitter slightly to simulate movement
    lat, lon = random.choice(nagpur_coords)
    lat += random.uniform(-0.003, 0.003)
    lon += random.uniform(-0.003, 0.003)
    return {"lat": round(lat, 6), "lon": round(lon, 6)}

if __name__ == "__main__":
    # simple CLI simulation that emits JSON position every 0.5s (used for testing)
    try:
        while True:
            pos = random_bus_position()
            print(json.dumps(pos))
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
