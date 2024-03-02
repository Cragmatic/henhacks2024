from flask import Flask, render_template

app = Flask(__name__)

'''
@app.route("/")
def hello_world():
    return <p>Hello, World!</p>
'''


@app.route('/')
def main():
    return render_template('test.html')


#def main():
#    print("hiii")



if __name__ == "__main__":
    main()
    #app.run()
