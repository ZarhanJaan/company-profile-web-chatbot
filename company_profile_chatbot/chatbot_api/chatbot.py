import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return json.load(file)

knowledge_base = load_knowledge_base("knowledge_base.json")

questions = [q["question"] for q in knowledge_base["questions"]]
answers = [q["answer"] for q in knowledge_base["questions"]]
intents = [str(i) for i in range(len(questions))]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

model = MultinomialNB()
model.fit(X, intents)

def get_answer(user_input: str) -> str:
    X_test = vectorizer.transform([user_input])
    predicted_intent = model.predict(X_test)[0]
    return answers[int(predicted_intent)]