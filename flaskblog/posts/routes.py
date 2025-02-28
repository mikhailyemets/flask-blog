from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm
posts = Blueprint("posts", __name__)

@posts.route("/post/new", methods=["GET", "POST"])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            content=form.content.data,
            user_id=current_user.id
        )
        db.session.add(post)
        db.session.commit()
        flash("Post has been created!", "success")
        return redirect(url_for("main.home"))
    return render_template(
        'create_post.html',
        title='New post',
        form=form,
        legend="New post",
        submit="Post"
    )

@posts.route("/post/<int:post_id>")
def post(post_id: int):
    post = Post.query.get_or_404(post_id)
    return render_template(
        "post.html",
        title=post.title,
        post=post
    )


@posts.route("/post/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def update_post(post_id: int):
    post = Post.query.get_or_404(post_id)
    if post.user_id != current_user.id:
        abort(403)

    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Post has been updated!", "success")
        return redirect(url_for("posts.post", post_id=post.id))

    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content

    return render_template(
        "create_post.html",
        title="Update post",
        form=form,
        legend="Update post",
        submit="Update"
    )

@posts.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id: int):
    post = Post.query.get_or_404(post_id)
    if post.user_id != current_user.id:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Post has been deleted!", "success")
    return redirect(url_for("main.home"))


@posts.route('/latest_posts')
def latest_posts():
    posts = Post.query.order_by(Post.date_posted.desc()).limit(2).all()
    return render_template('latest_posts.html', posts=posts)