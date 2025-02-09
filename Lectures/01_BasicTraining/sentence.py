sentence = ""
while True:
    word = input("Enter a word: ")
    if word in ['.', '!', '?']:
        break
    sentence += word + " "
    print ("The sentence is:", sentence)
