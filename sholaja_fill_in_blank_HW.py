
# -*- coding: cp1252 -*-
medium_string = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ 
takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ 
    if you don't specify the value to return. ___2___ can be standard data types such as string, number, 
dictionary,tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
medium_answers = ["function", "arguements", "None", "list"]

easy_string = '''A common first thing to do in programming is to display Hello ___1___! In ___2___ this is particulary easy; all you have to do is 
type in: ___3___  “Hello ___1___”  Of course, that isn’t a very useful thing to do. However, it is an example of how output to the user using the ___3___ command, and
produces a program which does something, so it is useful in that capacity.
It may seem a bit odd to do something in a totally complete language that can be done even more easily with an ___4___ file in a browser, but it’s a step in learning ___2___ syntax,
and that’s really its purpose.'''
easy_answers = ["World", "python", "print", "py"]

hard_string = '''Goku is the main hero of the manga series called ___1___. Goku is a ___2___ who lives on Earth.  He has two sons: ___3___ and ___4___. '''
hard_answers = ["Dragonball", "Sayian", "Gohan", "Goten"]

#List of blanks that will be passed in.
blanks1 = ["___1___", "___2___","___3___", "___4___"]



#checks to see if strings in blanks1 are also in answer

def fill_in_blanks(answer, blanks):
    for pos in blanks:
        if pos in answer:
            return pos
    return None

#plays the fill in the blank game.  The user will be provided with a paragraph (fib_string) containing blanks.
#The user will then be asked to fill in each blank. 

def play_game(fib_string, blanks):
    replaced = []
    print fib_string
    fib_string = fib_string.split()
    for answer in fib_string:
        replacement = fill_in_blanks(answer, blanks)

        if replacement != None:
            user_input = raw_input("Fill in the blank for: " + replacement + " ")
            #if statement to check for correct answer
            hard_correct(user_input)
            answer = answer.replace(replacement, user_input)
            replaced.append(answer)
        else:
            replaced.append(answer)
    replaced = " ".join(replaced)
    return replaced


#prompts the user to enter a difficulty level and
#sends an error if an incorrect selection was made
user_input2 = raw_input('''Please select a game difficulty by typing it in!
            Possible choices include easy, medium, and hard. ''')
user_input2.lower()
while user_input2 != "easy" or "medium" or "hard":
    print "That's not an option! Please select a game difficulty by typing it in!"
    user_input2 = raw_input('''Please select a game difficulty by typing it in!
            Possible choices include easy, medium, and hard. ''')
    if user_input2 == "easy":
        print play_game(easy_string, blanks1)
    elif user_input2 == "medium":
        print play_game(medium_string, blanks1)
    elif user_input2 == "hard":
        print play_game(hard_string, blanks1)
    

    
