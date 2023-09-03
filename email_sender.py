import smtplib
from verify import verify_token
from secret_key import EMAIL_ADDRESS, EMAIL_PASSWORD

def send_email(subject, to, body):
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to, f"Subject: {subject}\n\n{body}")

if __name__ == "__main__":
    token = input("Enter JWT: ")
    data = verify_token(token)

    subject = "Your Subject Here"
    body = "Your email body here."

    send_email(subject, data['email'], body)
    print("Email sent successfully!")