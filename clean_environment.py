import requests

# To clean up the environment

# Try Stoping REST Api server
try:
    res = requests.get('http://127.0.0.1:5000/stop_server')
    print("REST Api " + res.text)
except Exception as error:
    print("REST Api: ")
    print(error)

print("_____________")

# Try Stoping web application server
try:
    res = requests.get('http://127.0.0.1:5001/stop_server')
    print("Web application " + res.text)
except Exception as error:
    print("Web application: ")
    print(error)