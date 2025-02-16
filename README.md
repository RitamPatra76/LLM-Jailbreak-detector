# LLM Jailbreak Detector  

## Overview  
Language models are powerful, but they can be manipulated to generate harmful or unintended responses through jailbreak attempts. This project helps detect such attempts before they reach an AI system, ensuring responsible and ethical AI usage.  

With a simple Streamlit UI, you can enter a prompt and instantly check whether it's safe or a jailbreak attempt.  

## How It Works  
- Text Preprocessing: The input prompt is cleaned and standardized.  
- Feature Extraction: TF-IDF vectorization is applied for efficient text representation.  
- Classification: A Naïve Bayes model identifies whether the prompt is safe or a jailbreak attempt.  
- Real-Time Detection: The trained model runs in a simple web app, giving instant feedback.  

## Try It Out  
1. Clone this repository:  
   ```bash
   git clone https://github.com/RitamPatra76/LLM-Jailbreak-detector.git
   cd LLM-Jailbreak-detector
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:  
   ```bash
   streamlit run app.py
   ```  

## Why This Matters  
AI safety is crucial. If we want AI to be reliable and trustworthy, we need safeguards against manipulation. This tool is a step toward responsible AI by identifying harmful prompts before they reach an AI model.  

### Contributions & Feedback  
This is an open-source project—contributions and feedback are welcome. Let’s work together to build safer AI.  

Would love to hear your thoughts! What more can we do to make AI safety stronger? Let’s discuss.
