# Soal 3
'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar.
It encrypts letters by shifting them over by a certain number of places in the alphabet. 
We call the length of shift the *key*. For example, if the key is 4, 
then *A* becomes *E*, *B* becomes *F*, *C* becomes *G*, and so on. 
To decrypt the message, you must shift the encrypted letters in the opposite direction. 
This program lets the user encrypt and decrypt messages according to this algorithm.

Your solution is correct if the following output are all similar:

input: 'Meet me by the rose bushes tonight.'
output: 'QIIX QI FC XLI VSWI FYWLIW XSRMKLX.'
'''

# fungsi encrypt
def encrypt():
    '''ini adalah fungsi enkripsi

    Return:
        result (str): hasil dari enkripsi (text dengan format baru sesuai key yang diinput)
    '''
    result = ''
    for i in range(len(text)):
        letter = text[i].upper()
        if letter in alphabet:
            seq = alphabet.find(letter.upper())            
            seq += key
            if seq >= len(alphabet):
                seq %= len(alphabet)
            letter = alphabet[seq]
        result += f'{letter}'
    return result

# fungsi decrypt
def decrypt():
    '''ini adalah fungsi dekripsi

    Return:
        result (str): hasil dari dekripsi
    '''
    result = ''
    for i in range(len(outputEnc)):
        letter = outputEnc[i].upper()
        if letter in alphabet:
            seq = alphabet.find(letter.upper())            
            seq -= key
            if seq < 0:
                seq += len(alphabet)
            letter = alphabet[seq]
        result += f'{letter}'
    return result


if __name__ == "__main__":
    key = int(input('input key: '))
    text = 'Meet me by the rose bushes tonight.'

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    outputEnc = encrypt()
    outputDec = decrypt()

    print(f'Txt: {text}')
    print(f'Enc: {outputEnc}')
    print(f'Dec: {outputDec}')