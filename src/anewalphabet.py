# https://open.kattis.com/problems/anewalphabet

D = {"A": "@", "B": "8", "C": "(", "D": "|)", "E": "3","F": "#", "G": "6", "H": "[-]", "I": "|", "J": "_|", "K": "|<", "L": "1", "M": "[]\\/[]", "N": "[]\\[]", "O": "0", "P": "|D", "Q": "(,)", "R": "|Z", "S": "$", "T": "']['", "U": "|_|", "V": "\\/", "W": "\\/\\/", "X": "}{", "Y": "`/", "Z": "2"}

print((lambda x: ''.join([D[chr(ord(c) - 32)] if 97 <= ord(c) <= 122 else D[c] if 65 <= ord(c) <= 90 else c for c in x]))(input()))
