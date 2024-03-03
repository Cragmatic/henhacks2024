from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

app = Flask(__name__)

'''
@app.route("/")
def hello_world():
    return <p>Hello, World!</p>
'''

'''
@app.route('/')
def main():
    return render_template('test.html')
'''




def scrape_news():

    myDict = {}

    driver = webdriver.Chrome()
    driver.get('https://studentcentral.udel.edu/events')
    html = driver.page_source
    soup = BeautifulSoup(html)

    z = soup.find('div', {"id": "event-discovery-list"})
    myEvents = []
    for a in z.find_all('h3'):
        myEvents.append(a.text)

    myDatesTimes = []
    for y in soup.find('div', {"id": "event-discovery-list"}).find_all('div', {"style": "margin: 0px 0px 0.125rem;"}):
        myDatesTimes.append(y.text)

    myDates = []
    myTimes = []
    for i in range(len(myDatesTimes)):
        splitText = myDatesTimes[i].split(" ")
        myDates.append(int(splitText[2]))
        myTimes.append(splitText[4])
        myDict[myEvents[i]] = [int(splitText[2]), splitText[4]]
    
    
    return myEvents, myDatesTimes, myDict

@app.route("/")
def view_home():
    return render_template("index.html", title="Home page")

@app.route("/support")
def view_first_page():
    return render_template("index.html", title="Support page")

@app.route("/feed")
def view_second_page():
    return render_template("index.html", title="Feed page")

@app.route("/calendar")
def view_third_page():
    myEvents, myDatesTimes, myDict= scrape_news()
    return render_template("index.html", title="Calendar page", myEvents=myEvents, myDatesTimes=myDatesTimes, myDict=myDict)


#def main():
#    print("hiii")

if __name__ == "__main__":
    #main()
    app.run()
