import streamlit as st
import pickle

with open("jailbreak_detector.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit UI
st.title("🚨 LLM Jailbreak Detector")
st.write("Enter a prompt to check if it's **safe** or a **jailbreak attempt**.")

user_input = st.text_area("Enter Prompt Here:", "")

if st.button("Check Prompt"):
    if user_input:
        prediction = model.predict([user_input])[0]
        if prediction == "safe":
            st.success("✅ This is a **safe** prompt.")
        else:
            st.error("⚠️ This is a **jailbreak attempt!**")
    else:
        st.warning("Please enter a prompt first.")
