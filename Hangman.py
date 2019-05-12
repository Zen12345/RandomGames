word = 'Hello'.lower()
win = False
line = "________________________"
hangman = (

"""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,

"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    H""",

"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    HA""",

"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    HAN""",


"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    HANG""",


"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    HANGM""",



"""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    HANGMA""",


"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    HANGMAN""")
guess_list = ['_' for x in word]
guess_words = []
print(hangman[0])
counter = 0
while win == False:
    guess = input("Guess a letter: ").lower()
    while True:
        if len(guess) != 1:
            guess = input("Please enter only 1 letter: ")
        elif guess in guess_words:
            guess = input("You entered this word already: ") 
        else:
            try:
                val = int(guess)
                guess = input("Don't enter a number: ")
            except ValueError:
                break
            
        
    guess_words.append(guess)
    for y, x in enumerate(word):
        if guess == x:
            guess_list[y] = guess
    if guess not in word:
        counter += 1
    guess_string = ' '.join(guess_list)
    print("\n \n \n" + line)
    print(guess_string)
    print(hangman[counter])
    print(line)
    if counter == 7:
        print("You have lost!")
        break
    if '_' not in guess_list:
        print("You have won!")
        break