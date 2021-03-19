from flask import render_template, current_app as app

@app.route('/')
def get_index():
    return render_template('index.html')

@app.route('/starfield')
def get_starfield():
    return render_template('starfield.html')
