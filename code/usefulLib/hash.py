import hashlib

#md5
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# splite long string to several strings
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8')) 
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# sha1
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

# password hash
password = "pass"
salt = "salt_TXT"
md5 = hashlib.md5()
md5.update(password.encode('utf-8'))
md5.update(salt.encode('utf-8'))
hashed = md5.hexdigest()
print("hashed pass with salt --->>> " + hashed)


# login autherization
md5 = hashlib.md5()
md5.update(password.encode('utf-8'))
md5.update(salt.encode('utf-8'))
if(hashed == md5.hexdigest()):
    print("login success")
else:
    print("login failed")
