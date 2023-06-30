import os
try:import requests
except:
  os.system('clear')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('xdg-open https://www.facebook.com/profile.php?id=100090830941440')
os.system('git pull')
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
  os.system('chmod 777 main;./main')
else:
  exit(' Sorry Device Not Support ')
