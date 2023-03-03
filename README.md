# Food Recipe App   🔗 [Live Link](http://13.233.149.208:8000/)

Welcome to our Food Recipe App - the ultimate platform for all your recipe needs! With our simple and user-friendly web application, you can easily search and view hundreds of delicious food recipes. Whether you're a seasoned chef or a cooking novice, our app has something for everyone. Plus, with the ability to sign up, login, and add/edit your own recipes, you can showcase your culinary skills and share your favorite recipes with the world!

## Installation & Setup 🏭

To set up and install our containerized Recipe backend using Docker, follow these steps:

- Clone the GitHub repository to your local machine
- Navigate to the project directory
- Run the following command to build the Docker containers: `docker-compose build`
- Start the containers using the following command: `docker-compose up`
- Open a web browser and navigate to `http://localhost:8000` to access the Recipe app.

Note: The entire application has been containerized using Docker, ensuring that the application is portable and can be easily deployed on any system with Docker installed. If you make any changes to the code, you may need to rebuild the containers and restart the application. You can do this by running the `docker-compose down` command followed by `docker-compose up`.

To set up without Docker, follow these steps:

- Clone this repository to your local machine using `git clone https://github.com/yogesh2k21/recipes.git`
- Create a virtual environment for the project using virtualenv `pip install virtualenv` then `virtualenv venv` and then `venv/Scripts/activate`
- Install the required packages listed in requirements.txt using `pip install -r requirements.txt`.
- Run the server using `python manage.py runserver`.

## How its Works 🏃‍♂️🏃‍♀️

- After Installation is done and server is running now, just open your web browser and go to http://localhost:8000.
- Sign up for a new account or login with your existing account.
- Search for recipes using the search bar on the homepage.
- Click on a recipe to view its details, including image, description, ingredients, and steps.
- To add a new recipe, click on the "Create Recipe" button on the homepage or in the navbar.
- To edit a recipe, click on the "Edit Recipe" button on the recipe details page.

## Features 📜

- Users can sign up and login
- Users can search for recipes based on food name or ingredients used
- Users can view a recipe's image, description, ingredients, and steps
- Users can add/edit their own recipes
- Users can perform CRUD operations on recipes
- Responsive UI/UX design
- Easy to use and navigate

## Authentication 🔐

We have used Django session authentication and the built-in User model to handle user authentication and authorization in this app. When a user logs in, a session is created and stored on the server. This session is then used to authenticate the user for subsequent requests.

To handle user registration, login, and editing of user information, we have used Django's built-in User model, which provides a secure and easy-to-use way to manage user accounts, passwords, and permissions.

Using Django's session authentication and the User model provides a secure and scalable way to manage user accounts in our app. It also allows for easy integration with other Django apps and automatic handling of password hashing.

## Tools ⚒️ and Tech Stack 🧑‍💻

Tech Stack used in our platform:

- Django Python web framework for backend development
- SQLite for lightweight database management
- TailwindCSS for styling and UI design

##  Requirements 🏗️

Requirements to run this application:

- Docker installed on your system
- At least 4 GB of RAM available
- A web browser, such as Google Chrome, Mozilla Firefox, or Microsoft Edge
- A stable internet connection

Note: The application has been tested on Linux and macOS, but it should also run on Windows with Docker installed. The required packages and dependencies are included in the Docker containers, so you do not need to install anything manually on your system.

## Hosting & Deployment ☁️

This Recipe app's backend has been hosted on Amazon EC2 as part of my journey to learn about AWS and containerized using Docker.
By using Docker, the application has been packaged into a container that can be easily moved between development, testing, and production environments.
AWS provides a wide range of cloud computing services, and hosting this application on EC2 has been a great opportunity to dive deeper into the platform. 
By hosting on EC2, I was able to gain hands-on experience with cloud computing and improve my skills in this area.

## END

Thank you for taking the time to review this Recipe app project. Your feedback and support are greatly appreciated. If you have any questions or comments, please feel free to reach out.

