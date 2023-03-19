from flask import Flask, render_template, request
import csv

app = Flask(__name__)

#will add sha256

@app.route('/',  methods=['GET', 'POST'])
def index():
	data = None
	file_content = []
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		fullname = None
		Class = None
		
		if(username == 'Discere Servire' and password == 'Non Mihi Solum'):
			data = 'GoToASR'
		elif(username == 'Non Mihi Solum' and password == 'Discere Servire'):
			data = 'NotGoToASR'
		elif(username == 'placeholder for SQL injection'):
			data = 'SQLINJ'
		elif(username == 'Easter' and password == 'Egg'):
			data = 'Easter'
		else:
			with open('data.csv', 'r') as file:
				raw = csv.reader(file)
				for row in raw:
					file_content.append(row)

				for row in file_content:
					if(username == row[0] and password == row[1]):
						fullname = row[2]
						Class = row[3]
						file.close()
						return render_template('index.html', data='Normal', username=username, fullname=fullname, Class=Class)
			file.close()
			data = 'NotFound'
			
	return render_template('index.html', data=data)
	



@app.route('/registration',  methods=['GET', 'POST'])
def registration():
	#open and write csv file
	#submit stuff
	file_content = []
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		fullname = request.form['fullname']
		Class = request.form['class']
		with open('data.csv', 'r') as file:
			raw = csv.reader(file)
			for row in raw:
				file_content.append(row)
			print(file_content)
			for row in file_content:
				if(username == row[0]):
					file.close()
					return render_template('registration.html', error='UsernameTaken')

				if(fullname == row[2]):
					file.close()
					return render_template('registration.html', error='AccountMade')
		
		file.close()
		
		data = [username, password, fullname, Class]
		with open('data.csv', 'a') as file:
			writer = csv.writer(file)
			writer.writerow(data)
			
		file.close()
		
	return render_template('registration.html')


app.run(host='0.0.0.0', port=5000)
