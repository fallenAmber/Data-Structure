import os
import smtplib

EMAIL_ADDRESS= str(input())
EMAIL_PASSWORD= str(input())
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    subject='This is entirely on testing purpose'
    body='As you\'re getting this, I want you to know I care for you and you\'ll be remembered throughout ups and downs .\n Otherwise the paper is in order'

    msg=f'Subject: {subject}\n\n {body}'
    smtp.sendmail(EMAIL_ADDRESS, 'kimonnona_pn@hotmail.com', msg)
    smtp.quit()
    print("Email successfully sent")