from flask import Flask, render_template, request, redirect, url_for, session
from datetime import date

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# Dummy data for book categories and list of books
categories = ['Fiction', 'Non-Fiction', 'Mystery']
books = {
    'Fiction': ['The Great Gatsby', 'To Kill a Mockingbird', '1984'],
    'Non-Fiction': ['Blink', 'The 7 Habits of Highly Effective People', 'Thinking, Fast and Slow'],
    'Mystery': ['The Adventures of Sherlock Holmes', 'The Da Vinci Code', 'The Girl with the Dragon Tattoo']
}

# Route for index page
@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('signup'))
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
    if 'username' not in session:
        return redirect(url_for('signup'))
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

# Route for signup page
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         # TODO: Implement logic for signing up with a username
#         return redirect(url_for('index'))
#     else:
#         return render_template('signup.html', date=date)
# Route for signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        if username not in session:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('signup.html', date=date, error='Username already taken')
    else:
        return render_template('signup.html', date=date)

@app.route('/logout')
def logout():
    if 'username' not in session:
        return redirect(url_for('signup'))
    session.pop('username', None)
    return redirect(url_for('index'))


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
