import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from environment import get_from_config, get_from_dotenv


def send_mail(subject, log_path, img_path, mode=get_from_config):
    with open(img_path, 'rb') as raw_img, open(log_path) as raw_log:
        img = raw_img.read()
        log = raw_log.read()

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mode('email')
    msg['To'] = mode('email')

    log = MIMEText(log)
    msg.attach(log)

    image = MIMEImage(img, name=os.path.basename(img_path))
    msg.attach(image)

    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.ehlo()
    conn.login(mode('email'), mode('email_app_password'))
    conn.sendmail(msg['From'], msg['To'], msg.as_string())
    conn.quit()

    logging.info(f'Attendance report sent.')
