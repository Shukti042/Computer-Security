from collections import deque
from BitVector import *
import math
import time
AES_modulus = BitVector(bitstring='100011011')
mixer=[["02", "03", "01", "01"],["01", "02","03","01"],["01","01", "02","03"],["03","01","01","02"]]
invMixer=[["0e", "0b", "0d", "09"],["09", "0e","0b","0d"],["0d","09", "0e","0b"],["0b","0d","09","0e"]]
# sbox=[["63", "7c", "77", "7b", "f2", "6b", "6f", "c5", "30", "01", "67", "2b", "fe", "d7", "ab", "76"],
#     ["ca", "82", "c9", "7d", "fa", "59", "47", "f0", "ad", "d4", "a2", "af", "9c", "a4", "72", "c0"],
#     ["b7", "fd", "93", "26", "36", "3f", "f7", "cc", "34", "a5", "e5", "f1", "71", "d8", "31", "15"],
#     ["04", "c7", "23", "c3", "18", "96", "05", "9a", "07", "12", "80", "e2", "eb", "27", "b2", "75"],
#     ["09", "83", "2c", "1a", "1b", "6e", "5a", "a0", "52", "3b", "d6", "b3", "29", "e3", "2f", "84"],
#     ["53", "d1", "00", "ed", "20", "fc", "b1", "5b", "6a", "cb", "be", "39", "4a", "4c", "58", "cf"],
#     ["d0", "ef", "aa", "fb", "43", "4d", "33", "85", "45", "f9", "02", "7f", "50", "3c", "9f", "a8"],
#     ["51", "a3", "40", "8f", "92", "9d", "38", "f5", "bc", "b6", "da", "21", "10", "ff", "f3", "d2"],
#     ["cd", "0c", "13", "ec", "5f", "97", "44", "17", "c4", "a7", "7e", "3d", "64", "5d", "19", "73"],
#     ["60", "81", "4f", "dc", "22", "2a", "90", "88", "46", "ee", "b8", "14", "de", "5e", "0b", "db"],
#     ["e0", "32", "3a", "0a", "49", "06", "24", "5c", "c2", "d3", "ac", "62", "91", "95", "e4", "79"],
#     ["e7", "c8", "37", "6d", "8d", "d5", "4e", "a9", "6c", "56", "f4", "ea", "65", "7a", "ae", "08"],
#     ["ba", "78", "25", "2e", "1c", "a6", "b4", "c6", "e8", "dd", "74", "1f", "4b", "bd", "8b", "8a"],
#     ["70", "3e", "b5", "66", "48", "03", "f6", "0e", "61", "35", "57", "b9", "86", "c1", "1d", "9e"],
#     ["e1", "f8", "98", "11", "69", "d9", "8e", "94", "9b", "1e", "87", "e9", "ce", "55", "28", "df"],
#     ["8c", "a1", "89", "0d", "bf", "e6", "42", "68", "41", "99", "2d", "0f", "b0", "54", "bb", "16"]]
# invSbox = [["52", "09", "6a", "d5", "30", "36", "a5", "38", "bf", "40", "a3", "9e", "81", "f3", "d7", "fb"],
#     ["7c", "e3", "39", "82", "9b", "2f", "ff", "87", "34", "8e", "43", "44", "c4", "de", "e9", "cb"],
#     ["54", "7b", "94", "32", "a6", "c2", "23", "3d", "ee", "4c", "95", "0b", "42", "fa", "c3", "4e"],
#     ["08", "2e", "a1", "66", "28", "d9", "24", "b2", "76", "5b", "a2", "49", "6d", "8b", "d1", "25"],
#     ["72", "f8", "f6", "64", "86", "68", "98", "16", "d4", "a4", "5c", "cc", "5d", "65", "b6", "92"],
#     ["6c", "70", "48", "50", "fd", "ed", "b9", "da", "5e", "15", "46", "57", "a7", "8d", "9d", "84"],
#     ["90", "d8", "ab", "00", "8c", "bc", "d3", "0a", "f7", "e4", "58", "05", "b8", "b3", "45", "06"],
#     ["d0", "2c", "1e", "8f", "ca", "3f", "0f", "02", "c1", "af", "bd", "03", "01", "13", "8a", "6b"],
#     ["3a", "91", "11", "41", "4f", "67", "dc", "ea", "97", "f2", "cf", "ce", "f0", "b4", "e6", "73"],
#     ["96", "ac", "74", "22", "e7", "ad", "35", "85", "e2", "f9", "37", "e8", "1c", "75", "df", "6e"],
#     ["47", "f1", "1a", "71", "1d", "29", "c5", "89", "6f", "b7", "62", "0e", "aa", "18", "be", "1b"],
#     ["fc", "56", "3e", "4b", "c6", "d2", "79", "20", "9a", "db", "c0", "fe", "78", "cd", "5a", "f4"],
#     ["1f", "dd", "a8", "33", "88", "07", "c7", "31", "b1", "12", "10", "59", "27", "80", "ec", "5f"],
#     ["60", "51", "7f", "a9", "19", "b5", "4a", "0d", "2d", "e5", "7a", "9f", "93", "c9", "9c", "ef"],
#     ["a0", "e0", "3b", "4d", "ae", "2a", "f5", "b0", "c8", "eb", "bb", "3c", "83", "53", "99", "61"],
#     ["17", "2b", "04", "7e", "ba", "77", "d6", "26", "e1", "69", "14", "63", "55", "21", "0c", "7d"]]
def rowToCol(mat):
      cols=len(mat[0])
      newMat=[[] for i in range(cols)]
      for i in range(len(mat)):
            for j in range(len(mat[i])):
                  newMat[j].append(mat[i][j])
      return newMat
def pad0toOneDigit(str):
      if(len(str)==1):
            str="0"+str
      return str
def bitWiseXOR(a,b):
      cols=len(a)
      c=[[] for i in range(cols)]
      for i in range(cols):
            for j in range(cols):
                  entry = (hex(int(a[i][j], 16) ^ int(b[i][j], 16)))[2:]
                  if len(entry) == 1:
                        entry = "0" + entry
                  c[i].append(entry)
      return c
def generateKey(key):
      keyMat = [[] for i in range(4)]
      for i in range(0, len(key)):
            keyMat[i // 4].append(key[i].encode('utf-8').hex())
      roundConst = ['01', '00', '00', '00']
      for round in range(1, 11):
            temp = deque(keyMat[(round * 4) - 1])
            temp.rotate(-1)
            temp = list(temp)
            keyMat.append([])
            for i in range(4):
                  temp[i] = sbox[int(temp[i][0], 16)][int(temp[i][1], 16)]
                  temp[i] = (hex(int(temp[i], 16) ^ int(roundConst[i], 16)))[2:]
                  entry = (hex(int(temp[i], 16) ^ int(keyMat[(round - 1) * 4][i], 16)))[2:]
                  if len(entry) == 1:
                        entry = "0" + entry
                  keyMat[round * 4].append(entry)
            keyMat.append([])
            for i in range(4):
                  entry = (hex(int(keyMat[(round - 1) * 4 + 1][i], 16) ^ int(keyMat[round * 4][i], 16)))[2:]
                  if len(entry) == 1:
                        entry = "0" + entry
                  keyMat[round * 4 + 1].append(entry)
            keyMat.append([])
            for i in range(4):
                  entry = (hex(int(keyMat[(round - 1) * 4 + 2][i], 16) ^ int(keyMat[round * 4 + 1][i], 16)))[2:]
                  if len(entry) == 1:
                        entry = "0" + entry
                  keyMat[round * 4 + 2].append(entry)
            keyMat.append([])
            for i in range(4):
                  entry = (hex(int(keyMat[(round - 1) * 4 + 3][i], 16) ^ int(keyMat[round * 4 + 2][i], 16)))[2:]
                  if len(entry) == 1:
                        entry = "0" + entry
                  keyMat[round * 4 + 3].append(entry)
            roundConst[0] = BitVector(hexstring=roundConst[0]).gf_multiply_modular(BitVector(hexstring="02"),AES_modulus,8).get_bitvector_in_hex()
      return keyMat
def substituteSbox(mat):
      for i in range(len(mat)):
            for j in range(len(mat)):
                  mat[i][j]=sbox[int(mat[i][j][0], 16)][int(mat[i][j][1], 16)]
def invSubstituteSbox(mat):
      for i in range(len(mat)):
            for j in range(len(mat)):
                  mat[i][j]=invSbox[int(mat[i][j][0], 16)][int(mat[i][j][1], 16)]
def shiftRow(mat):
      for i in range(len(mat)):
            temp = deque(mat[i])
            temp.rotate(-1 * i)
            temp = list(temp)
            mat[i]=temp
def invShiftRow(mat):
      for i in range(len(mat)):
            temp = deque(mat[i])
            temp.rotate(i)
            temp = list(temp)
            mat[i]=temp
def mixColumns(mat):
      mixedMat=[[] for i in range(4)]
      for i in range(len(mat)):
            for j in range(len(mat)):
                  first=BitVector(hexstring=mixer[i][0]).gf_multiply_modular(BitVector(hexstring=mat[0][j]),AES_modulus,8).get_bitvector_in_hex()
                  second=BitVector(hexstring=mixer[i][1]).gf_multiply_modular(BitVector(hexstring=mat[1][j]),AES_modulus,8).get_bitvector_in_hex()
                  third= BitVector(hexstring=mixer[i][2]).gf_multiply_modular(BitVector(hexstring=mat[2][j]),AES_modulus, 8).get_bitvector_in_hex()
                  fourth=BitVector(hexstring=mixer[i][3]).gf_multiply_modular(BitVector(hexstring=mat[3][j]),AES_modulus,8).get_bitvector_in_hex()
                  temp=(hex(int(first, 16) ^ int(second, 16) ^int(third,16)^int(fourth,16)))[2:]
                  temp=pad0toOneDigit(temp)
                  mixedMat[i].append(temp)
      return mixedMat
def invMixColumns(mat):
      mixedMat=[[] for i in range(4)]
      for i in range(len(mat)):
            for j in range(len(mat)):
                  first=BitVector(hexstring=invMixer[i][0]).gf_multiply_modular(BitVector(hexstring=mat[0][j]),AES_modulus,8).get_bitvector_in_hex()
                  second=BitVector(hexstring=invMixer[i][1]).gf_multiply_modular(BitVector(hexstring=mat[1][j]),AES_modulus,8).get_bitvector_in_hex()
                  third= BitVector(hexstring=invMixer[i][2]).gf_multiply_modular(BitVector(hexstring=mat[2][j]),AES_modulus, 8).get_bitvector_in_hex()
                  fourth=BitVector(hexstring=invMixer[i][3]).gf_multiply_modular(BitVector(hexstring=mat[3][j]),AES_modulus,8).get_bitvector_in_hex()
                  temp=(hex(int(first, 16) ^ int(second, 16) ^int(third,16)^int(fourth,16)))[2:]
                  temp=pad0toOneDigit(temp)
                  mixedMat[i].append(temp)
      return mixedMat
def encript(inputStringMat,keyMat):
      currenRoundtKey = rowToCol(keyMat[:4])
      inputStringMat = bitWiseXOR(currenRoundtKey, inputStringMat)
      for i in range(1, 11):
            substituteSbox(inputStringMat)
            shiftRow(inputStringMat)
            if i != 10:
                  inputStringMat = mixColumns(inputStringMat)
            currenRoundtKey = rowToCol(keyMat[i * 4:(i + 1) * 4])
            inputStringMat = bitWiseXOR(currenRoundtKey, inputStringMat)
      return inputStringMat
def decript(inputStringMat,keyMat):
      currenRoundtKey = rowToCol(keyMat[40:])
      inputStringMat = bitWiseXOR(currenRoundtKey, inputStringMat)
      for i in range(10, 0,-1):
            invShiftRow(inputStringMat)
            invSubstituteSbox(inputStringMat)
            currenRoundtKey = rowToCol(keyMat[(i-1) * 4:i*4])
            inputStringMat = bitWiseXOR(currenRoundtKey, inputStringMat)
            if i != 1:
                  inputStringMat = invMixColumns(inputStringMat)
      return inputStringMat
#main code from here
sbox=[[] for i in range(16)]
for i in range(16):
    for j in range(16):
        a = BitVector(hexstring=hex(i)[2:]+hex(j)[2:])
        if i==0 and j==0:
            b="00"
        else:
            b = a.gf_MI(AES_modulus, 8)
            b = b.get_bitvector_in_hex()
        b = int(b, 16)
        b = b & 255
        b = b ^ (((b << 1) | (b >> 7)) & 255) ^ (((b << 2) | (b >> 6)) & 255) ^ (((b << 3) | (b >> 5)) & 255) ^ (((b << 4) | (b >> 4)) & 255) ^ 99
        b=hex(b)[2:]
        if len(b)==1:
            b="0"+b
        sbox[i].append(b)
invSbox=[[] for i in range(16)]
for i in range(16):
    for j in range(16):
        b=hex(i)[2:]+hex(j)[2:]
        b = int(b, 16)
        b = b & 255
        b = (((b << 1) | (b >> 7)) & 255) ^ (((b << 3) | (b >> 5)) & 255) ^ (((b << 6) | (b >> 2)) & 255) ^ 5
        b=hex(b)[2:]
        if(b!="0"):
            b=BitVector(hexstring=b)
            b = b.gf_MI(AES_modulus, 8)
            b = b.get_bitvector_in_hex()
        if len(b)==1:
            b="0"+b
        invSbox[i].append(b)
print("Plain Text : ")
key=input("Key : ")
print(key.encode('utf-8').hex())
key=key+"000000000000000"
key=key[:16]
inputString=input("Text : ")
print(inputString.encode('utf-8').hex())
steps=math.ceil(len(inputString)/16)
primaryInputString=inputString+"               "
start1=time.time()
keyMat=generateKey(key)
keyGenerationTime=time.time()-start1
finalInputStringMat=[]
start2=time.time()
for s in range(steps):
    inputStringMat = [[] for i in range(4)]
    inputString=primaryInputString[s*16:(s+1)*16]
    for i in range(0, len(key)):
          inputStringMat[i % 4].append(inputString[i].encode('utf-8').hex())
    finalInputStringMat=finalInputStringMat+encript(inputStringMat,keyMat)
encryptionTime=time.time()-start2
cypheredtext=""
cypheredtexthex=""
for i in range(len(finalInputStringMat)):
    for j in range(len(finalInputStringMat[i])):
        cypheredtext = cypheredtext + (chr(int(finalInputStringMat[j][i], 16)))
        cypheredtexthex=cypheredtexthex+finalInputStringMat[j][i]
print()
print("Cipher Text : ")
print(cypheredtexthex)
print(cypheredtext)
steps=len(finalInputStringMat)//4
decodedString=""
decodedStringhex=""
start3=time.time()
for s in range(steps):
    inputStringMat=finalInputStringMat[s*4:(s+1)*4]
    inputStringMat=decript(inputStringMat,keyMat)
    for i in range(len(inputStringMat)):
          for j in range(len(inputStringMat[i])):
                decodedString=decodedString+(chr(int(inputStringMat[j][i],16)))
                decodedStringhex=decodedStringhex+inputStringMat[j][i]
decryptionTime=time.time()-start3
print()
print("Deciphered Text:")
print(decodedStringhex)
print(decodedString)
print()
print("Execution Time")
print("Key Scheduling : ",keyGenerationTime)
print("Encryption Time : ",encryptionTime)
print("Decryption Time : ",decryptionTime)
print()
print("Encrypting 'demo.jpg' And Decrypting to 'copy.jpg'")
file = open("demo.jpg", "rb")
hexfile=[]
byte = file.read(1)
while byte:
    temp = byte.hex()
    hexfile.append(temp)
    byte = file.read(1)
file.close()
pad=16-(len(hexfile) % 16)
hexfile=hexfile+["20" for i in range(pad)]
steps= len(hexfile) // 16
finalInputStringMat=[]
for s in range(steps):
    inputStringMat = [[] for i in range(4)]
    for i in range(16):
          inputStringMat[i % 4].append(hexfile[16*s+i])
    finalInputStringMat=finalInputStringMat+encript(inputStringMat,keyMat)
f = open('copy.jpg','wb')
steps=len(finalInputStringMat)//4
for s in range(steps):
    inputStringMat=finalInputStringMat[s*4:(s+1)*4]
    inputStringMat=decript(inputStringMat,keyMat)
    for i in range(len(inputStringMat)):
          for j in range(len(inputStringMat[i])):
              f.write(byte.fromhex(inputStringMat[j][i]))
f.close()