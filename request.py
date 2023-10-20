import requests

url = 'http://localhost:5000/predict_api'
import requests

url = 'http://localhost:5000/predict_api'

data = {
    'Recipientgender': 1,
    'Stemcellsource': 1,
    'Donorage': 22.830137,
    'Donorage35': 0,
    'Gendermatch': 0,
    'DonorABO': 1,
    'RecipientABO': 1.0,
    'RecipientRh': 1.0,
    'ABOmatch': 0.0,
    'CMVstatus': 3.0,
    'DonorCMV': 1.0,
    'RecipientCMV': 1.0,
    'Disease': 'ALL',
    'Riskgroup': 1,
    'Txpostrelapse': 0,
    'Diseasegroup': 1,
    'HLAmatch': 0,
    'HLAmismatch': 0,
    'Antigen': -1.0,
    'Allele': -1.0,
    'HLAgrI': 0,
    'Recipientage': 9.6,
    'Recipientage10': 0,
    'Recipientageint': 1,
    'Relapse': 0,
    'CD34kgx10d6': 7.2,
    'CD3dCD34': 1.33876,
    'CD3dkgx10d8': 5.38,
    'Rbodymass': 35.0,
    'ANCrecovery': 19,
    'PLTrecovery': 51
}

r = requests.post(url, json=data)

print(r.json())


r = requests.post(url,json=data)

print(r.json())