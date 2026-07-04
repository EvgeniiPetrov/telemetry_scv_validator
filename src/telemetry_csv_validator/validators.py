# uv pip install -e .
def validate_station_id(station_id: object) -> bool:

    if not isinstance(station_id, str):
        return False
    clean_station_id = station_id.strip()
    if not clean_station_id:
        return False
    return True

# print(validate_station_id(None))
