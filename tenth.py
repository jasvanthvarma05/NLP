
corpus = [
    ["I", "want", "to", "book", "a", "flight"],
    ["the", "book", "is", "on", "the", "table"]
]

rules = {
    ("to", "book"): "VERB"
}

def apply_rules(sentence):
    return [
        ("VERB" if i > 0 and (sentence[i-1], word) in rules else "NOUN", word)
        for i, word in enumerate(sentence)
    ]

transformed_corpus = [apply_rules(sentence) for sentence in corpus]
for sentence in transformed_corpus:
    print(sentence)