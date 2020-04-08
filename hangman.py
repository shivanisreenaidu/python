print("Hangman game")
print ("Start guessing")
word = "balloon"
guesses = ''
turns = 10
while turns > 0:         
    failed = 0             
    for char in word:      
        if char in guesses:    
            print(char)    
        else:
            print("")  
            failed += 1    
    if failed == 0:        
        print ("You won")  
        break              
    print
    guess =input("guess a character:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print("Wrong")
        print("You have", + turns, 'more guesses') 
        if turns == 0:           
            print("You Lose")
 
