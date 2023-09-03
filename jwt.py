import jwt
from secret_key import SECRET_KEY

def generate_token(payload):
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

if __name__ == "__main__":
    data = {
        "email": "recipient@example.com",
        # Add other data as necessary
    }
    token = generate_token(data)
    print(f"Generated token: {token}")