#! python3
# Quiz.py
# Creates quizzes with questions and answers in
# random order, along with the answer key.

import random
# The quiz data. Keys are states values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
            'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
            'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
            'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord',
            'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
            'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
# Generate 35 quiz files

for quizNum in range(35):
    # Create the quiz file and answer key files
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')

    # Write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')

    # Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states) # Shuffles order of the states so they are asked in a random order

    # Loop through all 50 states, making a question for each
    for questionNum in range(50): # there are 50 questions

        # Get right and wrong answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())      # Get a complete list of answers
        del wrongAnswers[wrongAnswers.index(correctAnswer)]     # Removes the right answer
        wrongAnswers = random.sample(wrongAnswers, 3)   # Picks 3 random cities
        answerOptions = wrongAnswers + [correctAnswer]  # Shows the 3 wrong answers and the right answer
        random.shuffle(answerOptions)   # Answers are randomised so answers arent always D

        # Write the question and the answer options to the quiz file
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4): # use 4 as there are 4 choices of answer
            quizFile.write(f"{'ABCD'[i]}.{answerOptions[i]}\n") # Writes to file
        quizFile.write('\n') # '\n' is a new line

        # Write answer key to a file
        answerKeyFile.write(f"{questionNum + 1, 'ABCD' [answerOptions.index(correctAnswer)]}")
    quizFile.close()
    answerKeyFile.close()   # Closes the files when done

