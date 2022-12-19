from flask import Flask, render_template, url_for

app=Flask('__name__')

@app.route('/')
@app.route('/pocetna-stranica')
def index():
    return render_template('pocetna-stranica.html')



@app.route('/youtube')
def youtube():
    return render_template('youtube.html')

@app.route('/prijava')
def prijava():
    return render_template('prijava.html')

@app.route('/registracija')
def registracija():
    return render_template('registracija.html')

if __name__=='__main__':
    app.run(debug=True)
