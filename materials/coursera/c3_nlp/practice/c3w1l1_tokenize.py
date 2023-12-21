"""
Tokenizer Basics
- https://github.com/https-deeplearning-ai/tensorflow-1-public/blob/main/C3/W1/ungraded_labs/C3_W1_Lab_1_tokenize_basic.ipynb
"""

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = [
    "i love my dog",
    "I, love my cat",
    "Do you love my cat"
]

tokenizer = Tokenizer(
    num_words=100,
    oov_token="<OOV>"
)
tokenizer.fit_on_texts(sentences)

word_idx = tokenizer.word_index

print(word_idx)


test_sentences = [
    "Do you love my dog and cat",
    "My cat love my dog"
]
sequences = tokenizer.texts_to_sequences(test_sentences)
print(sequences)

padded_sequences = pad_sequences(
    sequences,
    padding="post",
    # maxlen=5
)
print(padded_sequences)
