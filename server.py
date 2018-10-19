from flask import Flask
import price_alert
app = Flask(__name__)

@app.route('/')
def index():
	
	return "Your app is running!"

@app.route('/getCurrentPrice')
def getPrice():
    url = 'https://www.amazon.com/Gaming-i7-8750H-Display-Gigabit-FX504GM-ES74/dp/B07F6K21HJ/'
    content = price_alert.simple_get(url)
    return price_alert.get_price(content)




if __name__ == '__main__':
    app.run()



