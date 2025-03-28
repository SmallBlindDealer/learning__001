from flask import Flask, request, jsonify
from phi.agent import Agent
from phi.model.groq import Groq
from nutrition import check_nutrition
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
"""
from flask import Flask, request, jsonify
from phi.agent import Agent
from phi.model.huggingface import HFModel
from nutrition import check_nutrition

app = Flask(__name__)

# Load the model from local storage
model = HFModel(model_path="./models/llama3-70b")

# Initialize the Phidata Agent
agent = Agent(
    model=model,
    instructions=[
        "Extract nutrition values (calories, protein, carbs, fat, fiber, sugar) from raw text.",
        "Summarize the remaining daily intake in a tabular format."
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)


"""
# Initialize Phidata Agent
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Extract nutrition values (calories, protein, carbs, fat, fiber, sugar) from raw text.",
        "Summarize the remaining daily intake in a json format."
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

@app.route("/check_nutrition", methods=["POST"])
def nutrition_advice():
    """API endpoint to check remaining nutrition based on raw text input."""
    raw_text = request.json.get("text", "")

    if not raw_text:
        return jsonify({"error": "Invalid input, provide nutrition data in text format"}), 400

    # Extract nutrition data using AI
    extracted_nutrition = agent.run(f"Extract nutrition values from: {raw_text}")
    print("->>--->")
    print(extracted_nutrition.content)
    print("\n"*5)
    print(extracted_nutrition)

    # Convert AI output to dictionary
    try:
        # user_nutrition = eval(extracted_nutrition)  # AI returns a dict-like string
        return jsonify({"data": "extracted_nutrition"}), 200

    except Exception as e:
        return jsonify({"error": f"Failed to process input: {str(e)}"}), 500

    # Calculate remaining nutrition
    nutrition_table = check_nutrition(user_nutrition)

    return jsonify({"nutrition_summary": nutrition_table})

if __name__ == "__main__":
    app.run(debug=True)


#  huggingface-cli download --resume-download meta-llama/Meta-Llama-3.3-70B-Versatile --local-dir ./models/llama3-70b