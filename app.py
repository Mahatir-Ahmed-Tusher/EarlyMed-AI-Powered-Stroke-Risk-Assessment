import gradio as gr
import numpy as np
import pickle

# Load the trained models
with open("stroke_clf.pkl", "rb") as f:
    clf_model = pickle.load(f)

with open("stroke_reg.pkl", "rb") as f:
    reg_model = pickle.load(f)

def predict_stroke(chest_pain, shortness_breath, irregular_heartbeat, fatigue_weakness, 
                   dizziness, swelling, pain_neck_jaw, excessive_sweating, 
                   persistent_cough, nausea_vomiting, high_bp, chest_discomfort, 
                   cold_hands_feet, snoring, anxiety, age):
    """
    Prepares the input features and returns stroke risk prediction using both the classification
    and regression models.
    """
    # Convert boolean inputs to 1 (True) or 0 (False), keeping age as numeric.
    features = [
        1 if chest_pain else 0,
        1 if shortness_breath else 0,
        1 if irregular_heartbeat else 0,
        1 if fatigue_weakness else 0,
        1 if dizziness else 0,
        1 if swelling else 0,
        1 if pain_neck_jaw else 0,
        1 if excessive_sweating else 0,
        1 if persistent_cough else 0,
        1 if nausea_vomiting else 0,
        1 if high_bp else 0,
        1 if chest_discomfort else 0,
        1 if cold_hands_feet else 0,
        1 if snoring else 0,
        1 if anxiety else 0,
        age
    ]
    
    sample_input = np.array([features])
    
    # Get predictions
    classification_result = clf_model.predict(sample_input)[0]
    risk_class = "At Risk" if classification_result == 1 else "Not At Risk"
    
    regression_result = reg_model.predict(sample_input)[0]
    risk_percentage = round(regression_result, 2)
    
    return (f"**Classification Result:** {risk_class}\n"
            f"**Regression Result:** {risk_percentage}% stroke risk")

# Build Gradio Interface using Blocks for a clean, organized UI
with gr.Blocks(css=".output { white-space: pre-wrap; }") as demo:
    gr.Markdown(
    """
    # Stroke Risk Prediction
    This application uses two machine learning models to predict stroke risk:
    
    - **Classification Model:** Determines if an individual is at risk (Yes/No).
    - **Regression Model:** Estimates the stroke risk percentage.
    
    **Provide the following information based on your symptoms:**
    """
    )
    
    with gr.Row():
        with gr.Column():
            chest_pain = gr.Checkbox(label="Chest Pain")
            shortness_breath = gr.Checkbox(label="Shortness of Breath")
            irregular_heartbeat = gr.Checkbox(label="Irregular Heartbeat")
            fatigue_weakness = gr.Checkbox(label="Fatigue & Weakness")
            dizziness = gr.Checkbox(label="Dizziness")
            swelling = gr.Checkbox(label="Swelling (Edema)")
            pain_neck_jaw = gr.Checkbox(label="Pain in Neck/Jaw/Shoulder/Back")
            excessive_sweating = gr.Checkbox(label="Excessive Sweating")
        with gr.Column():
            persistent_cough = gr.Checkbox(label="Persistent Cough")
            nausea_vomiting = gr.Checkbox(label="Nausea/Vomiting")
            high_bp = gr.Checkbox(label="High Blood Pressure")
            chest_discomfort = gr.Checkbox(label="Chest Discomfort (During Activity)")
            cold_hands_feet = gr.Checkbox(label="Cold Hands/Feet")
            snoring = gr.Checkbox(label="Snoring/Sleep Apnea")
            anxiety = gr.Checkbox(label="Anxiety/Feeling of Doom")
            age = gr.Number(label="Age", value=50)
    
    predict_btn = gr.Button("Predict Stroke Risk", variant="primary")
    output = gr.Markdown(label="Prediction Results", elem_classes="output")
    
    predict_btn.click(
        predict_stroke, 
        inputs=[
            chest_pain, shortness_breath, irregular_heartbeat, fatigue_weakness,
            dizziness, swelling, pain_neck_jaw, excessive_sweating,
            persistent_cough, nausea_vomiting, high_bp, chest_discomfort,
            cold_hands_feet, snoring, anxiety, age
        ],
        outputs=output
    )
    
    gr.Markdown(
    """
    ---
    **Disclaimer:** This tool is intended for informational purposes only and should not be used as a substitute for professional medical advice.
    """
    )

demo.launch()
