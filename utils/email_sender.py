import smtplib

def send_email(subject, message, recipient):
    sender = "b835bb19ee58a1"
    password = "5241cf54df3d75"

    if not sender or not password:
        print("Email credentials not set. Please set the EMAIL_USERNAME and EMAIL_PASSWORD environment variables.")
        return

    receiver = recipient
    body = message

    email_text = """\
    From: %s
    To: %s
    Subject: %s
    %s
    """ % (sender, ", ".join(receiver), subject, body)

    try:
        server = smtplib.SMTP_SSL('sandbox.smtp.mailtrap.io', 465)
        server.ehlo()
        server.login(sender, password)
        server.sendmail(sender, receiver, email_text)
        server.close()
        print('Email sent!')

    except Exception as exception:
        print("Error: %s!\n\n" % exception)

send_email("Test", "This is a test email", ["recipient@example.com"])
