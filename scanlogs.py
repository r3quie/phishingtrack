import time
from email.message import EmailMessage
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def scanLogs(file):
    abc = "abcdefghijklmnopqrstuvwxyz"
    with open(file, "r") as f:
        lines = f.readlines()
        return ["".join([abc[(abc.find(c)+13)%26] for c in line.split("?id=")[1].split(" ")[0]]) for line in lines if "?id=" in line]

def sendmail(clickers):
    esender = "email@gmail.com"
    epass = "yourappcode"
    erecievel = ["example@google.com", "example@protonmail.com"]
    while 0 < len(erecievel):
        erecieve = erecievel.pop(0)
        subject = "New clicks"
        em = MIMEMultipart("alternative")
        em['From'] = "Logger"
        em['To'] = erecieve
        em['Subject'] = subject

        text = "Clicks: " + str(clickers)
        html = """<html><body><p>Clicks: """+str(clickers)+"""</p></body></html>"""
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        em.attach(part1)
        em.attach(part2)

        ccontext = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ccontext) as smtp:
            smtp.login(esender, epass)
            smtp.sendmail(esender, erecieve, em.as_string())

if __name__ == "__main__":
    path = input("Enter file name or path:\n")
    old = None
    while True:
        new = scanLogs(path)
        if old != new:
            old = new
            sendmail(new)
        time.sleep(60)