import os, platform

try:

    import requests

except:

    os.system('pip install requests')

os.system('git pull')

import requests

os.system('git pull')

bit = platform.architecture()[0]

if bit == '64bit':

    import 64bit

elif bit == '32bit':

    import 32bit
