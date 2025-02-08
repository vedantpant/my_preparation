sentence = "Hey, my name is vedant"

new_sentence = ""
i = 0
n = len(sentence)

while i < n:
    if sentence[i:].startswith("vedant"):
        new_sentence += sentence[i:].capitalize()
        break

    if i % 2 == 0:
        new_sentence += sentence[i].upper()
    else:
        new_sentence += sentence[i].lower()
    i += 1

print(new_sentence)

