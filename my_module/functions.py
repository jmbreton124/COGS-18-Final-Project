import time
import threading  # learned about threading and time from geeks for geeks, https://www.geeksforgeeks.org/timer-objects-python/

isTime = bool(1)

# Function "start_quiz" takes questions, as defined earlier, as input.
def start_quiz(questions): # learned how to format code for a quiz from mikedane.com
    """Generating a quiz while simultaneously grading it and giving you a score at the end.
    
    Parameters
    ----------
    questions : list
        Each index holds a list of strings, that is a question, followed by 4 answer choices, a, b, c, and d.
        
    Returns
    -------
    score : int
        The users end score for the quiz.
    """
    
    # User starts off with having 0 points
    score = 0
    
    # A for loop that loops through questions in input
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    
    # Printed statement at the end of the quiz that reveals users score
    print("Congrats! You got", score, "out of", len(questions))
    
# Function "continue_on" bridges both quizzes together.     
def continue_on():   # Caitlin helped me understand how to write docstrings with no Parameters
    """Requires user input to either continue on to Bonus Quiz or quit the quiz.
    
    Parameters
    ----------
    None
        
    Returns
    -------
    True : bool
        Will return True when user types an input of 'start'.
    False : bool
        Will return False when user types an input of 'stop'.
    """
    
    value = input("Please type 'start' if you'd like to complete the Bonus Round, or 'stop' to exit.\n\n")
    
    if value == 'start':
        print("Alright, let's continue!")
        return True
    elif value  == 'stop':
        print('Ok, bye!')        
        return False
        

# Function "start_bonus" takes questions_2, as defined earlier, as input.
def start_bonus(questions_2):
    """Generates a timed second quiz while simultaneously grading it and giving you a score at the end.
    
    Parameters
    ----------
    questions : list
        Each index holds a list of strings, that is a question, followed by 4 answer choices, a, b, c, and d.
        
    Returns
    -------
    score : int
        The users end score for the quiz.
    """
    
    print("Are you ready? You have 30 seconds to answer the next 10 questions. \nNotice: If your quiz times out while on a question, just press enter to see your final score!")
    
    timer = threading.Timer(60.0, time_is_up) # setting up the timer to give user 30 seconds
    timer.start()

    # User starts off with having 0 points
    score = 0
    
    # A for loop that loops through questions in input
    for question in questions_2:
        answer = input(question.prompt)
        if not isTime:
            break
        if answer == question.answer:
            score += 1
    
    # Printed statement at the end of the quiz that reveals users score
    print("That was the bonus round! You got", score, "out of", len(questions_2))
    

# After allotted time, function "time_is_up" will stop timer.
def time_is_up():
    """Ends time when 30 seconds have passed.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
        Doesn't return an an output because it's a function embeded in another function.
    """
    print("Oh man, time's up! Better luck next time!")
    global isTime # Global allows for modifications to be made to a variable while it's outside of its current scope
    isTime = bool(False)