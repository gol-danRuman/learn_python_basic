import configparser
import codecs

import binascii




config = configparser.ConfigParser()

# Please note that using RawConfigParser's set functions, you can assign
# non-string values to keys internally, but will receive an error when
# attempting to write to a file or when you get it in non-raw mode. Setting
# values using the mapping protocol or ConfigParser's set() does not allow
# such assignments to take place.
config.add_section('Section1')
# config.set('Section1', 'an_int', '15')
# config.set('Section1', 'a_bool', 'true')
# config.set('Section1', 'a_float', '3.1415')
config.set('Section1', 'baz', 'fun')
config.set('Section1', 'bar', 'Python')
config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

# Writing our configuration file to 'example.cfg'
# with codecs.open('example.cfg', mode='w', encoding='utf-16') as configfile:
#     # encoded = configfile.encoding()
#     encoding = 'utf-8'
#     config.write(codecs.unicode_internal_encode(configfile, encoding))
    # print(type(configfile))
    # configfile.write(configfile)

# from cryptography.fernet import Fernet
# key = Fernet.generate_key() # Use one of the methods to get a key (it must be the same when decrypting)
# print('Key:: {}'.format(key))
# input_file = 'example.cfg'
# output_file = 'test.encrypted'
#
# with open(input_file, 'rb') as f:
#     data = f.read()
#
# fernet = Fernet(key)
# encrypted = fernet.encrypt(data)
#
# with open(output_file, 'wb') as f:
#     f.write(encrypted)

# from cryptography.fernet import Fernet
# key = b'oKVZ1mUvnramTrXolyErWxUCNsJhjD7sBBMnQyN7XQY=' # Use one of the methods to get a key (it must be the same as used in encrypting)
# input_file = 'test.encrypted'
# output_file = 'test.txt'
#
# with open(input_file, 'rb') as f:
#     data = f.read()
#
# fernet = Fernet(key)
# encrypted = fernet.decrypt(data)
# print('encrypted'+ encrypted.decode("utf-8"))
# with open('test.encrypted','rb') as f:
#     contents = f.read()
# # print(type(contents))
# contents = contents.decode("utf-8")
# print(type(contents))
# # contents = contents.split("\r\n")
# print('decrypt: '+contents)
# print('frenet decrypt: '+ fernet.decrypt(contents))
# print('encrypted file : {}'.format(encrypted))
# with open(output_file, 'wb') as f:
#     # f.write(encrypted)
#     print(type(encrypted))
# config = configparser.RawConfigParser()
# config.read('test.encrypted')
# print('config: '+config.decode())