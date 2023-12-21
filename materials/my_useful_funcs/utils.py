import csv
import numpy as np
from typing import List
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer


##### GENERAL PURPOSES
def show_data_type_and_shape(X):
    print("--Info.--")
    print(f"shape: {X.shape}")
    print(f"dtype: {X.dtype}")


##### NLP PURPOSES
def parse_data_from_file(filename):
    """
    https://github.com/williamcwi/DeepLearning.AI-TensorFlow-Developer-Professional-Certificate/blob/master/3.%20Natural%20Language%20Processing%20in%20TensorFlow/3.%20Sequence%20Models/assignment/C3W3_Assignment.ipynb
    See also parse_data_from_file_without_stopwords

    :param filename: csv file
    """

    sentences = []
    labels = []

    with open(filename, 'r') as csvfile:
        ### START CODE HERE
        reader = csv.reader(csvfile, delimiter=',')

        for row in reader:
            labels.append(0 if row[0] == 0 else 1)
            sentences.append(row[5])

        ### END CODE HERE

    return sentences, labels


def remove_stopwords(sentence):
    """
    Removes a list of stopwords

    Args:
        sentence (string): sentence to remove the stopwords from

    Returns:
        sentence (string): lowercase sentence without the stopwords
    """
    # List of stopwords
    stopwords = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at",
                 "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did",
                 "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have",
                 "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself",
                 "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's",
                 "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only",
                 "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd",
                 "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs",
                 "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're",
                 "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we",
                 "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's",
                 "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll",
                 "you're", "you've", "your", "yours", "yourself", "yourselves"]

    # Sentence converted to lowercase-only
    sentence = sentence.lower()

    words = sentence.split()
    results_words = [word for word in words if word not in stopwords]
    sentence = ' '.join(results_words)

    return sentence


def parse_data_from_file_without_stopwords(filename):
    """
    Extracts sentences and labels from a CSV file without stopwords.
    See also parse_data_from_file function

    Args:
        filename (string): path to the CSV file

    Returns:
        sentences, labels (list of string, list of string): tuple containing lists of sentences and labels
    """
    sentences = []
    labels = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        # Skip header
        next(reader, None)

        for row in reader:
            labels.append(remove_stopwords(row[0]))
            sentences.append(remove_stopwords(row[1]))
    return sentences, labels


def create_training_data_and_labels_for_textgeneration(tokenizer, corpus: List):
    """
    :param tokenizer: Tokenizer object
    :param corpus: List of lines
    :return:
    """

    total_words = len(tokenizer.word_index) + 1

    # Initialize the sequences list
    input_sequences = []

    # Loop over every line
    for line in corpus:

        # Tokenize the current line
        token_list = tokenizer.texts_to_sequences([line])[0]

        # Loop over the line several times to generate the subphrases
        for i in range(1, len(token_list)):
            # Generate the subphrase
            n_gram_sequence = token_list[:i + 1]

            # Append the subphrase to the sequences list
            input_sequences.append(n_gram_sequence)

    # Get the length of the longest line
    max_sequence_len = max([len(x) for x in input_sequences])

    # Pad all sequences
    input_sequences = pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre')

    # Create inputs and label by splitting the last token in the subphrases
    xs, labels = input_sequences[:, :-1], input_sequences[:, -1]

    # Convert the label into one-hot arrays
    ys = tf.keras.utils.to_categorical(labels, num_classes=total_words)

    return xs, ys


def generate_text_using_trained_model(seed_text, tokenizer, model, max_sequence_len, randomize_choice=False):
    """
    :param seed_text: example -> seed_text = "help me obi-wan kinobi youre my only hope"
    :param tokenizer: Tokenizer object
    :param model: trained model
    max_sequence_len: see max([len(x) for x in input_sequences]) in create_training_data_and_labels_for_textgeneration
    :return: predicted texts
    """

    # Define total words to predict
    next_words = 100

    # Loop until desired length is reached

    for _ in range(next_words):

        # Convert the seed text to a token sequence
        token_list = tokenizer.texts_to_sequences([seed_text])[0]

        # Pad the sequence
        token_list = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')

        # Feed to the model and get the probabilities for each index
        probabilities = model.predict(token_list, verbose=0)


        if randomize_choice:
            # Pick a random number from [1,2,3]
            choice = np.random.choice([1, 2, 3])

            # Sort the probabilities in ascending order
            # and get the random choice from the end of the array
            predicted = np.argsort(probabilities)[0][-choice]
        else:
            # Get the index with the highest probability
            predicted = np.argmax(probabilities, axis=-1)[0]

        # Ignore if index is 0 because that is just the padding.
        if predicted != 0:
            # Look up the word associated with the index.
            output_word = tokenizer.index_word[predicted]

            # Combine with the seed text
            seed_text += " " + output_word

    return seed_text


def make_ngram_sequence_and_padding(corpus, tokenizer):
    """
    .
    """


    # Initialize the sequences list
    input_sequences = []

    # Loop over every line
    for line in corpus:

        # Tokenize the current line
        token_list = tokenizer.texts_to_sequences([line])[0]

        # Loop over the line several times to generate the subphrases
        for i in range(1, len(token_list)):
            # Generate the subphrase
            n_gram_sequence = token_list[:i + 1]

            # Append the subphrase to the sequences list
            input_sequences.append(n_gram_sequence)

    # Get the length of the longest line
    max_sequence_len = max([len(x) for x in input_sequences])

    # Pad all sequences
    input_sequences = pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre')



##### TIME SERIES DATA


# window_size = 20
# batch_size = 32
# shuffle_buffer_size = 1000
def windowed_dataset(series, window_size=64, batch_size=32, shuffle_buffer=1000):
    """Generates dataset windows

    Args:
      series (array of float) - contains the values of the time series
      window_size (int) - the number of time steps to average
      batch_size (int) - the batch size
      shuffle_buffer(int) - buffer size to use for the shuffle method

    Returns:
      dataset (TF Dataset) - TF Dataset containing time windows
    """

    series = tf.expand_dims(series, axis=-1)  # Added by myself

    # Generate a TF Dataset from the series values
    dataset = tf.data.Dataset.from_tensor_slices(series)

    # Window the data but only take those with the specified size
    dataset = dataset.window(window_size + 1, shift=1, drop_remainder=True)

    # Flatten the windows by putting its elements in a single batch
    dataset = dataset.flat_map(lambda window: window.batch(window_size + 1))

    # Create tuples with features and labels
    dataset = dataset.map(lambda window: (window[:-1], window[-1]))

    # Shuffle the windows
    dataset = dataset.shuffle(shuffle_buffer)

    # Create batches of windows
    dataset = dataset.batch(batch_size).prefetch(1)

    return dataset