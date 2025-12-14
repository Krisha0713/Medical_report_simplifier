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

medical_tests = {
    "hemoglobin": {
        "description": "Hemoglobin carries oxygen in the blood.",
        "range": (12, 16),
        "low": "Low hemoglobin may indicate anemia.",
        "high": "High hemoglobin may indicate dehydration."
    },
    "glucose": {
        "description": "Glucose level indicates blood sugar.",
        "range": (70, 140),
        "low": "Low glucose may cause hypoglycemia.",
        "high": "High glucose may indicate diabetes."
    }
}

