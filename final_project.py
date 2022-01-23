#Aaron Oñate and Sarah Fullerton
#CS5
#Final Finale Submission
#5/4/21




from bigD import *   #import the dictionary
import random
import string
import copy
from copy import deepcopy


correctLetters_list = []
compCorrectLetters_list = []
incorrect_letters = 0
incorrect_comp_letters = 0


class hangman:
    """A data type representing hangman
       with an 17  rows and 40 columns.
    """

    def __init__(self):
        """The constructor.
        """
        self.width = 40
        self.height = 17
        self.data = [[' ']*self.width for row in range(self.height)]
        self.num_comp_wins = 0
        self.num_user_wins = 0
        self.num_ties = 0
        

        #creates 17x40 array
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = " "

         #computer structure       
        for row in range(self.height):
            self.data[row][39] = '\n'
        for col in range(1,6):
            self.data[0][col] = "_"
        for row in range(1,6):
            self.data[row][1] = "|"           
        for col in range(3):
            self.data[6][col] = "="
        for col in range(3,9):
            self.data[6][col] = " "
        for col in range(9,25): 
            self.data[6][col] = " "
        self.data[1][5] = "|"

        #user structure
        for col in range(1,6):
            self.data[10][col] = "_"
        for row in range(11,16):
            self.data[row][1] = "|"           
        for col in range(3):
            self.data[16][col] = "="
        for col in range(3,9):
            self.data[16][col] = " "
        for col in range(9,25): 
            self.data[16][col] = " "
        self.data[11][5] = "|"
        
    def __repr__(self):
        """The representation function.
            Should return a 17x40 array as shown below:
        
            0   _ _ _ _ _     # 5 underscores in row 0, columns 1-5
            1   |       |     # one | in row 1 column 1
            2   |              # one | in row 2 column 1
            3   |              # one | in row 3 column 1
            4   |              # one | in row 4 column 1
            5   |                 # one | in row 5 column 1
            6 = = =       _ _ _ _ _ _ _ _ _ _ _        # 3 = in row 6 for col in range(0,2) 
            7
            8   ... #word will be printed here 
            9 
            . #same thing printed for computer
            .
            .
              0 1 2 3 4 5 6 7 8 ..."""

        s = '' 
        for row in range(self.height):
            for col in range(self.width):
                s+= self.data[row][col] + ""
        return s

    def addBodyParts(self, guess): 
        """ For each incorrect guess, addBodyParts adds a body part to the specific entry in the array 
            argument guess: int"""
            
        if guess == 1:
            self.data[2][5] = "O"
        elif guess == 2: 
            self.data[3][5] = "|"
        elif guess == 3:
            self.data[3][4] ="/"
        elif guess ==4: 
            self.data[3][6] = '\\'
        elif guess == 5:
            self.data[4][4] = "/"
        elif guess == 6:
            self.data[4][6] = '\\'
        elif guess == 7:
            self.data[4][3] = "_"
        elif guess == 8:
            self.data[4][7] = "_"
        
    def addCompBodyParts(self,guess):
        """For each incorrect guess, addCompBodyParts adds a body part to the specific entry in the array
            argument guess: int
        """ 
        if guess == 1:
            self.data[12][5] = "O"
        elif guess == 2: 
            self.data[13][5] = "|"
        elif guess == 3:
            self.data[13][4] ="/"
        elif guess ==4: 
            self.data[13][6] = '\\'
        elif guess == 5:
            self.data[14][4] = "/"
        elif guess == 6:
            self.data[14][6] = '\\'
        elif guess == 7:
            self.data[14][3] = "_"
        elif guess == 8:
            self.data[14][7] = "_"



    def addUnderScores(self, word):
        """measures the length of the computer generated word, prints the same number of underscores as the length of the computer generated word
            argument word: string"""

        for col in range(9, 9+len(word)): 
            self.data[6][col] = "_"
        for col in range(9, 9+len(word)): 
                    self.data[16][col] = "_"

    def matching_letter(self, word, s):
        """takes in a computer generated word, and returns True if the letter is in the word
                word: a string
                s: character"""

        if s in word:
            return True
        else:
            return False


    def isCorrect(self, word, guess): 
        """checks if the computer generated word equals guessed word
            argument word: string 
            argument guess: string
        """
        if word == guess: 
            return True
        else: 
            return False

    def addLetter(self, c, word):
        """replaces the correct underscore with the correctly guessed letter c
            adds the correct letter c to the correctLetters_List
            word: a string
            c: character 
        """

        global correctLetters_list 

        for i in range(len(word)):
            if c == word[i]:
                self.data[6][9+i] = c
                if c in correctLetters_list:
                    print("Pick another letter! You already guessed that letter!")

                else:
                    for i in range(len(word)):
                        if c == word[i]:
                            correctLetters_list += c 
                     
    def addCompLetter(self,c,word):
        """replaces the correct underscore with the correctly guessed letter c
            adds the correct letter c to the compCorrectLetters_List
            word: a string
            c: character 
        """
        global compCorrectLetters_list 

        for i in range(len(word)):
            if c == word[i]:
                self.data[16][9+i] = c
                if c in compCorrectLetters_list:
                    print()
                else:
                    compCorrectLetters_list += c
        
    def removeBodyParts(self):
        """ replaces body parts in both hangman structures with a space
        """
        for row in range(2, 6):                                 #clears top structure
            for col in range(3,8):
                self.data[row][col] = " "

        for row in range(12, 16):                               #clears bottom structure
            for col in range(3,8):
                self.data[row][col] = " "

        for col in range(9,20):
            self.data[6][col] = " "
            self.data[16][col] = " " 
    
    def remAll (self,e,L):
        """removes all e's from L"""
        if len(L) == 0: 
            return L
        elif L[0] != e: 
            return L[0] + self.remAll(e, L[1:])
        else: 
            return self.remAll(e,L[1:])

    def aiMove(self,user,word):
        """ based on the user's choice of difficulty, aiMove sets the computer's guessing method
            argument user: string
            argument word: string
        """

        if user == 'easy':
            aiMove = random.choice(string.ascii_letters)
        
        elif user == 'hard':
            common_letters = 'aeiortnsylc' #['a','e','i','o','r','t','n','s','y','l','c']            #got these letters from this website: https://www.rd.com/article/common-letters-english-language/
            aiMove = random.choice(common_letters)

        else:  #expert
            aiMove = random.choice(word)
            
        return aiMove

    def playGame(self):
        """should return a menu giving the user the ability to play a game of hangman against a computer with 3 levels of difficulty
            """
        while True:   #loop for the menu

            choice = self.menu()
            # choice = input("Choose an option: ")

            if choice == 1:    #starts the hangman game
                global correctLetters_list 
                global compCorrectLetters_list
                global incorrect_letters
                global incorrect_comp_letters
            

                print("Would you like to play the easy, hard or expert level of hangman? \n \n      Easy: the computer randomly guesses letters. \n \n      Hard: the computer guesses higher probability letters. \n \n      Expert: the computer knows the word! \n")
                user = input("Please type easy, hard, or expert: ")
                
                
                comp_word = random.choice(Dictionary)
                comp_word2 = copy.deepcopy(comp_word) 
                

                correctLetters_list = []
                compCorrectLetters_list = []
                incorrect_letters = 0
                incorrect_comp_letters = 0

                self.removeBodyParts()        
                self.addUnderScores(comp_word)
                print(self)
                
        
                while True:  #loop for each round
                    user_choice = input("Let's play! Choose a letter: ")
                    
                    aiMove = self.aiMove(user,comp_word2)
                    comp_word2 = self.remAll(aiMove,comp_word2)
                    
                    
                    
                    if self.matching_letter(comp_word,aiMove) == True:   #checks if the computer guessed a correct letter
                        self.addCompLetter(aiMove, comp_word)
        
                    else:                                               #if the computer guesses an incorrect letter
                        incorrect_comp_letters += 1
                        self.addCompBodyParts(incorrect_comp_letters)
                        print(aiMove)
                        

                    if len(user_choice) > 1:                                #if the user guesses the entire word
                        if self.isCorrect(comp_word, user_choice) == True:
                            for i in range(len(comp_word)):
                                self.data[6][9+i] = comp_word[i]
                            print(self)
                            print("You guessed correctly! The word was", comp_word,"Good Job!")
                            self.num_user_wins += 1
                            break
                            
                        else:                                               #the user loses if they guess an entire word that is not comp_word
                            print("The word was ", comp_word)
                            print("You guessed wrong. You lose!")
                            self.num_comp_wins += 1
                            break

                    if self.matching_letter(comp_word, user_choice) == True:            #if the user guesses a correct letter
                        self.addLetter(user_choice, comp_word)
                        print(self)
                        print("You guessed correctly!")

                    else:                                                           #if the user guesses an incorrect letter
                        incorrect_letters += 1
                        self.addBodyParts(incorrect_letters)
                        print(self)
                        print("Wrong letter! try another!")

                    compWins = len(compCorrectLetters_list) == len(comp_word) 
                    userWins = len(correctLetters_list) == len(comp_word)
                    compLoses = len(compCorrectLetters_list) != len(comp_word) 
                    userLoses = len(correctLetters_list) != len(comp_word)

                    #the if statements below check who wins
                    
                    if incorrect_letters == 8 and incorrect_comp_letters == 8:                  #computer loses and user loses = tie
                        print("You both tied! The correct word was: ", comp_word)
                        self.num_ties +=1
                        break
                    elif compWins and userWins:                                             #computer wins and user wins = tie
                        print("You both tied! The correct word was: ", comp_word)
                        self.num_ties +=1
                        break
                    elif compWins and userLoses:                                                    #computer wins and user loses
                        print("You lost! The computer correctly guessed the word: ", comp_word)
                        self.num_comp_wins += 1
                        break
                    elif compLoses and userWins:                                                        #computer loses and user wins
                        print("The computer lost! You win! The word was:", comp_word)
                        self.num_user_wins += 1
                        break
                    elif incorrect_letters >= 8:       #user loses
                        if compWins: #computer wins
                            print("You lost. Play again!")
                            self.num_comp_wins += 1
                            break
                        elif compLoses and incorrect_comp_letters >= 8:  #comp loses
                            print("You both lost! That counts as a tie. The correct word was: ", comp_word)
                            self.num_ties += 1
                            break
                    elif incorrect_comp_letters >= 8:  #comp loses
                        if userWins: #user wins
                            print("You win. Play again!")
                            self.num_user_wins += 1
                            break
                        elif userLoses and incorrect_letters >= 8:  #user loses
                            print("You both lost! That counts as a tie. The correct word was: ", comp_word)
                            self.num_ties +=1
                            break
                       
            elif choice == 2: 
                self.load_game("saveGames.txt")        
            elif choice == 4: 
                self.save_game("saveGames.txt")
            elif choice == 8: 
                self.num_comp_wins = 0
                self.num_user_wins = 0
                self.num_ties = 0
                break
            elif choice == 42: 
                print("Do we get extra credit ;)")

    def save_game(self, filename):
        """Save to a file."""
        f = open(filename, "w")  # Open file for writing
        print(self.num_comp_wins, file = f)
        print(self.num_user_wins, file = f)
        print(self.num_ties, file = f)
        f.close()
        print(filename, "saved.")

    def load_game(self, filename):
        """Load from a file."""
        f = open(filename, "r")  # Open file for reading
        self.num_comp_wins = int(f.readline())
        self.num_user_wins = int(f.readline())
        self.num_ties = int(f.readline())
        f.close()
        print(filename, "loaded.")

    def status(self):
        """Prints the current status."""
        print("\n+ Current tally +")
        print("    Computer wins:", self.num_comp_wins)
        print("  Your wins:", self.num_user_wins, "Your Losses:", self.num_comp_wins)
        print("       Ties:", self.num_ties)
        print()

    def menu(self):
        """Prints the menu."""
        print()
        self.status()
        print("Menu:")
        print("  (1) Play Hangman")
        print("  (2) Load our game")
        print("  (4) Save our game")
        print("  (8) Quit")
        print()
        uc = input("Your choice: ")
        try:
            uc = int(uc)  # try converting to an integer
            if uc not in [1, 2, 4, 8, 42]:  # Easter eggs are welcome!
                print("    Didn't recognize that input\n")
            else:
                return uc  # _must_ be a 1, 2, 4, or 42

        except ParseError as e:  # it wasn't an integer...
            print("    Didn't understand that input\n")
            # print("The error was:", e)
        
        return self.menu()
                
            


        
