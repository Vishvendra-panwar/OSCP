#Enhanced with thanks to Dinesh Singh Sikawar @LinkedIn
import base64,codecs,sys

def encodeString(str):
    decode = codecs.decode(str[::-1], 'rot13')
    return base64.b64decode(decode) 

cryptoResult=encodeString(sys.argv[1])
print cryptoResult
