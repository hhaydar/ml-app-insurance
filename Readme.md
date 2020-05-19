#Code for learning how to predict insurance fare using Pycaret and Flask

Go to this url and pass some data it will return the insurance fare acording to values
https://hh-insurance.herokuapp.com/

For API Request use:
api_json_test.py


# App 

App is an application to study ml-algorithm in this case (prediction). I use a data for insurance basically I watch out this medium paper. 
https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99 

## Installation

You need PyCaret, Flask that's all.

```bash
pip install pycaret
pip install flask
```

## Web Page Usage
```html
https://hh-insurance.herokuapp.com/
```

## API Usage

```python
import requests
url = 'https://hh-insurance.herokuapp.com/predict_api'
pred = requests.post(url,json={ 'age':55,
                                'sex':'male',
                                 'bmi':59,
                                 'children':1,
                                 'smoker':'male',
                                 'region':'northwest'})
print(pred.json())
```

```python
python api_json_test.py
```

## Contributing
Pull requests are welcome.

## License
[MIT](https://choosealicense.com/licenses/mit/)