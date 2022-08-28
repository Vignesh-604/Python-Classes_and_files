from Class import Quiz

Questions = [
    "Which one of the below is a pet animal? \n(a) Cat \n(b) Monkey \n(c) Both \n",
    "Pick the odd one out. \n(a) Dog \n(b) Bear \n(c) Wolf \n",
    "Who is a member of the cat family? \n(a) Butterfly \n(b) Tiger \n(c) Bear \n",
]
Class = [
    Quiz(Questions[0], "a"),
    Quiz(Questions[1], "a"),
    Quiz(Questions[2], "b")
]
def Pop(x):
    score = 0
    for ask in x:
        answer = input(ask.quiz)
        if answer == ask.ans:
            score += 1
    print("You got " + str(score) + " out of " + str(len(x)) + " questions correct.")

Pop(Class)
