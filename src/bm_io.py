import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def read_email_file(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    smtp = lines[0].strip()
    from_add = lines[1].strip()
    passwd = lines[2].strip()
    to_add = lines[3].strip()

    return smtp, from_add, passwd, to_add

def send_message(email_file, body, subject):
    smtp, fromaddr, passwd, toaddr = read_email_file(email_file)
    server = smtplib.SMTP(smtp, 587)
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()

    server.starttls()
    server.login(fromaddr, passwd)
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


