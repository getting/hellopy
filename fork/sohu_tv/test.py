from hashlib import sha1

print(sha1(b'aaa').hexdigest())
print(sha1(b'aaa').hexdigest())
print(sha1(b'aba').hexdigest())
print(sha1('aaa'.encode()).hexdigest())


