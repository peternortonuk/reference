"""
reference:
    https://realpython.com/flask-connexion-rest-api/
    https://github.com/realpython/materials/tree/master/flask-connexion-rest

navigate to here:
   localhost:5000/api/people
"""

from flask import render_template
import connexion
from people import PEOPLE

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')


# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')


@app.route('/test')
def test():
    """
    To check the status of this variable directly as we play with the api
    """
    return PEOPLE


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
