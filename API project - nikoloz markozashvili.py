import requests
import json
import sqlite3

url = 'https://catfact.ninja/fact'
response = requests.get(url)
result_json = response.text
res = json.loads(result_json)
res_structured = json.dumps(res, indent=1)

print(res['fact'])

conn = sqlite3.connect('CarFactos.sqlite')
c = conn.cursor()

new_fact = res['fact']

c.execute('CREATE TABLE IF NOT EXISTS facts (fact TEXT)')
c.execute('INSERT INTO facts (fact )VALUES (? )',(new_fact,))

conn.commit()
conn.close()

