# coding: utf-8

# http://www.pythonchallenge.com/pc/def/linkedlist.html

import requests
import re
import sys

nothing = 12345
if sys.argv[1]:
    nothing = sys.argv[1]

while True:
    r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(nothing))
    try:
        nothing = re.findall(r'.*and the next nothing is (\d+)', r.text)[0]
    except Exception:
        sys.exit()
    finally:
        print r.text
