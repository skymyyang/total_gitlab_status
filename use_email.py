#!/usr/bin/env python
# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email import utils


server = smtplib.SMTP("smtp.exmail.qq.com")

# 这里使用的是腾讯企业邮箱
class sendmail():
    def __init__(self, sender, auth, receiver):
        self.sender = sender
        self.auth = auth
        self.receiver = receiver

    def send_email(self, filename):
        m = MIMEMultipart()
        text_info = "上月代码统计，详情请参考附件"
        text_sub = MIMEText(text_info, 'plain', 'utf-8')
        data = MIMEApplication(open(filename, 'rb').read())
        data.add_header('Content-Disposition', 'attachment', filename=filename)
        title = "上月代码概况"
        m.attach(text_sub)
        m.attach(data)
        m['Subject'] = title
        # 设置属性
        m['From'] = self.sender
        m['To'] = self.receiver
        m['Date'] = utils.formatdate()
        try:
            server.login(self.sender, self.auth)
            server.sendmail(self.sender, self.receiver, m.as_string())
            print('sucess')
            server.quit()
            return 'sucess'
        except smtplib.SMTPException as e:
            print("error:", e)
            return e



if __name__ == '__main__':
    pass
    # s = sendmail("skymyyang@example.com","SPZhBboW7Ydsfs","26030555555@qq.com")
    # s.send_email("./dist/GitStatic_2021-06-01.zip")