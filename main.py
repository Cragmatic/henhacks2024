from flask import Flask, render_template, request, redirect, url_for
import ai
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# URL of the Canvas API endpoint
courseurl = "https://udel.instructure.com:443/api/v1/courses/1761781/assignments?order_by=due_at"
# Canvas access token
access_token = "25~MeKzRGR5wUWF9au7XwVeceEIubMRsucYxAi1AwsycUxpuvt8CzVtI7tiQlSROaDU"
#"25~EQFlkWacDA3dN9NTEsxXl7GRwsXr7B5H6h0xrssjgRmNnwglJ1RjDrumO6fBYSZ6"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

response = requests.get(courseurl, headers=headers)

assignments = dict()
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Print some information from the response
    for assignment in data:
        if (assignment['due_at'][5:7] == '03'):
            assignments[assignment['name']] = [int(assignment['due_at'][8:10]), '11pm']
else:
    print("Error:", response.status_code)
    print("Response:", response.text)
print(assignments)

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
        nameFeed = request.form.get("NAMEfeed")
        descriptionFeed = request.form.get("DESCfeed")
        return render_template("feed.html", title="Feed page", addFeed=addFeed, nameFeed=nameFeed, descriptionFeed=descriptionFeed)
    return render_template("feed.html", title="Feed page")

@app.route("/calendar")
def view_third_page():
    events= scrape_news()
    return render_template("calendar.html", title="Calendar page", events=events, assignments=assignments, c=range(1,31))


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
