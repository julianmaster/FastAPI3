import re
import numpy as np


def process_sentence(sentence):
    """
    Fonction pour le preprocessing de la question de l'utilisateur
    """
    processed_sentence = re.sub(r"[^\w\s]", "", sentence).lower()
    return processed_sentence


def from_str_to_list(input_string):
    """
    Fonction pour passer la question de l'utilisateur initialement au format string en objet list
    """
    sentence_list = [input_string]
    return sentence_list


def tags(prediction):
    """
    Fonction traduisant l'output du modèle en tags qui s'affiche à l'utilisateur
    """
    prediction_array = np.array(prediction)
    list_tags = [
        ".net",
        "Other",
        "android",
        "asp.net",
        "c",
        "c#",
        "c++",
        "css",
        "database",
        "html",
        "ios",
        "iphone",
        "java",
        "javascript",
        "jquery",
        "json",
        "linux",
        "mysql",
        "node.js",
        "objective-c",
        "performance",
        "php",
        "python",
        "reactjs",
        "ruby-on-rails",
        "spring",
        "sql",
        "sql-server",
        "swift",
        "windows",
        "xcode",
    ]
    # Crée un dictionnaire pour map les indices des colonnes indices aux tags
    index_to_tag = {i: tag for i, tag in enumerate(list_tags)}
    # Extrait les valeurs "1" de la prédiction
    indices_of_ones = np.argwhere(prediction_array == 1)
    # Map les indices aux tags
    predicted_tags = [index_to_tag[index[1]] for index in indices_of_ones]
    return predicted_tags
