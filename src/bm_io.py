import smtplib
import string
import subprocess
import tempfile
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def read_email_file(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
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

def read_data_file(filename):
    f = open(filename,'r')
    lines = f.readlines()
    f.close()
    data_dict = {}
    for line in lines:
        (name_txt, time_txt, weight_txt) = line.split()
        data_dict[name_txt] = (string.replace(name_txt, '_', ' '),
                               int(time_txt), float(weight_txt))
    return data_dict

def read_sequence_file(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    step_list = []
    for line in lines:
        elements = line.split()
        n_elements = len(elements)
        max_time = float(elements[-2])
        units = elements[-1]
        step = [elements[i] for i in xrange(n_elements-2)]
        step_list.append((step, max_time, units))
    return step_list

def read_sms_file(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    buddy = lines[0].strip()
    service = lines[1].strip()
 
    return buddy, service

def send_sms_message(sms_file, body):
    buddy, service = read_sms_file(sms_file)
    fname = tempfile.NamedTemporaryFile(mode='w', delete=False)
    fname.write("tell application \"Messages\"\n")
    fname.write("activate\n")
    fname.write("send \"%s\" to buddy \"%s\" of service \"E:%s\"\n" %
        (body, buddy, service))
    fname.write("end tell")
    fname.close()
    subprocess.call(["osascript", fname.name])
    os.unlink(fname.name)
