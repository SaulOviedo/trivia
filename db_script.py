import html
import requests

questions = []

for i in range(20):
    res = requests.get('https://opentdb.com/api.php?amount=50&category=9&type=multiple')
    res_json = res.json()

    for q in res_json['results']:
        q['question'] = html.unescape(q['question'])
        q['correct_answer'] = html.unescape(q['correct_answer'])
        q['incorrect_answers'] = [html.unescape(e) for e in q['incorrect_answers']]

    questions += res_json['results']

with open('questions.txt', 'w') as f:
    for q in questions:
        data = [q['difficulty'], q['question'], q['correct_answer']] + q['incorrect_answers']
        f.write('||'.join(data)+'\n')