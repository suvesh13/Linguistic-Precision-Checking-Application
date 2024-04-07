import re
import string 
from collections import Counter
import numpy as np


def read_text(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
        words = []

        for line in lines:
            words += re.findall(r'\w+',line.lower())
    return words
    
words = read_text('C:/Users/VANSHIKA/Downloads/spellfolder/big.txt')
print(f"No of words {len(words)}")

vocabs = set(words)
print(f"Unique Wordss {len(vocabs)}")

word_count = Counter(words)
#print(word_count)

total_word_count = float(sum(word_count.values()))
word_probs = {word: word_count[word]/total_word_count for word in word_count.keys()}

#print(word_probs["sherlock"],word_probs["tea"])

def split(word):
    return[(word[:i], word[i:]) for i in range(len(word)+1)]
#print(split("trash"))

def delete(word):
    return[ l+r[1:] for l,r in split(word) if r]
#print(delete("trash"))

def swap(word):
    return [ l+r[1]+r[0]+r[2:] for l,r in split(word) if len(r)>1 ]
#print(swap('trash'))

def replace(word):
    letters = string.ascii_lowercase
    return [l+c+r[1:] for l,r in split(word) if r for c in letters]
#print(replace("trash"))

def insert(word):
    letters = string.ascii_lowercase
    return [l+c+r for l,r in split(word) for c in letters]
#print(replace("trash"))

def level_one_edits(word):
    return set(delete(word)+ swap(word)+replace(word)+insert(word))

def level_two_edits(word):
    return set(e2 for e1 in level_one_edits(word) for e2 in level_one_edits(e1))

def correct_spelling(word,vocabulary,word_probabilities):
    if(word in vocabulary):
        #print(word+" ")
        return
    sugg = level_one_edits(word) or level_two_edits(word) or [word]
    best = [w for w in sugg if w in vocabulary]
    return [(w,word_probabilities[w]) for w  in best]

# str = input()
# ls = re.findall(r'\w+', str.lower())
# print(ls)
# for i in ls:
#     guesses = correct_spelling(i,vocabs,word_probs)
#     if guesses is None:
#         print(i,end=" ")
#     else:
#         print(guesses)
def spellcheck(sentence):
    words = re.findall(r'\w+', sentence.lower())
    corrected_sentence = []

    for word in words:
        guesses = correct_spelling(word, vocabs, word_probs)
        if guesses is None:
            pass
            #corrected_sentence.append(word)  # Append the word itself if it's correct
        else:
            corrected_sentence.append(f"[{word}]-")  # Highlight the potentially misspelled word
            correction_suggestions = ', '.join(str(guess[0]) for guess in guesses)  # Convert each suggestion to string
            corrected_sentence.append("{"+correction_suggestions+"}")  # Suggest corrections

    return ' '.join(corrected_sentence)

# sentence = input("Enter a sentence: ")
# corrected_sentence = spellcheck(sentence)
# print(corrected_sentence)

