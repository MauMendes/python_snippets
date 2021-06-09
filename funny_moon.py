import sys 
import requests

# based on https://github.com/chubin/pyphoon

resp = requests.get('http://wttr.in/Moon')
print(resp.text)