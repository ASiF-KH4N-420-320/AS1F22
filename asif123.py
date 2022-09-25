import os, platform
try:
    import requests
except:
    os.system('pip install requests')
 
import requests
bit = platform.architecture()[0]
 


elif bit == '32bit':
    from AS1F32 import create_file
    create_file()
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
