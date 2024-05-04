import streamlit as st
import requests

# Titre
st.title("Question Tag System")

# Text input pour que l'utilisateur pose sa question
question = st.text_input("Enter your question:")

# Bouton pour appeler l'API
if st.button("Get Answer"):
    # Envoie une requête POST l'API endpoint (/predict) avec la question de l'utilisateur
    response = requests.post(
        url="http://127.0.0.1:8000/predict", json={"sentence": question}
    )
    if response.status_code == 200:
        # Extrait la réponse de l'API
        model_output = response.json()

        # Affiche l'output de l'API
        st.write("Model Output:")
        st.write(model_output)
    else:
        st.error("Failed to get response from the server. Please try again later.")

# Bouton pour appeler l'API
if st.button("Say Hello"):
    # Envoi une requête POST à l'API endpoint ("/greet")
    response = requests.post(url="http://127.0.0.1:8000/greet")

    if response.status_code == 200:
        # Affiche le message
        st.write("Greet Message:")
        st.write(response.text)
    else:
        st.error("Failed to get response from the server. Please try again later.")
# %%

# %%
