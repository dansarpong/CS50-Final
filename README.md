# EasyEats: A Recipe Finder Web Application

#### Video Demo:  [YOUTUBE LINK](https://www.youtube.com/watch?v=-GUcf3J3VU8)


#### Description

EasyEats is a web application developed as a final project for Harvard's CS50x course. The application is built with Flask, a micro web framework written in Python. It uses the Edamam API to fetch recipes based on user input, providing a simple and intuitive interface for finding new and exciting recipes to try.

The application is designed with simplicity and ease of use in mind. It provides a clean, user-friendly interface that allows users to search for recipes based on ingredients they have on hand. The application also features a random recipe generator on the homepage, providing users with culinary inspiration at the click of a button.

#### Project Structure

The project follows a typical Flask application structure, with a main Python script (`app.py`) that handles routing and request handling, a `templates/` directory for HTML templates, and a `static/` directory for static files such as images and CSS.

##### app.py

`app.py` is the heart of the application. It sets up the Flask application and defines the routes that the application responds to. Each route corresponds to a different page on the website, and each function associated with a route is responsible for handling requests to that page and returning the appropriate response.

The `app.py` file also handles communication with the Edamam API. It sends requests to the API based on user input, receives the response, and processes the data to be displayed on the website.

##### requirements.txt

`requirements.txt` is a file that lists all Python packages that the project depends on. These packages can be installed using pip, a package manager for Python. The command `pip install -r requirements.txt` installs all necessary packages.

##### static/

The `static/` directory contains static files that are served directly by the web server. In this project, it contains the logo for the application.

##### templates/

The `templates/` directory contains HTML templates that are used to generate the pages of the website. Flask uses a templating engine called Jinja2, which allows for dynamic insertion of data into HTML templates.

###### index.html

`index.html` is the main template for the application. It serves as the homepage and displays a random recipe to the user.

###### layout.html

`layout.html` is a base template that other templates inherit from. It contains elements that are common to all pages, such as the header and footer.

###### search.html

`search.html` is used to display search results. It takes the data returned from the Edamam API and displays it in a user-friendly format.

##### Design Choices

One of the main design choices made in this project was the use of Flask as the web framework. Flask was chosen for its simplicity and flexibility. It allows for a lot of freedom in how the application is structured and doesn't impose much in the way of constraints or prerequisites. This makes it a great choice for small, simple applications like EasyEats.

Another important design choice was the use of the Edamam API for fetching recipes. There are many APIs available for this purpose, but Edamam was chosen for its extensive database of recipes and its straightforward, easy-to-use API.

#### How to run:
To run this application locally, run the following commands in your terminal:
```bash
git clone https://github.com/dansarpong/CS50-Final.git
cd CS50-Final
pip install -r requirements.txt
export FLASK_APP=application.py
flask run
```
Then, open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

##### Conclusion

EasyEats is a simple, user-friendly web application for finding recipes. It demonstrates the use of Flask for web development and the use of APIs to fetch data from external sources. The application is designed with simplicity and ease of use in mind, providing a clean, intuitive interface for users to interact with.

While the application is currently quite simple, there is a lot of potential for further development. Features such as user accounts, saving favorite recipes, and more advanced search options could be added in the future. Despite its simplicity, EasyEats serves as a great introduction to web development with Flask and API usage.
