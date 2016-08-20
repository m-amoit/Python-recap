from flask import Flask, render_template
app = Flask(__name__)
@app.route('/result')
def result():
	dict = {'math':70, 'chem':84, 'phyc':68}
	return render_template('result.html', result=dict)

if __name__=='__main__':
	app.run(debug=True)
