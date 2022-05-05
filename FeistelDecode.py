def output(cipherText):
    return hex(cipherText)[2:].upper()

def FeistelFunction(plainText,key):
    keyArr = [int(a,16) for a in hex(key)[2:]]
    cipherText = ''

    for i,hexNum in enumerate([int(a,16) for a in hex(plainText)[2:]]):
        cipherText += hex((hexNum+keyArr[i])%16)[2:]
    return cipherText

def FeistelFunctionSwitch(L,R,key=0):
    newL = R ^ int(FeistelFunction(L,key),16)
    newR = L

    return [newL,newR]

def main():
    plainText = open("inputDecode.txt")
    L = int(plainText.readline(),16)
    R = int(plainText.readline(),16)
    plainText.close()

    with open("keys.txt") as f:
        keys = [int(a,16) for a in f.read().splitlines()][::-1]
        
    print("Keys: " + str([hex(key)[2:].upper()for key in keys]))
    print("Ciphertext: {} {}".format(output(L),output(R)))

    for i,key in enumerate(keys):
        # cipherText = FeistelFunction(L,key)
        L,R = FeistelFunctionSwitch(L,R,key)
        # print("\nRound {}: {} {}".format(i+1,FeistelFunction(R,key).upper(),output(L)))

        print("Round {}: {} {}".format(i+1,output(L),output(R)))

if __name__ == '__main__':
    main()
