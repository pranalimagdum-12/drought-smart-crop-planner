import pandas as pd
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "drought_smart_crop_data.csv"
PROFILE_FILE = BASE_DIR / "crop_profiles.json"

# Load dataset
df = pd.read_csv(DATA_FILE)

# Load crop profiles
with open(PROFILE_FILE, "r", encoding="utf-8") as f:
    crop_profiles = json.load(f)


def run_agent(question):

    # Find farm ID
    farm_match = re.search(r"F\d{4}", question.upper())

    if not farm_match:
        return "Please provide a farm ID such as F1001."

    farm_id = farm_match.group()

    # Find crop
    crop_name = None

    for crop in crop_profiles:

        if crop.lower() in question.lower():

            crop_name = crop
            break

    if crop_name is None:
        return "Please provide a crop name such as Corn."

    # Find matching row
    result = df[
        (df["Farm_ID"].astype(str) == farm_id)
        &
        (df["Crop_Selected"].str.lower() == crop_name.lower())
    ]

    if result.empty:
        return f"No assessment found for {farm_id} and {crop_name}."

    row = result.iloc[0]

    profile = crop_profiles[crop_name]

    print("\n========================================")
    print("DROUGHT-SMART CROP PLANNER")
    print("========================================")

    print(f"Farm ID              : {row['Farm_ID']}")
    print(f"Crop                 : {row['Crop_Selected']}")
    print(f"3-Month Precipitation: {row['3Mo_Precip_Forecast_mm']} mm")
    print(f"Soil Moisture       : {row['Current_Soil_Moisture_pct']}%")
    print(f"Risk                 : {row['Alert_Flag']}")
    print(f"Recommendation       : {row['Action_Recommendation']}")

    print("\nCrop Information")
    print("----------------------------------------")
    print(f"Water Requirement   : {profile['water_requirement']}")
    print(f"Drought Resistance  : {profile['drought_resistance']}")
    print(f"Alternative Crop    : {profile['alternative_crop']}")

    print("========================================\n")

    return "Analysis completed."


while True:

    question = input("\nFarmer: ")

    if question.lower() in ["exit", "quit"]:
        print("Agent stopped.")
        break

    run_agent(question)