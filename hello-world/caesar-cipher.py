def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
    

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
    
    
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount

# Take three arguments: the message, the cipherKey, and the alphabet.
def encryptMessage(message, cipherKey, alphabet):
    # Initialize variables.
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    
    # Use a for loop to traverse each letter in the message.
    for currentCharacter in uppercaseMessage:
        # For a specific letter, find the position.
        position = alphabet.find(currentCharacter)
        # For a specific letter, determine the new position given the cipher key.
        newPosition = position + int(cipherKey)
        # If current letter is in the alphabet, append the new letter to the encrypted message.
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
        # If current letter is not in the alphabet, append the current letter.
            encryptedMessage = encryptedMessage + currentCharacter
    # Return the encrypted message after exhausting all the letters in the message.
    return encryptedMessage

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
    
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')


runCaesarCipherProgram()





