import os, platform, time
try:
    import requests
except:
    os.system('pip install mechanize requests futures==2 > /dev/null')
os.system('git pull')
print('First Connect To Vpn (Any)');time.sleep(2)





import mechanize
bit = platform.architecture()[0]
if bit == '64bit':
    import arch64
    BRAND64.ff()
elif bit == '32bit':
    import arch64
    BRAND.ff()
