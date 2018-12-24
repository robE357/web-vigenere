import caesar

def alphabet_position(letter):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if letter.isalpha():
        letter = letter.lower()
        return alphabet.index(letter)
    elif letter.isdigit():
        return int(letter) % 26        
    else:
        return 0 
def rotate_character(char, rot):
    
    # define alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    #Get new postion:
    if char.isupper():
        if char.lower() in alphabet:
            new_position = (alphabet_position(char) + rot) % 26
            #print("The character [{}], was rotated {} times!".format(char,rot))
            return alphabet[new_position].upper()
    elif char in alphabet:
        new_position = (alphabet_position(char) + rot) % 26
        #print("The character [{}], was rotated {} times!".format(char,rot))
        return alphabet[new_position]
    else:
        return char

def unrotate_character(char, rot):
    
    # define alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    #Get new postion:
    if char.isupper():
        if char.lower() in alphabet:
            new_position = (alphabet_position(char) - rot) % 26
            #print("The character [{}], was rotated {} times!".format(char,rot))
            return alphabet[new_position].upper()
    elif char in alphabet:
        new_position = (alphabet_position(char) - rot) % 26
        #print("The character [{}], was rotated {} times!".format(char,rot))
        return alphabet[new_position]
    else:
        return char

def encrypt(text,key_txt):
    #print("*" * 10,"\n")
    keyTxtLength = len(key_txt)
    encryptedMessage = ""
    count = 0
    if keyTxtLength == 0:
        count = 0

    for i in range(len(text)):
        if text[i].isalpha():
            encryptedChar = rotate_character(text[i],alphabet_position(key_txt[count % keyTxtLength]))
            encryptedMessage += encryptedChar
            count += 1
        else:
            encryptedMessage += text[i]
            #print("The character [{}], was not rotated!".format(text[i]))
    return encryptedMessage

def decrypt(text,key_txt):
    #print("*" * 10,"\n")
    keyTxtLength = len(key_txt)
    decryptedMessage = ""
    count = 0
    if keyTxtLength == 0:
        count = 0

    for i in range(len(text)):
        if text[i].isalpha():
            decryptedChar = unrotate_character(text[i],alphabet_position(key_txt[count % keyTxtLength]))
            decryptedMessage += decryptedChar
            count += 1
        else:
            decryptedMessage += text[i]
            #print("The character [{}], was not unrotated!".format(text[i]))
    return decryptedMessage


def main():
    choice = input("Do you want to [e]ncrypt or [d]ecrypt a message?:")
    if choice.isalpha():
        choice = choice.lower()
        if choice == 'd':
            print(decrypt(input("Provide the encrypted message:\n"),input("\nProvide the key: ")))
            print('*'*10,'\n')
        elif choice == 'e':
            print(encrypt(input("Type a message:\n"),input("\nProvide the key: ")))
            print('*'*10,'\n')    
        else:
            return "Invalid Input!"
    else:
        return "Invalid Input!"
    

if __name__ == '__main__':
    main()

