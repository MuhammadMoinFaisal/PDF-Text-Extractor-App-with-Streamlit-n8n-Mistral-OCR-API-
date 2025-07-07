import streamlit as st
import requests
import json

st.title("PDF OCR using Mistral + n8n")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    st.write("Processing...")

    # Send PDF to n8n webhook
    files = {
        "data": (uploaded_file.name, uploaded_file, "application/pdf")
    }

    try:
        # Replace with your actual n8n webhook URL
        response = requests.post("https://muhammadmoin9900.app.n8n.cloud/webhook-test/436bd44f-055b-4a20-9a5e-376549ffa8d4", files=files)

        if response.status_code == 200:
            try:
                data = json.loads(response.text)
                markdown_text = data["pages"][0]["markdown"]

                st.subheader("Extracted PDF Content")
                st.markdown(markdown_text)
            except Exception as parse_error:
                st.error(f"Failed to parse OCR result: {parse_error}")
                st.text(response.text)  # fallback
        else:
            st.error(f"Error from n8n: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Request failed: {e}")
