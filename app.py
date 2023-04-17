from flask import Flask, render_template, request, redirect, url_for, session
from datetime import date
DEFAULT_PASSWORD = 'admin'

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# # Dummy data for book categories and list of books

import string
import random

# Dummy data for book categories and list of books
categories = ['Hospitality', 'Civil', 'Chemistry', 'Physics', 'Dictionaries', 'Mechanical', 'Fashion Design', 'Misc', 'Law', 'Electronics'] 
books = {
        'Hospitality': [], 'Civil':[], 'Chemistry':[], 'Physics':[], 'Dictionaries':[], 'Mechanical':[], 'Fashion Design':[], 'Misc':[], 'Law':[], 'Electronics':[]
}

# Function to generate random book names
def generate_book_name():
    # Generate a random string of length between 5 to 15 characters
    length = random.randint(5, 15)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

# Populate the books dictionary with random book names
for category in categories:
    for i in range(10):  # Generate 10 books per category
        book_name = generate_book_name()
        books[category].append(book_name)

# categories = ['Hospitality', 'Civil', 'Chemistry', 'Physics', 'Dictionaries', 'Mechanical', 'Fashion Design', 'Misc', 'Law', 'Electronics'] 
# books = {
#         'Hospitality': [], 'Civil':[], 'Chemistry':[], 'Physics':[], 'Dictionaries':[], 'Mechanical':[], 'Fashion Design':[], 'Misc':[], 'Law':[], 'Electronics':[]
# }

# Default admin username and password
default_username = 'admin'
default_password = 'password'

# Route for index page
@app.route('/')
def index():
    return render_template('index.html', date=date)

#Route for search functionality
@app.route('/search')
def search():
    query = request.args.get('q')
    results = []
    for category in categories:
        for book in books[category]:
            if query.lower() in book.lower():
                results.append((book, category))
    return results

# Route for list page
@app.route('/list', methods=['GET', 'POST'])
def book_list():
    if session.get('username') != default_username:
        return redirect(url_for('login'))
    if request.method == 'POST':
        category = request.form['category']
        book_name = request.form['book_name']
        if category not in categories:
            categories.append(category)
            books[category] = []
        books[category].append(book_name)
        return redirect(url_for('book_list', category=category))
    else:
        selected_category = request.args.get('category', categories[0])
        return render_template('list.html', categories=categories, selected_category=selected_category, book_list=books[selected_category], date=date)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == DEFAULT_PASSWORD:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', date=date, error='Invalid username or password')
    else:
        return render_template('login.html', date=date)


@app.route('/logout')
def logout():
    if session.get('username') != default_username:
        return redirect(url_for('login'))
    session.pop('username', None)
    return redirect(url_for('index'))


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
