# This was just to find number of scripts in extracted_data_tedex.json, u can ignore it, its not necessary
# You can run this script with python .\ignore\find_length_of_file.py to verify if needed, add to list in future
# 26-05-2025 : Total talks processed: 3995

import json
from pathlib import Path


def count_objects(json_path):
    print(f"Loading: {json_path.resolve()}")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"Total talks processed: {len(data)}")


if __name__ == "__main__":
    from pathlib import Path

    project_root = Path(__file__).resolve().parents[1]
    data_path = project_root / "extracted_data_tedex.json"
    count_objects(data_path)
