from flask import Flask, render_template

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
    return render_template("calendar.html", title="Calendar page")


#def main():
#    print("hiii")



if __name__ == "__main__":
    #main()
    app.run()
