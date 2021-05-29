import smtplib
import time
import imaplib
import email
import traceback
import re
# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "souro89" + ORG_EMAIL
FROM_PWD = "souro1989"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        data = mail.search(None, '(from "action@ifttt.com")')
        mail_ids = data[1]


        id_list = mail_ids[0].split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        int_id_list = []
        int_id_list.append(latest_email_id)

        for i in int_id_list:
            data = mail.fetch(str(i), '(RFC822)' )
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1],'utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('Date : ' + msg['Date'])
                    otpmsg=re.findall(r"[ ]\d{6}.",str(msg))[0]
                    return otpmsg.replace(' ','').replace('.','')


    except Exception as e:
        print(str(e))
        return -1