from email.message import EmailMessage
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getlist

esender = "EXAMPLE@gmail.com"
epass = "xxxx yyyy zzzz aaaa"
erecievel = ['example@example.com', 'example2@example.com']
# erecievel = get_list()
abc = "abcdefghijklmnopqrstuvwxyz"

while 0 < len(erecievel):
  print(len(erecievel))
  erecieve = erecievel.pop(0)
  emID = erecieve[:-10] # Removes last **10** characters of the adress. ##### YOU NEED TO CHANGE THIS NUMBER TO FIT YOUR ORG'S DOMAIN CHAR LENGHT + @ ##### there's probably a better solution to this, too lazy rn, feel free to submit a pull request
  rotemID = "".join([abc[(abc.find(c)+13)%26] for c in emID])

  subject = "2000 USD allowance"

  em = MIMEMultipart("alternative")
  em['From'] = "Org Name"
  em['To'] = erecieve
  em['Subject'] = subject

  # text/plain part
  text = """\
  Your text,

  texty text.

  link: https://EXAMPLEDOMAIN.COM/EXAMPLE?id=""" + rotemID + """

  Regards"""

  # HTML part
  html = """\
  <html>
  <head>
  <style>

  </style>

  </head>

  <body lang=XXX link=blue vlink="#96607D" style='word-wrap:break-word'>

  <div class=WordSection1>

  <p class=MsoNormal style='margin-bottom:0.5cm;line-height:13.8pt;background:white'><span
  style='font-size:12.0pt;color:#242424'>Link;<a href="https://EXAMPLEDOMAIN.COM/EXAMPLE?id=""" + rotemID + """"><span
  style='color:#467886'>link</span></a>.</span></p>

  </div>

  </body>

  </html>
  """

  # MIMEText to MIMEMultipart
  part1 = MIMEText(text, "plain")
  part2 = MIMEText(html, "html")
  em.attach(part1)
  em.attach(part2)

  ccontext = ssl.create_default_context()
  # YOU WILL NEED TO CHANGE THE SMTP SERVER
  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ccontext) as smtp:
      smtp.login(esender, epass)
      smtp.sendmail(esender, erecieve, em.as_string())
  print("Sent to " + erecieve)
