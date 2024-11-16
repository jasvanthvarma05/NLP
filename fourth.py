def pluralize_noun(noun):
    if noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"
    elif noun.endswith("y") and noun[-2] not in "aeiou":
        return noun[:-1] + "ies"
    else:
        return noun + "s"

# Test cases
nouns = ["cat", "dog", "bus", "king", "baby", "lady", "wish", "fox"]
pluralized_nouns = [pluralize_noun(noun) for noun in nouns]

for noun, plural in zip(nouns, pluralized_nouns):
    print(f"{noun} -> {plural}")
