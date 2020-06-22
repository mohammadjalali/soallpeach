from flask import Flask, request

app = Flask(__name__)

global sumOfRequests
sumOfRequests = 0

@app.route('/count')
def count():
    global sumOfRequests
    return str(sumOfRequests\n)

@app.route('/', methods=['POST'])
def index():
    global sumOfRequests
    in_number = int(request.stream.read())
    sumOfRequests += in_number
    return str(sumOfRequests\n)

if __name__ == '__main__':
    app.run(host=localhost, debug=True, port=80)

