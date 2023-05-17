from flask import Flask, render_template

app = Flask(__name__)

@app.route('/dash')
def dashboard():
    data = {
        "january": 25,
        "february": 35,
        "march": 7,
        "april": 56,
        "may": 89,
        "june": 0,
        "july": 34,
        "august": 23,
        "september": 12,
        "october": 89,
        "november": 99,
        "december": 11,
        
    }
    return render_template('dashboard.html',data=data)

if __name__=='__main__':
        app.run(debug=True)
