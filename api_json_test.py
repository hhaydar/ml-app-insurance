import requests
url = 'https://hh-insurance.herokuapp.com/predict_api'
pred = requests.post(url,json={ 'age':55,
                                'sex':'male',
                                 'bmi':59,
                                 'children':1,
                                 'smoker':'male',
                                 'region':'northwest'})
print(pred.json())