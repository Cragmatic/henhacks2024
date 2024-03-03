from flask import Flask, render_template, request, redirect, url_for
import ai
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
    for i in range(len(myDatesTimes)):
        splitText = myDatesTimes[i].split(" ")
        myDict[myEvents[i]] = [int(splitText[2]), splitText[4]]
    return myDict

@app.route("/")
def view_home():
    return render_template("login.html", title="Home page")

@app.route("/support/", methods=["GET", "POST"])
def view_first_page():
    elaini_response = ''
    if request.method == "POST":
        elaini_response = ai.ai_user_io(request.form["elani_input"])
    return render_template(
        "ai.html",
        title="Elaini: Customized AI to adapt to your needs!",
        elaini_response=elaini_response
    )

@app.route("/feed", methods=["GET", "POST"])
def view_second_page():
    if request.method == "POST":
        addFeed = request.form.get("ADDfeed")
        return render_template("feed.html", title="Feed page", addFeed=addFeed)
    return render_template("feed.html", title="Feed page")

@app.route("/calendar")
def view_third_page():
    events= scrape_news()
    return render_template("calendar.html", title="Calendar page", events=events, c=range(1,31))


@app.route("/login", methods=["GET", "POST"])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == '12345':
        return redirect(url_for('calendar'))
    else:
        return render_template('login.html', message='Invalid credentials')



if __name__ == "__main__":
    # main()
    app.run()
