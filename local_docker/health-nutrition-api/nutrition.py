import yaml
import pandas as pd

# Load reference nutrition intake
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

NUTRITION_REFERENCE = config["nutrition_reference"]

def check_nutrition(user_input):
    """Compares user intake with recommended intake and returns remaining nutrition."""
    remaining_nutrition = {
        nutrient: max(0, NUTRITION_REFERENCE[nutrient] - user_input.get(nutrient, 0))
        for nutrient in NUTRITION_REFERENCE
    }

    # Convert to DataFrame for tabular format
    df = pd.DataFrame.from_dict(remaining_nutrition, orient="index", columns=["Remaining Intake"])
    return df.to_markdown()
