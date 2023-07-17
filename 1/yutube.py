
def free_urinals(urinals :str)->int:
    if '11' in urinals:
        return -1
    rez=0
    for i in range(len(urinals),2,-1):
        rez+=urinals.count('0'*i)*int((i-1)/2)
        urinals=urinals.replace('0'*i,'')
    return rez

def encryptor(key, message):
    word=''
    # slovar='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    slovar='abcdefghijklmnopqrstuvwxyz'
    print(slovar)

    for ch in message:
        if ch.islower():
            x=slovar.lower().find(ch)
        else: x=slovar.upper().find(ch)
        if ch.lower() in slovar :
            word += chr(ord(ch)+key)
        else:
            word += ch
    # print(chr(ord(ch)+key)+' '+str(ord(ch)+key))
    print(message,word)



# encryptor(13, 'Caesar Cipher')
# encryptor(13, '')
# encryptor(13, 'Caesar Cipher')
# encryptor(-5, 'Hello World!')
# encryptor(27, 'Whoopi Goldberg')
uri='0101000100001000001'
print(uri)
print(free_urinals(uri))