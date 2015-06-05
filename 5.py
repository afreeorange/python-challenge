# http://www.pythonchallenge.com/pc/def/peak.html
from time import sleep
import sys

with open('5.banner.p') as f:
    banner = [_.strip() for _ in f.readlines()]

# while True:
#     for _ in banner:
#         sys.stdout.write(_)