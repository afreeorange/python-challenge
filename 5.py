# coding: utf-8

# http://www.pythonchallenge.com/pc/def/peak.html
# "Peak Hill" = pickle, not pkill... :|

import pickle

pickled_banner = open('5.banner.p', 'r')

p = pickle.load(pickled_banner)

for _ in p:
    print ''.join(char * count for char, count in _)

