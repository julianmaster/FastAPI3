import json

from fastapi import FastAPI

from utils.setup_model import download_model
from utils.model_trained import model_prediction
from utils.sentence_prediction import process_sentence, from_str_to_list, tags

app = FastAPI(
    title="FastAPI3",
    description="Hello API developer!",
    version="0.1.0"
)

model = download_model()


@app.get("/")
async def main():
    return {"message": "Hello World !"}


@app.post("/predict")
async def prediction(sentence: dict):
    # Turns the json input into a string object
    string_sentence = json.dumps(sentence)

    # process_sentence needs a string objet, and use_embed needs a list object
    processed_sentence = process_sentence(string_sentence)

    # Suppression du premier mot "sentence" de la chaine de caractère
    words = processed_sentence.split(maxsplit=1)
    result_string = words[1]

    list_sentence = from_str_to_list(result_string)

    embedded_sentence = model(list_sentence)

    model_output = model_prediction(embedded_sentence)

    tags_result = tags(model_output)

    return tags_result
