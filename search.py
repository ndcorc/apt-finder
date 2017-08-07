from sets import Set
from apscheduler.schedulers.blocking import BlockingScheduler
import smtplib
from email.mime.text import MIMEText

from aptFinder import AptFinder
from aptsDotCom import AptsDotCom

websites = [AptFinder(), AptsDotCom()]

def search():
    openings = Set()
    retString = 'The following units are now available: \n'
    for website in websites:
        openings |= Set(website.find())
    if len(openings) is not 0:
        for opening in openings:
            retString += '- ' + str(opening) + '\n'
        fromAddr = 'nd.corc@gmail.com'
        toAddr = 'nd.corc@gmail.com'
        msg = MIMEText(retString)
        msg['Subject'] = 'Openings for Azul Lakeshore'
        msg['From'] = fromAddr
        msg['To'] = toAddr
        username = fromAddr
        password = 'Snickers123'
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(username,password)
        server.sendmail(fromAddr, [toAddr], msg.as_string())
        server.quit()


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(search, 'interval', hours=1)
    scheduler.start()