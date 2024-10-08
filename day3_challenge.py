#Victoria Nowak, Angela Macias, Kaleb svenningsen, Oscar Colotl-Garista, Nathan Dennis 

#step 1: Ask the user for a piece of text
text= input("Please enter a text: ")
print(text)

#step 2: Ask the user for 3 random letters
letter1= input("enter a letter of your choice: ")
letter2= input("enter another letter: ")
letter3 = input("enter one last random letter:  ")

#step 3: Count how many times the 3 random letters appear in the text?
occurance1 = letter1.count(letter1)
occurance2 = letter2.count(letter2)
occurance3 = letter3.count(letter3)
print(occurance1)
print(occurance2)
print(occurance3)

# step 4: How many words are in the whole text?
text_tuple= tuple(text)
print( "all letters in text" + str(text_tuple))

#step 5: Invert the whole text
inverted_text= text[::-1]
print(inverted_text)
# step 6 find the 1st and last words of the text
first_letter= text[0]
last_letter= text[-1]
print(first_letter)
print(last_letter)
# step 7 is the word "python" in the text
tp=text

print('python' in tp)


