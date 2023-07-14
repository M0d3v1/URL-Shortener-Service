# URL-Shortener-Service
This is a URL shortener service built with Django, Django REST Framework, and Redis. 
Features
Shorten long URLs to compact and manageable short URLs.
Redirect users to the original long URL when they visit the shortened URL.
View statistics such as the number of clicks for each shortened URL.
Installation
Clone the repository: git clone <repository_url>
Create a virtual environment and activate it:
# Create virtual environment (optional)
python -m venv myenv

# Activate virtual environment
source myenv/bin/activate

Install the dependencies:

pip install -r requirements.txt

Configure the database:

The project is currently configured to use SQLite as the database backend. If you want to use a different database, update the DATABASES setting in the settings.py file.
Apply database migrations:
python manage.py migrate
Run the development server:

python manage.py runserver
The URL shortener service will be accessible at http://localhost:8000/url/

API Endpoints
POST /url/: Create a new shortened URL.
GET /url/: Retrieve a list of all shortened URLs.
GET /url/<id>/: Retrieve details of a specific shortened URL.
PUT /url/<id>/: Update a shortened URL.
DELETE /url/<id>/: Delete a shortened URL.
For detailed API documentation, refer to the API Documentation file.

Usage
Send a POST request to /url/ with the following parameters:

original_url: The long URL you want to shorten.
Example:
curl -X POST -H "Content-Type: application/json" -d '{"original_url":"https://www.example.com/long-url"}' http://localhost:8000/url/
This will return a response with the shortened URL.

Access the shortened URL:http://localhost:8000/url/<short_code>/
Replace <short_code> with the code generated in the previous step.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please submit an issue or a pull request.
