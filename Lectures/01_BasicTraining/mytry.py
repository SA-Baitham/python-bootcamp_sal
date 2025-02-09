
sentence = ""
while True:
    new_word = input("Enter a word: ")
    if new_word in [".", "!", "?"]:
        if len(sentence) > 0:
            sentence = sentence[:-1]
        sentence += new_word
        break
    sentence += new_word + " "
    print("...", sentence) 
print("Final :", sentence) 
