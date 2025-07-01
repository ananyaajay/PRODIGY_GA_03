import random

def build_markov_chain(text):
    words = text.split()
    markov_chain = {}

    for current_word, next_word in zip(words[:-1], words[1:]):
        if current_word not in markov_chain:
            markov_chain[current_word] = []
        markov_chain[current_word].append(next_word)
    return markov_chain

def generate_text(chain, start_word, length=20):
    word = start_word
    result = [word]

    for _ in range(length - 1):
        next_words = chain.get(word)
        if not next_words:
            break
        word = random.choice(next_words)
        result.append(word)

    return ' '.join(result)

text = "the cat sat on the mat the cat lay on the rug"
chain = build_markov_chain(text)
generated = generate_text(chain, start_word="the", length=15)

print(generated)
