n1 = '\u25E7\u25E7\u25E7\u25E7\u25E7 '
n2 = '\u25E7   \u25E7 '
n3 = '\u25E7\u25E7\u25E7   ' 
n4 = '  \u25E7   '
n5 = '   \u25E7  '
n6 = ' \u25E7    '
n7 = '\u25E7     '
n8 = '    \u25E7 '
n9 = '      '

uni = {
    '0': (n1, n2, n2, n2, n2, n2, n1),
    '1': (n3, n4, n4, n4, n4, n4, n1),
    '2': (n1, n8, n8, n1, n7, n7, n1),
    '3': (n1, n8, n8, n1, n8, n8, n1),
    '4': (n2, n2, n2, n1, n8, n8, n8),
    '5': (n1, n7, n7, n1, n8, n8, n1),
    '6': (n1, n7, n7, n1, n2, n2, n1),
    '7': (n1, n8, n8, n8, n8, n8, n8),
    '8': (n1, n2, n2, n1, n2, n2, n1),
    '9': (n1, n2, n2, n1, n8, n8, n1)
}
def blink():
    count = 0
    r_with = '  \u25E7\u25E7   '
    r_without = '       '
    while True:
        sp = [r_with if i == count else r_without for i in range(7)]
        yield sp
        if count<6:
            count += 1
        else: 
            count = 0
gen_separ = blink()

# digts elements
