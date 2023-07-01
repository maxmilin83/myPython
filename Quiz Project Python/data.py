import requests

API = "https://opentdb.com/api.php?amount=10&category=23&difficulty=easy&type=boolean"
request = requests.get(f"{API}")
request = request.json()
request = request['results']

questions = []

for question in request:
    questions.append({'text':question['question'],'answer':question['correct_answer']})


