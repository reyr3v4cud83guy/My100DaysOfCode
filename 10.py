  my_branch
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, from_addr, to_addr, password):
    """
    Sends an email using the provided details.
    
    Args:
        subject (str): The subject of the email.
        message (str): The body of the email.
        from_addr (str): The sender's email address.
        to_addr (str): The recipient's email address.
        password (str): The sender's email password.
    """
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

def main():
    """
    Asks for user input and sends an email using the provided details.
    """
    subject = input("Enter the subject of the email: ")
    message = input("Enter the body of the email: ")
    from_addr = input("Enter your email address: ")
    to_addr = input("Enter the recipient's email address: ")
    password = input("Enter your email password: ")
    
    try:
        send_email(subject, message, from_addr, to_addr, password)
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
=======
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, from_addr, to_addr, password):
    """
    Sends an email using the provided details.
    
    Args:
        subject (str): The subject of the email.
        message (str): The body of the email.
        from_addr (str): The sender's email address.
        to_addr (str): The recipient's email address.
        password (str): The sender's email password.
    """
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

def main():
    """
    Asks for user input and sends an email using the provided details.
    """
    subject = input("Enter the subject of the email: ")
    message = input("Enter the body of the email: ")
    from_addr = input("Enter your email address: ")
    to_addr = input("Enter the recipient's email address: ")
    password = input("Enter your email password: ")
    
    try:
        send_email(subject, message, from_addr, to_addr, password)
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
  Osman--branch
