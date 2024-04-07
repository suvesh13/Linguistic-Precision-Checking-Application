import pickle
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import numpy as np


with open('train1.pkl', 'rb') as f:
    model_architecture = pickle.load(f)

# Reconstruct model from architecture
model = model_from_json(model_architecture)

with open('train1_tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# Load model weights
model.load_weights('train1_weights.pkl')



#seed_text = input("Enter something")
next_words = 1
max_sequence_len = 40

def generate_next_words(seed_text, next_words):
    for _ in range(next_words):
        # Tokenize the seed text
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        # Pad the token list
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        # Predict the next word index
        predicted = np.argmax(model.predict(token_list), axis=-1)
        output_word = ""
        # Convert the predicted index to word
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        # Update the seed text with the predicted word
        seed_text += " " + output_word
        print(output_word)
    return seed_text

#generated_text = generate_next_words(seed_text, next_words)
#print(generated_text)