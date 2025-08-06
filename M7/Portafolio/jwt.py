from jose import jwt

payload = {"sub":"johndoe", "role":"admin", "exp":1767225600}
secret = "supersecreto123"
algorithm = "HS256"
t = jwt.encode(payload, secret, algorithm=algorithm)

print(t)
