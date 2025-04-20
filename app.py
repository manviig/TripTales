from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 
@app.route('/map')
def map_page():
    return render_template('map.html')  
@app.route('/italy')
def italy_page():
    return render_template('italy.html')  
@app.route('/india')
def india_page():
    return render_template('india.html')  
@app.route('/japan copy')
def japan_page():
    return render_template('japan copy.html')  
@app.route('/korea')
def korea_page():
    return render_template('korea.html')  
@app.route('/russia')
def russia_page():
    return render_template('russia.html')  
@app.route('/india map')
def indiamap_page():
    return render_template('indiamap.html')

@app.route('/itinerary')
def itinerary_page():
    return render_template('itinerary.html')

@app.route('/booking')
def booking_page():
    return render_template('booking.html')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/uttarakhand')
def uttarakhand():
    return render_template('uttarkhand.html')


if __name__ == '__main__':
    app.run(debug=True)
