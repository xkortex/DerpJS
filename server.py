import random
from flask import Flask, request, redirect, url_for, send_from_directory, json, Response

app = Flask(__name__, static_folder='build')

params = {'temp': 0}

# # # # # 

def sendResponse(state, status=200):
  return Response(json.dumps(state), status=status, mimetype='application/json')

# Serves the index.html page
@app.route('/')
def root():
  return send_from_directory('build', 'index.html')

# Returns temperature
@app.route('/temperature')
def hello_world():
    return sendResponse({ "temp": random.randint(0,100) })

@app.route('/get_temperature')
def get_temperature():
    return sendResponse(params)

@app.route('/set_temperature', methods=['POST'])
def set_temperature():
    content = request.get_json()
    params.update(content)

    print('json [{}]'.format(content))

    return sendResponse({ "success": True })

# # # # # 

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')