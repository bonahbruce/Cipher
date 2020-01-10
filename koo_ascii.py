

start = input('mode 입력 : ')
message = input('message 입력 : ')
key = int(input('key 입력 : '))
a = ''

# a~z 는 97~122
# A~Z 는 65~90

if start == 'e': #e를 받으면 소문자에서 대문자로 치환하면서 +key 로 어지러뜨린다.
    for i in message:
        if 65+((ord(i)+7)%26)+key>90: # 65~90 사이 숫자를 받아야한다. 근데 97보다 작은 값이 나올 수 있다. 
                                      # 그때의 예외처리다.
            a += chr(65+((ord(i)+7)%26)+key-26) 
        else:
            a += chr(65+((ord(i)+7)%26)+key) # 7을 더해서 26으로 나눔으로써 a~z값의 나머지를 0~25로 바꿈.
                                             # 다시 65를 더함으로써 본 위치로 출력
            
    print(a)
elif start == 'd': #d를 받으면 대문자에서 소문자로 치환하면서 -key 암호를 다시 가져온다.
    for i in message:
        if 97+(ord(i)+13)%26-key<97:# 97~122 사이 숫자를 받아야한다. 근데 97보다 작은 값이 나올 수 있다. 
                                    # 그때의 예외처리다.
            a += chr(97+(ord(i)+13)%26-key+26) 
        else:
            a += chr(97+(ord(i)+13)%26-key) # 13을 더해서 26으로 나눔으로써 A~Z값의 나머지를 0~25로 바꿈.
                                            # 다시 97을 더함으로써 본 위치로 출력
            
    print(a)
