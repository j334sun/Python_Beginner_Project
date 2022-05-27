print("\n\n\n\n\n\n\n\n")
life = 7

word = "pythonday"
word_list = list(word)


empty = "_ " * len(word)

letter_count = 0

#print(word_list)
#print(empty)


while life > 0 and letter_count < len(word):
    letter = input("Guess a letter ")
    if letter in word_list:
        while letter in word_list:
            position = word_list.index(letter)
            empty = empty[0:position*2] + letter + empty[position*2+1:]
            empty_list = list(empty)
            letter_count += 1
            #word_list[position] = "_"
        print("{}\n".format(empty))
        #print(word_list)
    elif letter in empty_list:
        print("You have already guessed this letter.\n")
    else:
        life -= 1
        if life > 0:
            print("Wrong! Now you have {} life.".format(life))
        else:
            print("You died!")
          
print("\n\n\n\n\n\n\n\n")          
          
          
          
          
            

        
        
        
        

