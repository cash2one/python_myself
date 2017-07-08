# -*- coding: UTF-8 -*-

# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# # xiang.sun@charmclickseo.com
# # from@runoob.com
# sender = 'xiang.sun@charmclickseo.com'
# receivers = ['1925453680@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# # 1614070582        1614070582@qq.com
#
# # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
# message = MIMEText('huihui 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟", 'utf-8')
# message['To'] =  Header("测试", 'utf-8')
#
# subject = 'huihui 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
#
# try:
#     smtpObj = smtplib.SMTP('smtp.exmail.qq.com')
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print "邮件发送成功"
# except smtplib.SMTPException:
#     print "Error: 无法发送邮件"

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.exmail.qq.com"  #设置服务器
mail_user = "xiang.sun@charmclickseo.com"    #用户名
mail_pass = "Ww123456"   #口令


sender = 'xiang.sun@charmclickseo.com'
receivers = ['1925453680@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('http://115.159.148.162:8080/searchWebVersionOne/default.jsp  小菜鸟必点', 'plain', 'utf-8')
message['From'] = Header("小菜鸟@菜鸟", 'utf-8')
message['To'] = Header(" 是个小菜鸟  ", 'utf-8')

subject = '邮件'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"