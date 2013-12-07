"""use Google SMTP send mail
"""

from smtplib import SMTP


class Mail():
    def __init__(self, user, password, smtp_server='smtp.gmail.com', port=587):
        self.user = user
        self.password = password
        #SMTP服务器地址
        self.smtp_server = smtp_server
        #服务器端口号：可选465 或 587
        self.port = port
        self.server = self.connect_server()

    def connect_server(self):
        server = SMTP(self.smtp_server, self.port)
        server.ehlo()
        server.starttls()
        server.login(self.user, self.password)
        return server

    def send(self, to_mail, message):
        """

        """
        self.server.sendmail(self.user, to_mail, message)
        self.server.quit()


if __name__ == '__main__':
    mail = Mail('admin@maguowei.com', '')
    mail.send('imaguowei@gmail.com', 'hello word')
