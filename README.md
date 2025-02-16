# LLM-Jailbreak-Detector  

A machine learning-based tool to identify potential jailbreak attempts in prompts given to large language models (LLMs). This helps in detecting and preventing malicious or manipulative queries that attempt to bypass safety mechanisms in AI models.  

## Features  

- Pretrained model for detecting jailbreak prompts  
- Simple API interface for real-time detection  
- Dataset created from real-world jailbreak and non-jailbreak prompts  
- Fully open-source and community-driven  

## How It Works  

1. The dataset (`dataset.csv`) contains labeled prompts (safe vs. jailbreak).  
2. The model (`jailbreak_detector.pkl`) is trained using natural language processing (NLP) techniques.  
3. `app.py` provides an interface to classify input prompts in real time.  
4. Use `train_model.py` to retrain the model with new data.  

## Installation  

Clone the repository and install dependencies:  

```bash
git clone https://github.com/RitamPatra76/LLM-Jailbreak-detector.git
cd LLM-Jailbreak-detector
pip install -r requirements.txt
```

## Usage  

To run the detection system:  

```bash
python app.py
```

To retrain the model with new data:  

```bash
python train_model.py
```

## Demo Video  

[Click here to see the demo video](#) *(Replace # with the actual video link)*  

## Contributing  

Feel free to contribute by submitting pull requests or reporting issues.
