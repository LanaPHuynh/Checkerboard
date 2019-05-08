from flask import Flask, render_template
app = Flask(__name__)

@app.route("/checker/<x>/<y>")
def hello_world(x,y):
    print ("Hello!")
    return render_template('checker.html', rows = int(x), columns = int(y))

if __name__=="__main__":
    app.run(debug=True)