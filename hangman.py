import random 
# library that we use in order to choose on random words from a list of words

def hangman(name):
        global turns
        #User defined function
        
        words = ['test', 'aromatic', 'reading', 'programming', 
		'python', 'painful', 'cars', 'unsightly', 
		'memory', 'permit', 'skirt', 'coordinated','permit','bumpy'
                 ,'gigantic','canvas','secretary','straw','chew','orange'] 
        #list of letters to be used in game [randomly generated 20 words from a website
        #refer https://www.randomlists.com/random-words ] 
 
        word = random.choice(words) 
        # Function will choose a word randomly from the list

        print("Guess the characters") 
        #notifies the user that they can start the game
        
        guesses = ''      
        #empty string
        
        while turns > 0:
	
                # counts the number of times a user fails 
                failed = 0
	
                # all characters from the input word taking one at a time. 
                for char in word: 
		
                        # comparing that character with the character in guesses 
                        if char in guesses: 
                                print(char) 
			
                        else: 
                                print("_") 
			
                                # for every failure 1 will be incremented in failure 
                                failed += 1
			

                if failed == 0: 
                        # user will win the game if failure is 0 and 'You Win' will be given as output 
                        print("You Win") 
		
                        # this print the correct word 
                        print("The word is: ", word) 
                        break
	
                # if user has input the wrong alphabet then it will ask user to enter another alphabet 
                guess = input("guess a character:") 
	
                # every input character will be stored in guesses 
                guesses += guess 
	
                # check input with the character in word 
                if guess not in word: 
		
                        turns -= 1
		
                        # if the character doesn’t match the word then “Wrong” will be given as output 
                        print("Wrong") 
		
                        # this will print the number of turns left for the user 
                        print("Dear",name,"You have", + turns, 'more guesses') 
		
		
                        if turns == 0: 
                                print("You Loose")
                                ip=input("""Thank you for playing the game""",name)
                                
                                


name=input("Enter Your name :-\n")
print("Hello",name,"!\n")
turns=int(input("""How many chance would you like to have
        ->if you are a beginner player select a number between 11-20
        ->if you are an intermediate player select a number between 6-10
        ->if you are an advanced player select a number between 3-5\n"""))
hangman(name)
