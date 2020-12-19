import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'bw':2, 'd':9, 'fc':6,'a/d':5,'pf':8, 'Ef':7})

print(r.json())