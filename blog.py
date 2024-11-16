
  
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr_sqlalchemy.auth import login_required
from flaskr_sqlalchemy.db import get_db  # Import the get_db function
from flaskr_sqlalchemy.models import User, Post  # Import the User and Post models

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()  # Get the database connection
    # Join Post and User, explicitly selecting the columns you need
    posts = (
        db.query(Post)
        .join(User)
        .add_columns(User.username)
        .order_by(Post.created.desc())
        .all()
    )
    # Map the result into a more usable format
    post_data = [{'post': post, 'username': username} for post, username in posts]
    return render_template('blog/index.html', posts=post_data)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            new_post = Post(title=title, body=body, author_id=g.user.id)  # Use SQLAlchemy model
            db = get_db()  # Get the database connection
            db.add(new_post)  # Add the new post to the session
            db.commit()  # Commit the session to save changes
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')

def get_post(id, check_author=True):
    db = get_db()  # Get the database connection
    # Fetch the post along with the user information
    post = (
        db.query(Post)
        .join(User)
        .filter(Post.id == id)
        .add_columns(User.username)
        .first()
    )  # Use SQLAlchemy to get the Post object and the username

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    # The post is now a tuple, with the Post object as the first element
    post_obj, username = post  # Unpack the tuple

    if check_author and post_obj.author_id != g.user.id:  # Access author_id directly
        abort(403)

    return post_obj, username  # Return the post object and username

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post, username = get_post(id)  # Get the post object and username

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            post.title = title  # Update title
            post.body = body    # Update body
            db = get_db()  # Get the database connection
            db.commit()  # Commit changes to the database
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post, username=username)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    post, _ = get_post(id)  # Get the post object
    db = get_db()  # Get the database connection
    db.delete(post)  # Use SQLAlchemy to delete the post
    db.commit()  # Commit the changes
    return redirect(url_for('blog.index'))

