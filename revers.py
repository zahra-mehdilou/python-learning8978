def reverse(word):
    l=len(word)
    new_word=""
    for i in range(l-1,-1,-1):
            new_word+=word[i]
    print(new_word)
word=str(input("Enter a word:"))
reverse(word)
