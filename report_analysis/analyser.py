import csv

medical_tests = {}

with open("data/medical_ranges.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        medical_tests[row["test"]] = {
            "range": (float(row["low"]), float(row["high"])),
            "description": row["description"],
            "low": row["low_msg"],
            "high": row["high_msg"]
        }


   

