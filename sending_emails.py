def initial_sender(titles):
    import smtplib, ssl

    from_addrs = "thegeartofear@gmail.com"
    to_addrs = "ricoandreas.lepp@real.edu.ee"
    
    password = "Obelisk1234"
    msg = "\r\n".join(
            ["From: Reaalibot\n", "To: ricoandreaslepp\n", "Subject: Uudised\n"]+
            ["Reaalilehel hetkel olevad pealkirad:\n"] + titles + ["", "Best wishes"]).encode('utf-8')

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()

    server.login(from_addrs, password)
    server.sendmail(from_addrs, to_addrs, msg)

    server.quit()

def send_confirmation(titles):
    import smtplib
    from email.message import EmailMessage

    from_addrs = "thegeartofear@gmail.com"
    to_addrs = "ricoandreas.lepp@real.edu.ee"
    password = "Obelisk1234"

    msg = EmailMessage()
    msg['Subject'] = "Uudised!"
    msg['From'] = "Reaalibot"
    msg['To'] = to_addrs
    
    message = "\r\n".join(
            ["Tere!\n\n", "Reaalilehelt on tulnud uued uudised!\n"] +
            ["/*--*/ " + i for i in titles] +
            ["", "Parimat soovides"])

    msg.set_content(message)
    
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()

    server.login(from_addrs, password)
    server.sendmail(from_addrs, to_addrs, msg.as_string())

    server.quit()

def spam_bot(i):
    import smtplib
    from email.message import EmailMessage

    from_addrs = "thegeartofear@gmail.com"
    to_addrs = "ricoandreas.lepp@real.edu.ee"
    password = "Obelisk1234"

    msg = EmailMessage()
    msg['Subject'] = "Ya like jazz? " + str(i)
    msg['From'] = "Linnuke " + str(i)
    msg['To'] = to_addrs

    message = """eat ass, listen to jazz
    is this ill eagle?
    """
    
    msg.set_content(message)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()

    server.login(from_addrs, password)
    server.sendmail(from_addrs, to_addrs, msg.as_string())

    server.quit()

