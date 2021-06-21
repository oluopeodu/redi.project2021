# The game is played by one player who is asked a series of multiple choice questions where they can test
# their knowledge of geography, mountains, lakes.
# The player is awarded points for a correct answer or is deducted points for an incorrect answer.

question_prompts = [
    "1) What is the national symbol of Canada?\n (a) Mermaid\n (b) Hen\n (c) Maple leaf\n\n",
    "2) Which country in Latin America recognizes 68 official languages? \n (a) Panama\n (b) Mexico\n (c) Brazil\n\n",
    "3) Where is Nigeria located in Africa? \n (a) North\n (b) South\n (c) West\n\n",
    "4) What is the highest mountain in Italy?\n (a) Monte Bianco\n (b) Grenzgipgel\n (c) Gran Paradiso\n\n",
    "5) In which country is the Baikal Lake located?\n (a) Russia\n (b) Brazil\n (c) India\n\n",
    "6) What city in Poland is considered to be its medieval capital?\n (a) Wroclaw\n (b) Gdansk\n (c) Krakow\n\n",
    "7) In which country did Halloween originate?\n (a) Lithuania\n (b) Slovakia\n  (c) Ireland\n\n",
    "8) What is the longest river in Asia?\n (a) Indus\n (b) Yangtzy\n (c) Irtysh\n\n",
    "9) Where did the dodo bird originate from?\n (a) Mauritius\n (b) New Zealand\n (c) The Maldives\n\n",
    "10) What is the traditional Maori dish cooked underground called?\n (a) Rewena pararoa\n (b) Hangi\n (c) Kumara\n\n",
    "11) Which, from the following is a landlocked sea?\n (a) Aral\n  (b) Arafura\n (c) Greenland\n\n",
    "12) What is the constant intermingling of salt water and fresh water called?\n  (a) Delta\n (b) Bay\n (c) Estuary\n\n",
    "13) Where can you find basaltic lava?\n (a) Indo-Gangetic Plain\n (b) Deccan Trap\n (c) North-Eastern Hills\n\n",
]

class Question:
    def __init__(self, prompt, answers):
        self.prompt = prompt
        self.answers = answers

    def get_correct_answer(self):
        for answer in self.answers:
          if answer.is_correct == True:
            return answer

    def is_correct_answer(self,selection_answer):
        for answer in self.answers:
            if answer.selection_answer == selection_answer:
                return answer.is_correct
        return False

class Answer:
    def __init__(self, text_answer, selection_answer, is_correct):
        self.text_answer = text_answer
        self.selection_answer = selection_answer
        self.is_correct = is_correct

questions = [
    Question(question_prompts[0],[Answer('Mermaid','a',False), Answer('Hen','b', False),Answer ('Maple Leaf','c', True)]),
    Question(question_prompts[1],[Answer('Panama','a',False), Answer('Mexico','b', True),Answer ('Brazil','c', False)]),
    Question(question_prompts[2],[Answer('North','a',False), Answer('South','b', False),Answer ('West','c', True)]),
    Question(question_prompts[3],[Answer('Monte Bianco','a',True), Answer('Mexico','b', False),Answer ('Brazil','c', False)]),
    Question(question_prompts[4],[Answer('Russia','a',True), Answer('Brazil','b', False),Answer ('India','c', False)]),
    Question(question_prompts[5],[Answer('Wroclaw','a',True), Answer('Gdansk','b', False),Answer ('Krakow','c', False)]),
    Question(question_prompts[6],[Answer('Lithuania','a',False), Answer('Slovakia','b', False),Answer ('Ireland','c', True)]),
    Question(question_prompts[7],[Answer('Indus','a',False), Answer('Yangtzy','b', True),Answer ('Irtysh','c', False)]),
    Question(question_prompts[8], [Answer('Mauritius','a',True), Answer('New Zealand','b', False),Answer ('The Maldives','c', False)]),
    Question(question_prompts[9], [Answer('Rewena Pararoa','a',False), Answer('Hangi','b', True),Answer ('Kumara','c', False)]),
    Question(question_prompts[10], [Answer('Aral','a',True), Answer('Arafura','b', False),Answer ('Greenland','c', False)]),
    Question(question_prompts[11], [Answer('Delta','a',False), Answer('Bay','b', False),Answer ('Estuary','c', True)]),
    Question(question_prompts[12], [Answer('Ingo-Gangetic Plain','a',False), Answer('Deccan Trap','b', True),Answer ('North_Eastern Hills','c', False)]),
]

def run_game():
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if question.is_correct_answer(answer):
            score += 1
        else:
            score -= 1
        correct_answer = question.get_correct_answer()
        print(f'Score is {score} and correct answer is {correct_answer.selection_answer}\n')
    print("Congratulations You got" + str(score) + "/" + str(len(questions)) + " Correct!")

run_game()

