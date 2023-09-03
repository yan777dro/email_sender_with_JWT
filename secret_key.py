"""
create virtual environment and install packages

python -m venv email_jwt_env
source email_jwt_env/bin/activate  # On Windows: email_jwt_env\Scripts\activate
pip install pyjwt smtplib


to run program:

python email_sender.py
"""


SECRET_KEY = "YOUR_SECRET_KEY"  # Make sure this is kept secret
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD = "your_password"