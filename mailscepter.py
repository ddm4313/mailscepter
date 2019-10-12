import imaplib
import smtplib

class MailScepter:
    def __init__(self, email, password):
        self.mail_imap = imaplib.IMAP4_SSL(f"imap.{email.split('@')[1]}", 993)
        self.mail_smtp = smtplib.SMTP_SSL(f"smtp.{email.split('@')[1]}", 465)
        try:
            self.mail_imap.login(email, password)
            self.mail_smtp.login(email, password)
        except:
            email = input("[MailScepter] Re-enter your email: ")
            password = input("[MailScepter] Re-enter your password: ")
            try:
                self.mail_imap.login(email, password)
                self.mail_smtp.login(email, password)
            except:
                raise SystemExit
    def send_mail(self, sender, recipient, message):
        self.mail_smtp.sendmail(sender, recipient, message)
        print("[MailScepter] Email sent successfully!")
