import sys 
import requests

# based on https://github.com/chubin/wttr.in

resp = requests.get(f'https://wttr.in/{sys.argv[1].replace(" ", "+")}')
print(resp.text)

resp = requests.get(f'https://v2.wttr.in/{sys.argv[1].replace(" ", "+")}')
print(resp.text)