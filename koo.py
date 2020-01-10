low_alphabet = 'abcdefghijklmnopqrstuvwxyz'
start = input('mode 입력 : ')
message = input('message 입력 : ')
key = int(input('key 입력 : '))


def encrpyt():
    a = ''
    for i in message.lower():
        a += low_alphabet[(low_alphabet.find(i)+key)%26]
    print(a.upper())
def decrpyt():
    a = ''
    for i in message.lower():
        a += low_alphabet[(low_alphabet.find(i)-key)%26]
    print(a.lower())
    
if start =='e':
    encrpyt()
elif start =='d':
    decrpyt()
