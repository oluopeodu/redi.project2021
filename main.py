from Question import Question
question_prompts = [
    "What is the national symbol of Canada?\n(a) A Mermaid\n(b) A Hen\n(c) A Maple leaf\n\n",
    "Which country in Latin America recognizes 68 official languages?\n(a) Panama\n(b) Mexico\n(c) Brazil\n\n",
    "Where is Nigeria located in Africa?\n(a) East\n(b) South\n(c) West\n\n",
    "Where in the world is the biggest lake, the Baikal Lake located?\n(a) Russia\n(b) Brazil\n(c),India\n\n"
]
questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)