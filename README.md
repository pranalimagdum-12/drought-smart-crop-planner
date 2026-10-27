# 🌾 Drought-Smart Crop Planner

A Python-based agricultural decision-support prototype that helps farmers evaluate crop suitability using precipitation forecasts, soil moisture levels, and crop drought-resistance information.

## 📌 Project Overview

Unpredictable rainfall and changing soil moisture conditions can make crop selection difficult for farmers. Planting crops with high water requirements during dry conditions may increase agricultural risk.

The **Drought-Smart Crop Planner** uses farm-level data and crop profiles to display risk alerts and crop recommendations. It helps users understand the available assessment and explore alternative crops with better drought resistance.

## 🎯 Objectives

- Retrieve farm-specific agricultural data using a Farm ID.
- Display three-month precipitation forecasts and current soil moisture values.
- Show the risk alert and recommended action recorded in the dataset.
- Provide crop information, including water requirements and drought resistance.
- Suggest alternative crops based on the supplied crop profiles.

## 🛠️ Technologies Used

- **Python** — application logic
- **Pandas** — loading and filtering farm data
- **JSON** — storing crop profiles
- **Regular Expressions (`re`)** — extracting Farm IDs from user queries
- **Pathlib** — locating project files

## 📂 Project Structure

```text
drought-smart-crop-planner/
│
├── demo_agent.py
├── drought_smart_crop_data.csv
├── crop_profiles.json
└── README.md
```

## ⚙️ How It Works

1. The application loads farm records from a CSV file using Pandas.
2. It loads crop characteristics from `crop_profiles.json`.
3. The user enters a query containing a Farm ID and crop name.
4. The application identifies the requested farm and crop.
5. It retrieves the matching farm record and crop profile.
6. It displays precipitation, soil moisture, risk status, the existing recommendation, and crop characteristics.

The current prototype retrieves the risk alert and action recommendation from the supplied dataset. It does not independently calculate a new risk score.

## 🌱 Example

**Sample query:**

```text
What is the assessment for Sorghum at farm F1010?
```

**Example output:**

```text
Farm ID              : F1010
Crop                 : Sorghum
3-Month Precipitation: 100 mm
Soil Moisture        : 18%
Risk                 : Safe to Plant
Recommendation       : Minimal Watering Required

Crop Information
Water Requirement    : Low
Drought Resistance   : High
Alternative Crop     : Millet
```

*The values above are illustrative output from the supplied dataset.*

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or later
- Pandas

### 1. Clone the repository

Replace `YOUR-USERNAME` with your GitHub username.

```bash
git clone https://github.com/pranalimagdum-12/drought-smart-crop-planner
```

### 2. Navigate to the project directory

```bash
cd drought-smart-crop-planner
```

### 3. Install the dependency

```bash
python -m pip install pandas
```

### 4. Run the application

```bash
python demo_agent.py
```

### 5. Ask a question

Enter a query containing a valid Farm ID and crop name, for example:

```text
What is the assessment for Corn at farm F1001?
```

To exit the application, enter:

```text
exit
```

## 📊 Data Sources

The current prototype uses the CSV dataset and JSON crop profiles supplied for the project.

The farm data includes:

- Farm ID
- Selected crop
- Three-month precipitation forecast in millimetres
- Current soil moisture percentage
- Risk alert
- Recommended action

The crop profiles contain water requirements, drought-resistance levels, and alternative crop suggestions.

**Data limitation:** The current prototype uses supplied dataset values. It does not fetch live weather information from Open-Meteo or NASA POWER, and the sample dataset should not be treated as verified real-world agricultural data.

## 🔮 Future Enhancements

- Integrate a weather API such as Open-Meteo to retrieve weather information for a specified location.
- Calculate risk using transparent rules based on precipitation, soil moisture, and crop characteristics.
- Add an LLM-powered conversational interface.
- Validate crop recommendations against regional agricultural guidance.
- Improve input validation and error handling.
- Develop a simple web interface for farmers.

## 🎓 Learning Outcomes

Through this project, I practised:

- Reading and filtering CSV data with Pandas.
- Working with structured JSON data.
- Building a query-based Python application.
- Combining farm records with crop profiles.
- Presenting data-driven agricultural recommendations.
- Structuring a small, practical decision-support prototype.

## ⚠️ Disclaimer

This project is an educational prototype, not a substitute for professional agricultural advice. Actual planting decisions should consider local soil conditions, regional forecasts, crop varieties, irrigation availability, and guidance from agricultural experts.

## 👩‍💻 Author

**Pranali Anil Magdum**
