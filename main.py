from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

from time import sleep
import random
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from data import accounts
from data import email_accounts
from data import passwords
from data import number

n = 1

hour = int(time.strftime("%H"))
hours = str(hour)

mail_host = "smtp.qq.com"  # 设置服务器
mail_user = ""  # 用户名
mail_pass = ""  # 口令
sender = ''#收信人
smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 587)  # 587 为 SMTP 端口号
smtpObj.login(mail_user, mail_pass)

name_list = ' '

while n < number:  # n<max+1
    account = accounts[n]
    password = passwords[n]
    email_account = email_accounts[n]
    receivers = [email_account]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--disable-gpu")

    browser: WebDriver = webdriver.Chrome(options=chrome_options, executable_path="/home/ubuntu/chromedriver")
    #browser: WebDriver = webdriver.Chrome(options=chrome_options,executable_path="/home/ubuntu/chromedriver")
    #browser: WebDriver = webdriver.Chrome(options=chrome_options,executable_path="C:\\Users\\ASUS\\Desktop\\chromedriver.exe")

    url = 'http://hmgr.sec.lit.edu.cn'
    try:
        browser.get(url)
        sleep(5)
        browser.find_element_by_xpath("//input[@type='text']").send_keys(account)
        browser.find_element_by_xpath("//input[@type='password']").send_keys(password)
        browser.find_element_by_xpath(
            "//button[@class='van-button van-button--default van-button--normal van-button--block']").click()
        sleep(1)
        try:
            name1 = browser.find_element_by_xpath('//p[@class="user_name"]').text
        except:
            receivers = [email_account]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
            message = MIMEText('第' + str(n) + account + '账号或密码错误请联系群主及时更改', 'plain', 'utf-8')
            message['From'] = Header("Ubuntu serve", 'utf-8')
            message['To'] = Header('账号或密码错误 请及时联系群主更改', 'utf-8')
            subject = '自动上报系统'
            message['Subject'] = Header(subject, 'utf-8')
            smtpObj.sendmail(sender, receivers, message.as_string())
            browser.quit()
            n = n + 1

    except:
        receivers = [email_account]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        message = MIMEText(str(n) + '发生反爬虫', 'plain', 'utf-8')
        message['From'] = Header("Ubuntu serve", 'utf-8')
        message['To'] = Header("发生反爬虫", 'utf-8')
        subject = '发生反爬虫'
        message['Subject'] = Header(subject, 'utf-8')
        smtpObj.sendmail(sender, receivers, message.as_string())
        browser.quit()
        quit()
    if hour < 12:

        # first times
        try:
            name1 = browser.find_element_by_xpath('//p[@class="user_name"]').text
            name = name1[4:]
            print(name1)
            browser.find_element_by_xpath("//div[@role='checkbox']").click()
            sleep(1)
            browser.find_element_by_xpath(
                "//button[@class='bottom_btn van-button van-button--default van-button--normal van-button--block']").click()
            sleep(1)
            browser.find_element_by_xpath("//input[@placeholder='腋下温度(小数或整数)']").send_keys(
                str(36 + 0.1 * random.randint(1, 5)))
            browser.find_element_by_xpath(
                "//button[@class='ensure_button van-button van-button--default van-button--normal van-button--block']").click()
            sleep(1)
            name_list = name_list + ' ' + str(n) + name
            browser.quit()

            message = MIMEText(str(n) + '  账号' + account + name + '  ' + hours + '点签到成功', 'plain', 'utf-8')
            message['From'] = Header("Ubuntu serve", 'utf-8')
            message['To'] = Header("签到成功", 'utf-8')
            subject = '签到成功'
            message['Subject'] = Header(subject, 'utf-8')
            smtpObj.sendmail(sender, receivers, message.as_string())
            n = n + 1
            browser.quit()

        except:
            n = n + 1
            browser.quit()
    else:
        try:
            name1 = browser.find_element_by_xpath('//p[@class="user_name"]').text
            name = name1[4:]
            browser.find_element_by_xpath("//div[@role='checkbox']").click()
            sleep(1)
            browser.find_element_by_xpath("//a[@href='javascript:;']").click()
            sleep(1)
            browser.find_element_by_xpath(
                "//button[@class='van-button van-button--default van-button--normal van-button--block']").click()
            browser.find_element_by_xpath(
                "//button[@class='ensure_button van-button van-button--default van-button--normal van-button--block']").click()

            name_list = name_list + ' ' + str(n) + name
            browser.quit()

            message = MIMEText('  ' + account + name + '  ' + hours + '点签到成功', 'plain', 'utf-8')
            message['From'] = Header("Ubuntu serve", 'utf-8')
            message['To'] = Header("签到成功", 'utf-8')
            subject = '签到成功'
            message['Subject'] = Header(subject, 'utf-8')
            smtpObj.sendmail(sender, receivers, message.as_string())
            n = n + 1
            browser.quit()
        except:
            n = n + 1
            browser.quit()

receivers = ['']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
message = MIMEText(hours + '点签到结束' + '签到人员:' + name_list, 'plain', 'utf-8')
message['From'] = Header("Ubuntu serve", 'utf-8')
message['To'] = Header("签到成功", 'utf-8')
subject = '签到成功'
message['Subject'] = Header(subject, 'utf-8')
smtpObj.sendmail(sender, receivers, message.as_string())
quit()
