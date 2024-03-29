def output(cipherText):
    return hex(cipherText)[2:].upper()

def FeistelFunction(plainText,key):
    return hex((plainText+key)%65536)[2:]

    keyArr = [int(a,16) for a in hex(key)[2:]]
    cipherText = ''
    print(keyArr)
    for i,hexNum in enumerate([int(a,16) for a in hex(plainText)[2:]]):
        # print(hex(hexNum+keyArr[i]))
        cipherText += hex(hexNum+keyArr[i])[2:]
        
    return cipherText

def FeistelFunctionSwitch(L,R,key=0):
    newL = R
    newR = L ^ int(FeistelFunction(R,key),16)

    return [newL,newR]

def main():
    plainText = open("inputEncode.txt")
    L = int(plainText.readline(),16)
    R = int(plainText.readline(),16)
    plainText.close()

    with open("keys.txt") as f:
        keys = [int(a,16) for a in f.read().splitlines()]
    f.close()

    print("Keys: " + str([hex(key)[2:].upper()for key in keys]))
    print("Plaintext: {} {}".format(output(L),output(R)))

    for i,key in enumerate(keys):
        # cipherText = FeistelFunction(L,key)
        L,R = FeistelFunctionSwitch(L,R,key)
        # print("\nRound {}: {} {}".format(i+1,FeistelFunction(L,key).upper(),output(R)))

        print("Round {}: {} {}".format(i+1,output(L),output(R)))
    print("Ciphertext: {} {}".format(output(R),output(L)))


if __name__ == '__main__':
    main()


