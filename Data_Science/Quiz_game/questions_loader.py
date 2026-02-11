import json
from question import Question

def load_questions(path="data/questions.json"):
    with open(path, "r", encoding="utf-8") as f:
        raw_questions = json.load(f)

    questions = []
    for q in raw_questions:
        questions.append(Question(q["question"], q["choices"], q["answer"]))

    return questions
