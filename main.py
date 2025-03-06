import requests
import time

CARRIS_API = "https://api.carrismetropolitana.pt/v1/"

def get_carris_arrivals(stop_id):
    """Gets arrivals per each stop"""
    response = requests.get(f"{CARRIS_API}stops/{stop_id}/realtime")

    if response.status_code != 200:
        print(f"Erro: {response.status_code}")
        return None

    arrivals_data = response.json()

    #current_time = int(time.time())
    current_time = 1741156249

    time_interval_before = current_time - 1800 # 30 minutes before
    time_interval_after = current_time + 1800 # 30 minutes after

    arrivals_filtered = []
    for arrival in arrivals_data:
        estimated_time = arrival.get('estimated_arrival_unix')

        if estimated_time is not None:
            if time_interval_before <= estimated_time <= time_interval_after:
                arrivals_filtered.append(arrival)

    return arrivals_filtered

print(get_carris_arrivals("070383"))



