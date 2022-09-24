import os, platform, time

try:

    import mechanize

except:

    os.system('pip install mechanize')

os.system('git pull')

import mechanize

bit = platform.architecture()[0]

if bit == '64bit':

    import BRAND64

    BRAND64.ff()

elif bit == '32bit':

    import BRAND

    BRAND.ff()
