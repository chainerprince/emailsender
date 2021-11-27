import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

sender_email = "mutegetsi2000@gmail.com"
receiver_email = "princemutegetsi@gmail.com"
password = getpass("Type your password and press enter: ")

message = MIMEMultipart("alternative")
message["Subject"] = "Email sent using python Script"
message["From"] = sender_email
message["To"] = receiver_email


text = """\
Hi,
How are you?
I am Mutegetsi Prince I sent this email using a python script"""
html = """\
<html>
  <body>
    <h5 style="color:blue">Hi,<br>
       I believe you are well?<br>       
    </h5>
    <div>
    <img src="https://res.cloudinary.com/blocker/image/upload/v1637758002/page_y3lmsb.png" width="600" height="400"/> <br>    
    </div>
    <div style="display:flex;">    
         <span>Checkout more about me here<span/> <a href="http://www.pmutegetsi.me">Mutegetsi Prince</a>
    </div>     
    <div>
    <span>This is a link to the script: <span/> <a href="https://github.com/chainerprince/emailsender.git">Script Codes</a>
    </div>
       
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )