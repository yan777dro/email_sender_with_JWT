import jwt
from secret_key import SECRET_KEY

def verify_token(token):
    return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

if __name__ == "__main__":
    token = input("Enter JWT to verify: ")
    data = verify_token(token)
    print(f"Decoded data: {data}")