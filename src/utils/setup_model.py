import tensorflow_hub as hub
 
#use_loaded_model = hub.load("src/universal_sentence_encoder_model »)
#module_url = "src/utils/model"

# module_url ="https://tfhub.dev/google/universal-sentence-encoder/4"
# use_loaded_model = hub.load(module_url)
# print ("module %s loaded" % use_loaded_model)
#
#
# def use_embed(input_sentence):
#     """
#     Fonction créant un embedding de la question de l'utilisateur grâce à
# un Universal Sentence Encoder
#     """
#     return use_loaded_model(input_sentence


def download_model():
    model_url = "https://www.kaggle.com/models/google/universal-sentence-encoder/TensorFlow2/universal-sentence-encoder/2"

    model = hub.load(model_url)

    return model

if __name__ == '__main__':
    model = download_model()
    print("main download completed.")