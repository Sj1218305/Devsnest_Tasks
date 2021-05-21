from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/send", methods=['POST'])    
def convert():
	if request.method == 'POST':
		store = request.form.get('strings').split(" ")
		concatenate = ""
		for x in store:
			concatenate = concatenate + x
		return concatenate


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)	
