import os

div1_fp = os.path.expanduser('~/cltk_data/latin/text/latin_text_latin_library/cicero/divinatione1.txt')
div2_fp = os.path.expanduser('~/cltk_data/latin/text/latin_text_latin_library/cicero/divinatione2.txt')

with open(div1_fp) as fo:
    div1 = fo.read()

with open(div2_fp) as fo:
    div2 = fo.read()

print(div1[500:1500])