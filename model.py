from transformers import pipeline

# 🔹 Load BERT model (explicit for clarity)
bert_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# 🔹 Simulated BiLSTM (sequence-based scoring)
def bilstm_model(data):
    """
    Simulates sequence pattern learning.
    Returns normalized score (0 to 1)
    """
    if len(data) == 0:
        return 0

    score = sum(data) / len(data)
    return score


# 🔹 Convert answers into text for BERT
def prepare_text(data):
    """
    Convert numerical answers into meaningful text
    """
    text = []

    for value in data:
        if value == 1:
            text.append("stress")
        else:
            text.append("calm")

    return " ".join(text)


# 🔹 Classification logic
def classify_level(score):
    """
    Classify overthinking level based on score
    """
    if score >= 0.7:
        return "High Overthinking"
    elif score >= 0.4:
        return "Moderate Overthinking"
    else:
        return "Low Overthinking"


# 🔹 Main Prediction Function
def predict_overthinking(data):
    """
    Hybrid AI model:
    - BERT → emotional context
    - BiLSTM (simulated) → pattern scoring
    """

    # Step 1: Prepare text for BERT
    text_input = prepare_text(data)

    # Step 2: BERT Analysis
    bert_result = bert_model(text_input)[0]
    bert_label = bert_result['label']
    bert_score = bert_result['score']

    # Step 3: BiLSTM Pattern Analysis
    bilstm_score = bilstm_model(data)

    # Step 4: Combine Scores
    combined_score = (bilstm_score * 0.7) + (bert_score * 0.3)

    # Step 5: Final Classification
    level = classify_level(combined_score)

    # Step 6: Generate Explanation
    explanation = generate_explanation(level, bert_label)

    return level, explanation


# 🔹 Explanation Generator
def generate_explanation(level, bert_label):
    """
    Generate meaningful output for UI
    """

    if level == "High Overthinking":
        return f"High stress patterns detected ({bert_label}). Consider relaxation techniques."

    elif level == "Moderate Overthinking":
        return f"Moderate thinking patterns observed ({bert_label}). Try mindfulness practices."

    else:
        return f"Low overthinking detected ({bert_label}). Maintain your mental balance."


# 🔹 Optional: Test function (for debugging)
if __name__ == "__main__":
    sample_data = [1, 0, 1, 1, 0, 1]
    result = predict_overthinking(sample_data)
    print(result)