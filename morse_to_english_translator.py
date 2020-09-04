from english_to_morse_translator import MORSE_CODE_DICT
import re

def decrypt_message(message):
    word = ''
    letter = ''
    sentence = ''
    space = 1
    vals = MORSE_CODE_DICT.values()
    keys = MORSE_CODE_DICT.keys()
    new_dict = dict(zip(vals,keys))
    for symbol in message:
        if not symbol.isspace():
            letter += symbol
            space = 1
        else:
            if space == 1:
                word += new_dict[letter]
                letter = ''
                space += 1
            elif space == 2:
                space = 1
                sentence += word+" "
                word = ''
    return sentence+word

file = open('code.txt','r')
output = open('decode.txt','w')
# print(' '.join(file.read().splitlines()))
# file.seek(0)
res = decrypt_message(' '.join(file.read().splitlines()))
res = re.split('(?<=[.!?]) +',res)
# " ".join([sentence.capitalize() for sentence in res])
output.write(" ".join([sentence.capitalize() for sentence in res]))
file.close()
output.close()




