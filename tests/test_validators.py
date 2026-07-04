# uv pip install -e .
import pytest
from telemetry_csv_validator.validators import validate_station_id

@pytest.mark.parametrize(
    'value, expected',
    [
     (" a ", True),
     ("a", True),
     (" 1 ", True),
     ("1", True),
     (1, False),
     (None, False),
     ("  ", False),
     ("", False),
     ],
)
def test_validate_station_id_returns_expected_result(value, expected) -> None:
    assert validate_station_id(value) is expected
