#!flask/bin/python
from app import app # Importing app Flask-variable from our packet app 

app.run(debug = True, host='0.0.0.0')