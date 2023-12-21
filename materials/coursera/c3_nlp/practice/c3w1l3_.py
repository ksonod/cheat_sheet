

# import wget
# wget.download("https://storage.googleapis.com/tensorflow-1-public/course3/sarcasm.json")

import json
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


with open("sarcasm.json", "r") as f:
    datastore = json.load(f)

sentences = []
labels = []
urls = []

for item in datastore:
    sentences.append(item["headline"])
    labels.append(item["is_sarcastic"])
    urls.append(item["article_link"])

tokenizer = Tokenizer(oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)

word_idx = tokenizer.word_index

print(f"number of words: {len(word_idx)}")

sequences = tokenizer.texts_to_sequences(sentences)
padded_sequences = pad_sequences(sequences, padding = "post")

print(0)