import random
def dicts():
    letter_key = {
        'a': 'esfihb83q80u09w4gf4',
        'b': 'f57ge45ef15|743565#&($^',
        'c': 'djhf840)E*389iF-30',
        'd': 'D#sesrw44w#$(Tp09',
        'e': 'fj3)*Y9(*@0hd0f8',
        'f': 'df(u9hd8f9i90()*D))######%',
        'g': 'pre-903p9iE)P(O(#@*UH',
        'h': '(*@HDJo3rIS)A',
        'i': 'DS*#QNDSN#Dljldf[800q3i',
        'j': 'df973IUH(&do89ae8d09e-',
        'k': 'SJID)#sa8adf809q',
        'l': 'ud9*&CD)*DASF)*YDFOihwe3',
        'm': 'IUC*&3fSA&d79oq8r3udfu',
        'n': 'yagsygsydygyfgeygdfy@#$#@$#$#',
        'o': 'ftfrdd#%#$#Dtffdre%$$',
        'p': '@#$%@#$%%^^^^^^&&&&***((()qwertyuiop',
        'q': '!@#$%^&*((((()',
        'r': 'ASDFGHJKLLL!@#$%^&*(',
        's': '!@#$%^&ZXCVBNM',
        't': '+_)(*&^%$"?|}{ZXCVB',
        'u': '!@#$%^&*()ZXCVBNM<',
        'v': '^&*()DFGHJVBN',
        'w': '@#$%^&*()ZXCVBNM<',
        'x': 'WRCRASDCFVGYBH!@#$%^&*',
        'y': '@#$%^&*(SDFGHJ',
        'z': 'XCFVGBHNJ@#$%^&*()',
        '`': 'tasyadli!^@%&*E^UOWI',
        '&': 'SDKJ397QShuDL;A9P73QYUhawdp(&#qurO',
        '^': 'S#)*YDIOHP(W*Y##FOHI&AGDIASDO*',
        '*': 'DFOIH083qoni*{)S)iug(U#Q-=',
        ')': 'WOIe93qr3pindpi_)Q#R-U94',
        '(': 'dslkenkn0r*^&T23EBIUHOIS*HFI&C',
        '#': 'SJHD938isdg97a0-2qe-yASOIICU(PUsfs-9bbf',
        '$': 'JDH#*osdpq30rm{f)###$%%@*$^',
        '/': 'JHs@98qoijdffq3-0',
        '|': 'SDLH@(QQEOuhsd0q3r08',
        '<': '(N209fdh89n3wro9N*#)E',
        '>': 'NSD(*Q#N*sa9oduP0q3789Y@*$Q^^^^^^^^',
        '"': 'SD)(@M<D<!WP(WD(',
        "'": 'SDKH#9oisamaP()C@(*DIS29q8qE897r',
        '.': '>DD#)>SDQ@PRsafpindQP#(ELKSD',
        '-': 'Iuu()8iubi97ouu97oUh(*IO&*y9-',
        '_': 'JH97IUH9kjdfhfsef89UHUHsaouy',
        '+': 'Hdfy3qbhds9SDJ@*(Rjsdi%#$Q^^*%#Q%(',
        '=': 'UD)*#ROF)(#UF)SDLJ#R*Jdosad0Rui3qouh',
        ':': 'jDOWIQq933ru09douh38wr4$(&Q#($DSKj397r',
        ' ': '(#*IUdsfmo3w98r(#e*r3'
    }
    return letter_key


letters = [i for i in dicts()]

def random_str():
    char_list = []
    for i in range(10):
        char_list.append(letters[random.randint(0, len(letters) - 1)])
    return ''.join(char_list)


def encode_str(string):
    new_list = []
    for j in string:
        try:
            int(j)
            new_list.append((((j/10)*87)-544)*43)
        except Exception as e:
            new_list.append(dicts()[j] + '~~')
    new_list.append('--------++++++++========')

    return ''.join(new_list)


def decode_str(string):
    new_list = []
    chars = string.split('~~')
    for j in chars:
        if j != '--------++++++++========':
            try:
                int(j)
                new_list.append((((j / 43) + 544) / 84) * 10)
            except Exception as e:
                new_list.append(list(dicts().keys())[list(dicts().values()).index(j)])

    return ''.join(new_list)

