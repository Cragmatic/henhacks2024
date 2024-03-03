from flask import Flask, render_template, request

import ai

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


@app.route("/support/", methods=["GET", "POST"])
def view_first_page():
    elaini_response = ''

    if request.method == "POST":
        # print(request.form["elani_input"])
        elaini_response = ai.ai_user_io(request.form["elani_input"])

    # elaini_input = ai.input_func
    # elaini_response = ai.ai_user_io

    return render_template(
        "ai.html",
        title="Elaini: Customized AI to adapt to your needs!",
        # elaini_input = elaini_input,
        elaini_response=elaini_response
    )


@app.route("/feed")
def view_second_page():
    return render_template("index.html", title="Feed page")


@app.route("/calendar")
def view_third_page():
    return render_template("index.html", title="Calendar page")


if __name__ == "__main__":
    # main()
    app.run()
