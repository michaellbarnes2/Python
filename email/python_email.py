#!/usr/bin/env python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Send the message via local SMTP server.
s = smtplib.SMTP_SSL(


# me == my email address
# you == recipient's email address
me = "michael.barnes@plexusworldwide.com"
you = "it.devops@plexusworldwide.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "AWS ecom enclave backup report"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Application deployment to prod is complete!\nQA team can start testing\nUse the following link to begin testing:\nhttps://www.python.org"
html = """\
<html>
  <head></head>
  <body>
    <p>Backup report completed for AWS ecom
       AWS backup report files are located: <a href="ystems">link</a> 
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)


# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
s.sendmail(me, you, msg.as_string())
s.quit()
