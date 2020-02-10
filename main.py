from chat import Chat, render_template

app = Chat(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('īndex.html')

if __name__ == 'main':
    app.run(host='0.0.0.0', threaded=True, port='5000', debug=True)