# http://www.pythonchallenge.com/pc/def/map.html

import string

text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
cipher_offset = 2
translator = string.maketrans(string.ascii_lowercase, string.ascii_lowercase[cipher_offset:] + string.ascii_lowercase[:cipher_offset])

print text.translate(translator)
