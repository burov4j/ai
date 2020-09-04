def int_func(word):
    return word.capitalize()


sentence = input("Enter your sentence: ").split(" ")
for i in range(len(sentence)):
    sentence[i] = int_func(sentence[i])
print(f"{' '.join(sentence)}")
