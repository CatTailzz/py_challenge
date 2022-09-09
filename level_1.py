text1 = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''


def decipher(string):
    newstring = ''
    for char in string:
        if char == 'y':
            newstring += 'a'
        elif char == 'z':
            newstring += 'b'
        elif ord(char) >= 97 and ord(char) <= 120:
            newstring += chr(ord(char) + 2)
        else:
            newstring += char
    return newstring


def decipher2(string):
    table = string.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
    return string.translate(table)


print(decipher(text1))

print(decipher2(text1))

print(decipher('map'))

# ocr
