from transformers import pipeline

# Load BERT model
bert_model = pipeline("sentiment-analysis")

# Simulated BiLSTM
def bilstm_model(data):
    return sum(data) / len(data)

def predict_overthinking(data):
    text_input = " ".join(["stress" if x == 1 else "calm" for x in data])

    bert_result = bert_model(text_input)[0]
    bilstm_score = bilstm_model(data)

    final_score = bilstm_score * 5

    if final_score >= 4:
        level = "High Overthinking"
    elif final_score >= 2:
        level = "Moderate Overthinking"
    else:
        level = "Low Overthinking"

    return level, bert_result['label']