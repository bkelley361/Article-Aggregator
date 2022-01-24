from bs4 import BeautifulSoup
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import datetime

def login(): #Runs the program
    MY_ADDRESS = "Email"
    MY_PASSWORD = "Password"
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.ehlo()
    s.login(MY_ADDRESS, MY_PASSWORD)
    msg = MIMEMultipart()

    x = datetime.datetime.now()
    finalMsg = str(x) + "\n\n"

    finalMsg += getVerge()
    finalMsg += getEngadget()
    finalMsg += getDigitalTrends()

    msg['From'] = MY_ADDRESS
    msg['To'] = "Recipient Address"
    msg['Subject'] = "Articles"
    msg.attach(MIMEText(finalMsg, 'plain'))
    s.send_message(msg)
    s.quit()

    print("Message Sent")

def getVerge(): #The Verge website
    url = 'https://www.theverge.com/tech'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    findArticles = soup.find('div', class_="l-reskin l-hub-wrapper has-group-header")

    findIndividual = findArticles.find_all('div', class_="c-compact-river__entry")

    msg = "The Verge\n\n"

    for a in findIndividual:
        header = a.find('h2', class_="c-entry-box--compact__title")
        link = header.find('a', href=True)
        link = link['href']
        header = header.text
        msg += finalMsg(header, link)
    return msg

def getEngadget(): #Engadget website
    url = "https://www.engadget.com/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    findArticles = soup.find('div', id="module-latest")
    findIndividual = findArticles.find_all("div", class_="D(f) Fld(c) Ai(fs)")
    msg = "Engadget\n\n"

    for a in findIndividual:
        header = a.find("h2")
        link = header.find('a', href=True)
        link = "https://www.engadget.com" + link["href"]
        header = header.text
        msg += finalMsg(header, link)
    return msg

def getDigitalTrends(): #DigitalTrends website
    url = "https://www.digitaltrends.com"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    findArticles = soup.find('div', class_="b-grid b-grid__cols2 b-grid__rows12")
    findIndividual = findArticles.find_all('div', class_="b-meta b-snippet__meta b-snippet--2-2__meta")
    msg = "Digital Trends\n\n"

    for a in findIndividual:
        header = a.find("h3")
        link = header.find('a', href=True)
        link = link['href']
        header = header.text
        header = header.replace('\n','')
        msg += finalMsg(header, link)
    return msg

def finalMsg(header, link):
    msg = header + "\n"
    msg += link + "\n\n\n"
    return msg

login()