# a dictionary that stores question and answer
# have a variable that tracks the score of the player
# loop through the dictionary using key value pairs
# display each question to users and allow them to answer
# tell them if they are right or wrong
# show the final result when quiz is completed

quiz = {
    "question1": {
        "question": "what is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": 'Rome'
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": 'Rome'
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "answer": 'Madrid'
    },
    "question5": {
        "question": "What is the capital of Portugal?",
        "answer": 'Lisbon'
    },
    "question6": {
        "question": "What is the capital of Switzerland?",
        "answer": 'Bern'
    },
    "question7": {
        "question": "What is the capital of Austria?",
        "answer": 'Vienna'
    },
}

score = 0

for key,value in quiz.items():
    print(value['question'])
    answer = input('Answer? ')

    if answer.lower() == value['answer'].lower():
        print('correct')
        score +=1
        print('Your score is: ',score)
        print('')
        print('')
    
    else:
        print('Wrong')
        print('The answer is: ', value['answer'])
        print('Your score is: ',score)
        print('')
        print('')

print('You got ', score , "out of 7 question correctly")
print('Your percentage is ', str(int(score/7*100)),'%')

