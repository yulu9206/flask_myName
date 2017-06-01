from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('main.html')	
@app.route('/process', methods=['POST'])
def creat_user():
	name = request.form['name']
	print name
	return redirect('/')

app.run(debug=True)