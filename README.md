Python Simple Blog
==================
Python Simple Blog is a simple Flask blog system based on markdown files which can be used both as an app or as a static site builder.

This is a WIP and may get some changes. Use it on your own risk!

Installation steps
==================
1. Clone the repository: `git clone https://github.com/mamal72/python-simple-blog`
2. Install dependencies: `[sudo] pip install flask markdown`
3. Serve the blog: `./runner serve`

You can check the `posts` directory to find out how you should write your posts.

Use as a static site builder
============================
1. Clone and install the script as mentioned above.
2. Set your hostname (Sth like `example.com`) in `config.json` file.
2. Execute `./runner build`.
3. Copy|Upload the files in the `dist` direcotory to your host or server.


Configuration
=============
There is a `config.json` file which holds most system configurations.
* debug: Flask `debug`. Useful for debug and development.
* host: Flask's `SERVER_NAME`. It's required if you want to use it as a static site builder. (To create URLS)
* title: Blog title.
* description: Blog description.
* author: Blog author.
* social: Twitter, Facebook and Github usernames of author. Used in the footer of the blog.
* post: Posts configurations and options:
..* excerpt_length: Number of posts excerpt words. (short part of the post)
..* words_count: Show posts words count in the blog.


Todo
====
- [ ] Create and distribute pip package
- [ ] Make the template more SEO friendly
- [ ] Find a good solution for contact form that works in static mode too
- [ ] Pagination
- [ ] Add some date parsing library
- [ ] YOUR AWESOME IDEAS! [Fill an issue](https://github.com/mamal72/python-simple-blog/issues)


Contribution, issues or ideas?
==============================
[Fill issues](https://github.com/mamal72/python-simple-blog/issues) or send pull requests. I'll check them ASAP.
