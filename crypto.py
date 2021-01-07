from math import ceil

def chaveCrypto(chave):
    for i in range(1):
        chave2 = ''

        for x in chave:
            if (x.isalpha() == True):
                chave2 += chr(ord(x) + 3)
            else:
                chave2 += x

        chave3 = chave2[::-1]
        s = ceil(len(chave3)/2)
        chave4 = chave3[-s:]
        chave5 = ''

        for y in chave4:
            chave5 += chr(ord(y) - 1)

        chavefinal = chave3.replace(chave4, chave5)
        return chavefinal
