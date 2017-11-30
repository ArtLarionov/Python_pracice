def trans(char):
    '''Translate a letter as the one two places after it'''
    if char.isalpha():
        return chr((ord(char)- ord('a') + 2)%26 + ord('a'))
    return char

if __name__ == '__main__':
    text = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. '''
    print(''.join(map(trans, text)))