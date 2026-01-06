def reverse(word):
    l=len(word)
    new_word=""
    for i in range(l-1,-1,-1):
            new_word+=word[i]
    return(new_word)
word=str(input("Enter a word:"))
a=reverse(word)
print(a)