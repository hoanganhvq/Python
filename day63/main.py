#SQLITE
# from flask import Flask, render_template, request, redirect, url_for
# import sqlite3
#
# #Create database
# db = sqlite3.connect("book-collection.db")
# # a cursor is also known as the mouse or pointer.
# # If we were working in Excel or Google Sheet, we would be using the cursor to add rows of data or edit/delete data,
# # we also need a cursor to modify our SQLite database.
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
# app = Flask(__name__)
#
# all_books = []
#
#
# @app.route('/')
# def home():
#     return render_template("index.html", books=all_books)
#
# @app.route("/add")
# def add():
#     if request.method == "POST":
#         new_book = {
#             "title": request.form["title"],
#             "author": request.form["author"],
#             "rating": request.form["rating"]
#         }
#         all_books.append(new_book)
#         return redirect(url_for('home'))
#     return render_template("add.html")
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
#
#SQLALCHEMY
#
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

##CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()


