from Crypto.PublicKey import RSA
from Crypto.Util.number import *

#CRYPTOHACK: PRIVACY-ENHANCED MAIL? and SSH KEYS
file = open('test.pem','r')
#file = open('bruce_rsa.pub', 'r') #TODO: note that .pub files can be renamed to pem files
out = RSA.importKey(file.read())

print(out.e)
print(out.n)
print(out.d)




#CRYPTOHACK: CERTAINLY NOT
#openssl x509 -in cert.der -inform der -noout -text

'''
lst = ['b4',' cf',' d1',' 5e',' 33',' 29',' ec',' 0b',' cf',' ae',' 76',' f5',' fe',' 2d','c8',' 99',' c6',' 78',' 79',' b9',' 18',' f8',' 0b',' d4',' ba',' b4',' d7',' 9e',' 02',' 52',' 06',' 09',' f4',' 18',' 93',' 4c',' d4',' 70',' d1',' 42',' a0',' 29',' 13',' 92',' 73',' 50',' 77',' f6',' 04',' 89',' ac',' 03',' 2c',' d6',' f1',' 06',' ab',' ad',' 6c',' c0',' d9',' d5',' a6',' ab',' ca',' cd',' 5a',' d2',' 56',' 26',' 51',' e5',' 4b',' 08',' 8a',' af',' cc',' 19',' 0f',' 25',' 34',' 90',' b0',' 2a',' 29',' 41',' 0f',' 55',' f1',' 6b',' 93',' db',' 9d',' b3',' cc',' dc',' ec',' eb',' c7',' 55',' 18',' d7',' 42',' 25',' de',' 49',' 35',' 14',' 32',' 92',' 9c',' 1e',' c6',' 69',' e3',' 3c',' fb',' f4',' 9a',' f8',' fb',' 8b',' c5',' e0',' 1b',' 7e',' fd',' 4f',' 25',' ba',' 3f',' e5',' 96',' 57',' 9a',' 24',' 79',' 49',' 17',' 27',' d7',' 89',' 4b',' 6a',' 2e',' 0d',' 87',' 51',' d9',' 23',' 3d',' 06',' 85',' 56',' f8',' 58',' 31',' 0e',' ee',' 81',' 99',' 78',' 68',' cd',' 6e',' 44',' 7e',' c9',' da',' 8c',' 5a',' 7b',' 1c',' bf',' 24',' 40',' 29',' 48',' d1',' 03',' 9c',' ef',' dc',' ae',' 2a',' 5d',' f8',' f7',' 6a',' c7',' e9',' bc',' c5',' b0',' 59',' f6',' 95',' fc',' 16',' cb',' d8',' 9c',' ed',' c3',' fc',' 12',' 90',' 93',' 78',' 5a',' 75',' b4',' 56',' 83',' fa',' fc',' 41',' 84',' f6',' 64',' 79',' 34',' 35',' 1c',' ac',' 7a',' 85',' 0e',' 73',' 78',' 72',' 01',' e7',' 24',' 89',' 25',' 9e',' da',' 7f',' 65',' bc',' af',' 87',' 93',' 19',' 8c',' db',' 75',' 15',' b6',' e0',' 30',' c7',' 08',' f8',' 59']
lst = ['A2', '2F', '2B', '8D', '80', 'CE', '02', '6B', '48', '81', '8C', '93', 'F6', '88', 'FD', '57', '40', '67', '68', '7A', 'A6', 'DB', '74', '72', '47', '06', 'E1', '23', 'F5', '37', '29', '58', '3E', 'CB', 'C5', '96', '59', 'AD', 'C6', '74', '64', '0D', '99', '07', '07', 'AB', '97', '15', '48', 'AB', '32', 'FD', '71', '55', '97', 'D5', '35', 'E5', '6E', '45', 'DA', 'B9', '21', '03', '70', 'C3', 'C5', 'C5', '21', '56', '5D', 'B3', '17', 'E2', '32', '92', '01', 'B5', 'C8', '13', '90', 'DF', 'EF', '81', '7B', '95', 'E5', '66', 'B6', '80', '24', '7F', '9E', 'A8', '3B', 'DD', '03', 'EE', '46', 'DC', '7E', '1D', '1A', '83', '91', 'ED', '45', 'CE', '5B', '2D', 'E0', 'A5', 'F1', '33', 'DD', '8E', '68', 'B8', '51', '09', 'D3', '7C', '70', 'FF', 'DB', '79', '37', 'EF', '4E', '7A', 'B0', 'A3', '80', '57', 'B7', '4C', '6A', '5F', 'F2', '1A', '75', 'DE', '19', '70', 'BC', 'B6', '09', 'C7', '77', 'C2', 'B4', 'D3', '7E', 'F7', 'B7', '7B', '92', '80', '5E', 'FF', '35', 'FB', 'A0', '89', '5C', '4D', '3C', 'E4', '47', 'B3', '5A', 'D3', '25', '03', '06', 'EA', 'A3', 'FD', '2D', '5D', '27', '48', '57', 'DF', 'D4', '39', 'D5', '83', 'B0', 'DC', '14', '9A', 'AE', '82', 'BB', '4D', 'B0', '3E', 'BC', '5E', '73', '79', 'CD', 'D0', '5F', '49', 'CB', '37', '49', '35', '11', '50', '49', '27', 'D9', 'F8', '58', '61', '48', 'D3', 'E7', 'DC', '43', 'F8', '3C', '99', '4D', 'D0', '1D', '1C', '6F', 'A8', '15', '96', '1A', '8F', 'D2', 'C1', '64', '02', '2B', '99', '2A', '93', '93', 'D3', '93', 'A8', 'A6', '97', 'C2', '97', 'F9', '4D', '7B', '7F']

Nlist = [bytes.fromhex(x) for x in lst]
Nlist = b"".join(Nlist)
print(bytes_to_long(Nlist))
'''
