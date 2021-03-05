from pathlib import Path

import yaml


DATA = []


def read_data():
    """Read the files."""
    for file in sorted(Path(__file__).parent.glob("*.yaml")):
        DATA.append(yaml.safe_load(open(file)))


def get_classifiers(record, prefix):
    result = []

    for c in record.get("classifiers", []):
        parts = c.split(f"{prefix} :: ", maxsplit=1)
        if len(parts) > 1:
            result.append(parts[-1])

    return ", ".join(result)


if __name__ == "__main__":
    read_data()

    # Example: construct a table like the "Index" sheet of the spreadsheet
    for m in DATA:
        print(f"{m['id']:4} {m['name']}")

        # Extract information from each record
        for prefix in ["Mode", "Type", "Scope"]:
            print("     - " + get_classifiers(m, prefix))
