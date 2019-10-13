from flask import Flask, render_template, request 
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
	city_name = request.form['city_name']
	r = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city_name+',us&appid=ef6f79166f13c52387485b465b94796b')
	json_object = r.json()
	temp_k = float(json_object['main']['temp'])
	temp_f = (temp_k - 273.15) * 1.8 + 32
	return render_template('temperature.html', temp=round(temp_f), city=city_name)

@app.route('/')
def weather():
	return render_template('weather.html')

if __name__ == '__main__':
	app.run(debug=True)