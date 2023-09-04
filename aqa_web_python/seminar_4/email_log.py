import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_log_via_email(email_from, email_to, password, file_name):
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = email_to
    msg['Subject'] = 'Результаты автотестов для тестового стенда gb'

    with open(file_name, 'rb') as f:
        part = MIMEApplication(f.read(), Name=basename(file_name))
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file_name)
    msg.attach(part)

    body = 'Результат автотестирования тестового стенда GB https://test-stand.gb.ru'
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(email_from, password)
    text = msg.as_string()
    server.sendmail(email_from, email_to, text)
    server.quit()
