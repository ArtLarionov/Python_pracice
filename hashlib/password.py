import time
import hashlib
import hmac
import base64

secret_key = base64.b32decode('ABCDEFGHIGKLMNOP')  # заданный секретный ключ (TOTP-key - Time-based one time password)
counter = int(time.time()/30)  # вычисление UNIX-времени

# использование counter как 8-битного массива
bytes1 = bytearray()
for i in reversed(range(0, 8)):
    bytes1.insert(0, counter & 0xff)  # & 0xff - чтобы компилятор не расширял знаковый бит на более широкий тип
    counter >>= 8

# вычисление HMAC-SHA1 - кода аутентификации, использующего хэш-функцию SHA1
hs = bytearray(hmac.new(key=secret_key, msg=bytes1, digestmod=hashlib.sha1).digest())

# усечение результата по стандарту RFC4226
n = hs[-1] & 0xF
print('hs array = ', hs)
print('n=', n)
# распределение по наиболее значимым битам до 0
result = (hs[n] << 24 | hs[n+1] << 16 | hs[n+2] << 8 | hs[n+3]) & 0x7fffffff

print()
password = str(result)[-6:]
print(password)
