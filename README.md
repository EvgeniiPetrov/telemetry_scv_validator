# telemetry_csv_validator

[Русский](README.ru.md) | **English**

`telemetry_csv_validator` is a Python utility for validating industrial telemetry data stored in CSV files.

The tool checks incoming telemetry records, separates valid and invalid rows, and writes the result into two output files:

- `clean.csv` — valid telemetry records;
- `errors.csv` — invalid records with an additional `error` column describing the validation issue.

The project is designed for data quality control before loading telemetry data into databases, ETL pipelines, or analytical storage.

---

## Input format

The input CSV file must contain the following columns:

```csv
station_id,timestamp,pressure,temperature
```

Example:

```csv
station_id,timestamp,pressure,temperature
PUMP_001,2026-07-03T10:15:00,6.4,35.2
PUMP_002,2026-07-03T10:16:00,6.5,35.3
PUMP_003,2026-07-03T10:17:00,7.0,36.1
```

---

## Validation rules

Each row is validated according to the following rules:

| Field | Rule |
|---|---|
| `station_id` | Must not be empty |
| `timestamp` | Must be a valid ISO 8601 datetime value |
| `pressure` | Must be a number from `0` to `100` |
| `temperature` | Must be a number from `-50` to `150` |

---

## Output files

### `clean.csv`

Contains only valid telemetry records.

Example:

```csv
station_id,timestamp,pressure,temperature
PUMP_001,2026-07-03T10:15:00,6.4,35.2
PUMP_002,2026-07-03T10:16:00,6.5,35.3
```

### `errors.csv`

Contains invalid records and an additional `error` column.

Example:

```csv
station_id,timestamp,pressure,temperature,error
,2026-07-03T10:16:00,6.5,35.3,station_id is empty
PUMP_002,bad_date,7.0,36.1,timestamp is invalid
PUMP_003,2026-07-03T10:18:00,150,34.0,pressure is out of range
```

---

## Use cases

`telemetry_csv_validator` can be used for:

- validating telemetry exports before database import;
- separating clean and problematic records;
- preparing data for ETL processing;
- checking data quality in industrial automation systems;
- preprocessing CSV files received from PLC, SCADA, gateways, or external telemetry sources.

---

## Project structure

Planned project structure:

```text
telemetry_csv_validator/
├── README.md
├── README.ru.md
├── LICENSE
├── src/
│   └── telemetry_csv_validator/
│       ├── __init__.py
│       ├── validators.py
│       └── processor.py
├── tests/
│   └── test_validators.py
└── data/
    ├── input.csv
    ├── clean.csv
    └── errors.csv
```

---

## Modules

| Module | Responsibility |
|---|---|
| `validators.py` | Field-level validation functions |
| `processor.py` | CSV reading, row validation, and output writing |
| `tests/` | Automated tests |

---

## Validation functions

| Function | Description |
|---|---|
| `validate_station_id` | Checks that station ID is not empty |
| `validate_timestamp` | Checks that timestamp is a valid ISO datetime value |
| `validate_pressure` | Checks that pressure is within the allowed range |
| `validate_temperature` | Checks that temperature is within the allowed range |
| `validate_row` | Validates a full telemetry row |
| `process_csv` | Processes input CSV and writes output files |

---

## Development principles

The core validation logic is based on the Python standard library.

External data-processing frameworks are not required for the first version of the project.

---

## Testing

The project uses `pytest` for automated tests.

Planned test areas:

- valid and invalid `station_id` values;
- valid and invalid ISO datetime strings;
- pressure boundary values;
- temperature boundary values;
- full row validation;
- writing valid rows to `clean.csv`;
- writing invalid rows to `errors.csv`.

---

## Roadmap

- [ ] Validate `station_id`
- [ ] Validate `timestamp`
- [ ] Validate `pressure`
- [ ] Validate `temperature`
- [ ] Validate full CSV rows
- [ ] Write valid rows to `clean.csv`
- [ ] Write invalid rows to `errors.csv`
- [ ] Add automated tests
- [ ] Add SQLite loader
- [ ] Add PostgreSQL loader
- [ ] Add basic ETL pipeline

---

## References

- Python `csv` module: https://docs.python.org/3/library/csv.html
- Python `datetime` module: https://docs.python.org/3/library/datetime.html
- Python `pathlib` module: https://docs.python.org/3/library/pathlib.html
- pytest documentation: https://docs.pytest.org/
- SQLite documentation: https://www.sqlite.org/docs.html
- PostgreSQL documentation: https://www.postgresql.org/docs/

---

## License

This project is licensed under the [MIT License](LICENSE).
