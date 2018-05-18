

# -*- coding: cp1252 -*-
medium_string = '''The def keyword is used to create a ___1___. You specify the inputs a ___1___ 
takes by adding ___2___ separated by commas between the parentheses.\n ___1___s by default return ___3___ 
    if you don't specify the value to return. \n ___2___ can be standard data types such as string, number, 
dictionary,tuple, and ___4___ or can be more complicated such as objects and lambda functions.\n'''
medium_answers = ["function", "function", "arguements", "function", "None","arguements", "list"]

easy_string = '''A common first thing to do in programming is to display Hello ___1___! \n In ___2___ this is particulary easy; all you have to do is 
type in: ___3___  “Hello ___1___”  Of course, that isn’t a very useful thing to do. \n However, it is an example of how output to the user using the ___3___ command, and
produces a program which does something, so it is useful in that capacity.\n
It may seem a bit odd to do something in a totally complete language that can be done even more easily with an ___4___ file in a browser, but it’s a step in learning ___2___ syntax,
and that’s really its purpose.\n'''
easy_answers = ["World", "python", "print", "World", "py"]

hard_string = '''Goku is the main hero of the manga series called ___1___. Goku is a ___2___ who lives on Earth.  He has two sons: ___3___ and ___4___.\n '''
hard_answers = ["Dragonball", "Sayian", "Gohan", "Goten"]

#List of blanks that will be passed in.
blanks1 = ["___1___", "___2___","___3___", "___4___"]



#checks to see if strings in blanks1 are also in answer, if so returns the blank.
#pos isn't in answer, returns None

def fill_in_blanks(answer, blanks):
    for pos in blanks:
        if pos in answer:
            return pos
    return None

#plays the fill in the blank game.  The user will be provided with a paragraph (fib_string) containing blanks.
#function returns "game over if the user exceeds the number of tries
#if user answers correclty, it returns the correct filled in blank
#The user will then be asked to fill in each blank. 

def play_game(fib_string, blanks):
    replaced = []
    
    print fib_string
    fib_string = fib_string.split()
    for answer in fib_string:
        replacement = fill_in_blanks(answer, blanks)
        if replacement != None:
            user_input = raw_input("Fill in the blank for: " + replacement + " ")
            ic(user_input, replaced, replacement, answer)
            #if statement to check for correct answer
            #tries = 0
            #while user_input != answers[correct_answer]:
                #tries = tries + 1
                #if tries == user_attempt:
                    #return "Game Over, you used up all your chances."
               # print ("\nIncorrect, try again. You have used " + str(tries) + "/" + str(user_attempt) + "\n" + " "  .join(replaced) + " " + replacement)
                #user_input = raw_input("Fill in the blank for: " + replacement + " ")
            answer = answer.replace(replacement, user_input)
            replaced.append(answer)
            print "Correct \n" + " ".join(replaced)
            
        else:
            replaced.append(answer)
    replaced = " ".join(replaced)
    return replaced
#checks if the user response is correct
def ic(user_input, replaced, replacement, answer):
    correct_answer = 0
    #if statement to check for correct answer
    tries = 0
    while user_input != answers[correct_answer]:
        tries = tries + 1
        if tries == user_attempt:
            return "Game Over, you used up all your chances."
        print ("\nIncorrect, try again. You have used " + str(tries) + "/" + str(user_attempt) + "\n" + " "  .join(replaced) + " " + replacement)
        user_input = raw_input("Fill in the blank for: " + replacement + " ")
    correct_answer = correct_answer + 1
    
    
    

#prompts the user to enter a difficulty level and
#sends an error if an incorrect selection was made (I couldn't get this to work)
user_input2 = raw_input('''Please select a game difficulty by typing it in! \n Possible choices include easy, medium, and hard. ''')
user_input2.lower()
user_attempt = int(raw_input("Enter the number of guesses you will receive: "))

#while user_input2 != "easy" or "medium" or "hard":
    #print "That's not an option! Please select a game difficulty by typing it in!"
   
if user_input2 == "easy":
    answers = easy_answers
    print play_game(easy_string, blanks1)
elif user_input2 == "medium":
    answers = medium_answers
    print play_game(medium_string, blanks1)
elif user_input2 == "hard":
    answers = hard_answers
    print play_game(hard_string, blanks1)
    
