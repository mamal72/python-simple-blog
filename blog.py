from flask import Flask, render_template, request
import helpers


# Init
# ----------------------------------

app = Flask(__name__)
app.config.update(blog=helpers.get_config())
app.config.update(SERVER_NAME=app.config['blog']['host'])
app.debug = app.config['blog']['debug']
# ----------------------------------


# Routes
# ----------------------------------

@app.route('/')
def index():
    posts = helpers.get_posts()
    return render_template('index.html', posts=posts)


@app.route('/<post_name>')
def show_post(post_name):
    post = helpers.get_post(post_name)
    return render_template('post.html', **post)


@app.route('/contact')
def contact():
    if request.method == 'POST':
        return 'POSTED!'
    return render_template('contact.html', title='contact')

# ----------------------------------


# Run
# ----------------------------------

if __name__ == '__main__':
    app.run()

# ----------------------------------
