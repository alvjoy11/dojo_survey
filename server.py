from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.secret_key = 'very secret'

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/result', methods=['POST'])
def submit():
	data = request.form
	# name =  request.form['name']
	# location = request.form['dojo']
	# language = request.form['fave_lang']
	# comments = request.form['comment']
	print data
	return render_template('show.html', data=data)
	# return redirect('/')
	# redirects back to the '/' route

app.run(debug=True)