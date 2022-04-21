#quiz with question propmts in an array
from questionClass import Question
question_prompts = [
    "What color are apples\n(a) Red/Green\n(b) Purple\n(c) Yellow\n\n",
    "What color are bananas\n(a) Yellow\n(b) Teal\n(c) Black\n\n",
    "What color are strawberries\n(a) Red\n(b) Brown\n(c) Magenta\n\n"
    ]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a")
    ]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+= 1

    print("You got " + str(score) + " out of " + str(len(questions)) + " correct")

run_test(questions)