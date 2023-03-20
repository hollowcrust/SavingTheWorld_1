from flask import Flask, render_template, request
from hashlib import sha256 #no salt yet
import csv

app = Flask(__name__)


@app.route('/',  methods=['GET', 'POST'])
def index():
	data = None
	file_content = []
	if request.method == 'POST':
		username = request.form['username']

		password = str(
    		sha256(
                str(request.form["password"].strip()).encode("utf-8")
            ).hexdigest()
        )
		
		fullname = None
		Class = None
		
		if(username == 'Discere Servire' and password == '8358544a4658c414836b7f90f56305883fb921fd92ab452f8609a61afe4bd641'):
			data = 'GoToASR'
		elif(username == 'Non Mihi Solum' and password == '1d8391adfed7fb30460ab2aa63c6391a6c7f6a6d2dc4e5ec899bcbd965729909'):
			data = 'GoToAnotherASR'
		elif(username == 'Easter' and password == '37c50c935cd2a9ad065faec4824b7484acfd2b235c52368ccdb05d1f50240af0'):
			data = 'Easter'
		elif(username == 'Rick' and password == '87a000c6f6744b9dba814e868d53b67571d4821c8750378f7a41cc62fc481e64'):
			data = 'Rick'
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

					elif(username == row[0] and password != row[1]):
						file.close()
						return render_template('index.html', data='WrongPass')
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
		password = str(
    		sha256(
                str(request.form["password"].strip()).encode("utf-8")
            ).hexdigest()
        )
		fullname = request.form['fullname']
		Class = request.form['class']
		with open('data.csv', 'r') as file:
			raw = csv.reader(file)
			for row in raw:
				file_content.append(row)

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
