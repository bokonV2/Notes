from flask import Flask, render_template, redirect

from notes.index import notes

app = Flask(__name__)
app.register_blueprint(notes, url_prefix='/notes')

@app.route('/')
def index():
    return redirect('/notes/')

@app.route('/help')
def help():
    return render_template('help.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
