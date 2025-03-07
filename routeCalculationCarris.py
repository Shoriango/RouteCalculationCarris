import requests
import time

CARRIS_API = "https://api.carrismetropolitana.pt/v1/"


def get_carris_arrivals(stop_id):
    """Gets arrivals for a given stop and filters only those within the past 30 minutes and next 30 minutes."""

    response = requests.get(f"{CARRIS_API}stops/{stop_id}/realtime")

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return None

    arrivals = response.json()

    current_time = int(time.time())

    time_before = current_time - 1800  # 30 minutes ago
    time_after = current_time + 1800  # 30 minutes ahead

    filtered_arrivals = [
        arrival for arrival in arrivals
        if arrival.get('observed_arrival_unix') and time_before <= arrival[
            'observed_arrival_unix'] <= time_after
    ]

    return filtered_arrivals

print(get_carris_arrivals('070383'))