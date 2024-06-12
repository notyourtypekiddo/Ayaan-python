word_s = str(input("Enter a word: "))
word_a = str(input("Enter a word: "))
alphabet_s = "Aa"
you = 0
for i in word_s:
        if i in alphabet_s:
                you = 1 + you
for i in word_a:
        if i in alphabet_s:
                you = 1 + you
print(you)

        
        
  
       
   