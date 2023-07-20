import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def mailkaro():
# Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "aakashagrawal2710@gmail.com" #use your mail ID over here
    smtp_password = "" #use your smtp password through google
    smtp_tls = True

    # Create the message
    msg = MIMEMultipart()
    msg["From"] = smtp_username
    msg["To"] = "aakashagrawal2710@gmail.com"
    msg["Subject"] = "Question Arrived"

    # Add some text to the email body
    body = "This is a test email sent using Python."
    msg.attach(MIMEText(body, "plain"))

    # Add an image to the email
    #with open("image.jpg", "rb") as f:
    #   img_data = f.read()
    #img = MIMEImage(img_data, name="image.jpg")
    #msg.attach(img)

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        if smtp_tls:
            server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, "aakashagrawal2710@gmail.com", msg.as_string())
