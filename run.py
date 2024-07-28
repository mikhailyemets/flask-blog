from flaskblog import app

if __name__ == '__main__':
    app.run(debug=True)

# from flaskblog import db, app
# from flaskblog.models import User, Post

# with app.app_context():
#     User.query.all()
# with app.app_context():
#     post_2 = Post(title="My Post2", content="This is a post", author=user_1)
#     db.session.add(post_2)
#     db.session.commit()
#
# with app.app_context():
#     user_1 = User.query.filter_by(username="me").first()
#     post_1 = Post.query.first()
#     post_1.author
#
# user_1 = User(username="me", email="me@mail.com", password="123")
# user_2 = User(username="notme", email="notme@mail.com", password="123")