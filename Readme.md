# App 
[![Stability](https://img.shields.io/badge/stability-stable-green.svg)](https://img.shields.io/badge/stability-stable-green.svg)[![Git count](http://hits.dwyl.com/hhaydar/ml-app-insurance.svg)](http://hits.dwyl.com/hhaydar/ml-app-insurance)

<!--
[![Documentation Status](https://readthedocs.org/projects/pip/badge/?version=stable)](http://pip.pypa.io/en/stable/?badge=stable)
[![PyPI version](https://badge.fury.io/py/pycaret.svg)](https://badge.fury.io/py/pycaret)
[![License](https://img.shields.io/pypi/l/ansicolortags.svg)](https://img.shields.io/pypi/l/ansicolortags.svg)
--> 

App is an application to study ml-algorithm in this case (prediction). I use a data for insurance basically I watch out this medium paper. 
https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99 

## Installation

You need PyCaret, Flask that's all.

```bash
pip install pycaret
pip install flask
```

## Web Page Usage
https://hh-insurance.herokuapp.com/


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

### What's included

Within the download you'll find the following directories and files.

```
ml-app-insurance/
├── api_json_test.py
├── Procfile
├── README.md
├── dataset
│   ├── insurance.csv
├── templates
│   ├── home.html
├── app.py
├── requirements.txt
├── insurance_14052020.pkl {model}
```
## License
