import pickle

filename = "utils/finalized_model.sav"
loaded_model = pickle.load(open(filename, "rb"))


def model_prediction(processed_input):
    """
    Fonction pour prédire les tags relatifs à la question de l'utilisateur
    """
    model_output = loaded_model.predict(processed_input)
    return model_output
