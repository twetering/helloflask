import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, send_from_directory
     

# initialization
app = Flask(__name__)
app.config.update(dict(
    DEBUG = True,
    SECRET_KEY='devkey',
    USERNAME='admin',
    PASSWORD='colocolo',   
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# controllers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template('index.html')
    
@app.route("/concepts/")
def concepts():
    return render_template('concepts.html')
    
@app.route("/profile/")
def profile():
    return render_template('profile.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('index'))

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)