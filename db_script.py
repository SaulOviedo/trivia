import html
import requests
import pickle
import pandas as pd

questions = []

for i in range(20):
    res = requests.get('https://opentdb.com/api.php?amount=50&category=9&type=multiple')
    res_json = res.json()

    for q in res_json['results']:
        q['question'] = html.unescape(q['question'])
        q['correct_answer'] = html.unescape(q['correct_answer'])
        q['incorrect_answers'] = [html.unescape(e) for e in q['incorrect_answers']]

    questions += res_json['results']

df = pd.DataFrame(questions)
df.to_csv('questions.csv')

# with open('questions.pickle', 'wb') as f:
#     pickle.dump(questions, f)