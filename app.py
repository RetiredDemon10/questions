from question import Question

questions_prompts = [
    "what color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "what color are bananas?\n(a) teal\n(b) magenta\n(c) yellow\n\n",
    "what color are strawberries?\n(a) yellow\n(b) red\n(c) Orange\n\n",
]

questions = [
    Question(questions_prompts[0], "a"),
    Question(questions_prompts[1], "c"),
    Question(questions_prompts[2], "b"),

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)