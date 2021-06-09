from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World!"
@app.route('/say/<name>')
def say_name(name):
    return "Hello " + name + "!"
@app.route('/repeat/<int:amt>/<word>')
def repeat(amt, word):
    repeat = ""
    for times in range(int(amt)):
        repeat += word + " "
    return repeat
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.