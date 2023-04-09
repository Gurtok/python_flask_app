from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
from werkzeug.exceptions import abort





def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    db_connection = get_db_connection()
    post = db_connection.execute('SELECT * FROM posts WHERE id = ?',
                                 (post_id,)).fetchone()
    db_connection.close()
    #print(post)
    if post is None:
        abort(404)
    return post







app = Flask(__name__)

web_host="localhost"
web_port="5001"
app.config['SECRET_KEY'] = 'harocolorado'

# Base Index
@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

# View Post by ID
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

# Create Post and insert into DB
@app.route('/create', methods=('GET', 'POST') )
def create():
        if request.method == 'POST':
             title = request.form['title']
             content = request.form['content']

             if not title:
                  flash('Title is required')
             else:
                  conn = get_db_connection()
                  conn.execute('INSERT INTO posts (title, content) VALUES (?,?)',
                               (title, content))
                  conn.commit()
                  conn.close()
                  return redirect(url_for('index'))
        return render_template('create.html')


# Edit Post by ID and insert to DB
@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)
    print( request.method )

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        #print(title)
        #print(content)
         
        if not title:
            flash('Title is required')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            #print(title)
            #print(content)
            return redirect( url_for('index'))
        
    return render_template( 'edit.html', post=post)


# Delete a post

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully delete!',format( post['title'] ))
    return redirect( url_for('index'))
                           

if __name__ == '__main__':
    app.run(host='localhost',port=web_port)