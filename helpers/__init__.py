import os
import markdown
import json

# Helpers
# ----------------------------------


def get_application_dir(*path):
    if len(path) == 0:
        path = ['']

    #print(path)
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), '../', *path)


def get_config():
    try:
        f = open(get_application_dir('config.json'))
        config = json.load(f)
        f.close()
        return config
    except:
        raise IOError('Error reading config file')


def get_posts():
    current_dir = get_application_dir()
    posts = []
    for name in os.listdir(os.path.join(current_dir, 'posts')):
        name = os.path.splitext(name)[0]
        posts.append(get_post(name))
    return posts


def get_post(post_name):
    post = {}
    post.update(name=post_name, author=get_config()['author'])
    post_name = os.path.splitext(post_name)[0]
    current_dir = get_application_dir()
    try:
        f = open(os.path.join(current_dir, 'posts', post_name + '.md'))
        content = f.read()
        f.close()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.meta', 'markdown.extensions.fenced_code', 'markdown_checklist.extension'
        ])
        post.update(content=md.convert(content))
        post.update(title=md.Meta.get('title')[0], meta=md.Meta)
    except FileNotFoundError:
        post.update(content='<h2>404 - Post not found!<h2>')
        post.update(title='Oops!', meta={'date': ['Never! xD']})
    return post

# ----------------------------------
