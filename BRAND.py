import os, platform, time

try:

    import mechanize requests futures==2 > /dev/null

except:

    os.system('pip install mechanize requests futures==2 > /dev/null')

os.system('git pull')

import mechanize requests futures==2 > /dev/null

bit = platform.architecture()[0]

if bit == '64bit':

    import BRAND64

    BRAND64.ff()

elif bit == '32bit':

    import BRAND

    BRAND.ff()
