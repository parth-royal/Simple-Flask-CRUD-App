##  Simple Flask CRUD App

This project demonstrates a basic CRUD (Create, Read, Update, Delete) application using Flask. It allows you to manage a list of users with their names and contact details.

### Project Structure

The project contains the following files:

* **`app.py`:** The main Flask application code, handling routing, form processing, and data management.
* **`templates/base.html`:**  The base HTML template for the application, providing a basic layout.
* **`templates/index.html`:** The template for displaying the list of users.
* **`templates/add_user.html`:** The template for adding a new user.
* **`templates/edit_user.html`:** The template for editing an existing user.

### Functionality

* **User List Display:**  The `/` route displays the list of users in a table format using the `index.html` template.
* **User Creation:** The `/add_user` route handles adding new users. It displays the `add_user.html` template for user input and processes the form data using the POST method.
* **User Editing:** The `/edit_user/<uid>` route allows editing an existing user. It displays the `edit_user.html` template, pre-populated with the user's data, and processes the form data using the POST method.
* **User Deletion:** The `/delete_user/<uid>` route removes a user from the list.
* **Flash Messages:**  The application uses flash messages to provide feedback to the user on successful operations like adding, updating, and deleting users.

### Prerequisites

* **Python 3.6 or higher:** Install Python if you don't have it already.
* **Flask:** Install Flask using `pip install Flask`.

### Setup

1. **Install Dependencies:**
    * Install the required Python packages using the command: `pip install -r requirements.txt`
2. **Run the Application:**
    * Run the Flask application using `python app.py`. This will start the server, and you can access the application at `http://127.0.0.1:5000/`.

### Using the Application

1. **View User List:**  Access the home page (`/`) to see the list of users.
2. **Add a User:**  Click the "Add User" link (or navigate to `/add_user`) to add a new user. Fill in the required details and submit the form.
3. **Edit a User:**  Click the "Edit" link next to a user to edit their details. Update the fields and submit the form.
4. **Delete a User:**  Click the "Delete" link next to a user to remove them from the list.

### Important Notes

* **Data Persistence:**  The user data is stored in memory (within the `users` list) and will be lost when the application stops. Consider using a database (e.g., SQLite, PostgreSQL) to persist the data.
* **Security:**  The application has a basic secret key for session management, but it's important to implement proper security measures such as input validation, password hashing, and secure data storage for real-world applications.
* **Error Handling:**  Add error handling to gracefully manage cases like invalid input or database errors.

### Further Development

* **Database Integration:**  Integrate a database to make the user data persistent.
* **User Authentication:**  Implement user login and registration to protect the data.
* **Additional Features:**  Extend the application with features like search, pagination, sorting, and more complex data management.
* **UI Enhancements:**  Improve the user interface with better styling and design.

This README provides a basic overview of the project. Further documentation for specific functionalities or additional features can be added as needed. 


