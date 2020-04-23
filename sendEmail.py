import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os


class EmailSender:

    def send_email_to_user(self, recepient_email):
        try:
            load_dotenv()


            # instance of MIMEMultipart
            self.msg = MIMEMultipart()

            # storing the senders email address
            self.msg['From'] = os.getenv('SENDER_EMAIL')

            # storing the receivers email address
            self.msg['To'] = recepient_email


            # storing the subject
            self.msg['Subject'] = os.getenv('EMAIL_SUBJECT')

            # string to store the body of the mail
            #body = "This will contain attachment"
            body=os.getenv('EMAIL_BODY')

            # attach the body with the msg instance
            self.msg.attach(MIMEText(body, 'plain'))

            # open the file to be sent
            # filename = os.getenv('FILENAME')
            filename = r"COVID-19-infographic.pdf"
            attachment = open(filename, "rb")


            # instance of MIMEBase and named as p
            p = MIMEBase('application', 'octet-stream')

            # To change the payload into encoded form
            p.set_payload((attachment).read())

            # encode into base64
            encoders.encode_base64(p)

            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

            # attach the instance 'p' to instance 'msg'
            self.msg.attach(p)


            # creates SMTP session
            self.smtp = smtplib.SMTP('smtp.gmail.com', 587)


            # start TLS for security
            self.smtp.starttls()

            # Authentication
            self.smtp.login(self.msg['From'], os.getenv('PASSWORD'))

            # Converts the Multipart msg into a string
            self.text = self.msg.as_string()

            # sending the mail
            self.smtp.sendmail(self.msg['From'] , recepient_email, self.text)



            # terminating the session
            self.smtp.quit()
        except Exception as e:
            print('the exception is '+str(e))