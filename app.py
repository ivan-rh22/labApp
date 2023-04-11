from flask import Flask, render_template,request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret'

# function to read in details for page
def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

@app.route("/")
def home():
    name = 'Ricardo I. Hernandez'
    content = readDetails("static/about.txt")
    return render_template('base.html', name=name, aboutMe=content)

@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        name = request.form['name']
    return render_template('form.html', name=name)

@app.route('/counter', methods=['GET', 'POST'])
def counter():
    if 'count' not in session:
        session['count'] = 0
    return render_template('counter.html', count=session['count'])

@app.route('/count', methods=['POST'])
def count():
    session['count'] += 1
    return str(session['count'])

@app.route('/reset', methods=['POST'])
def reset_count():
    session['count'] = 0
    return redirect(url_for('counter'))

if __name__ == "__main__":
    app.run(debug=True)