from flask import jsonify, request
from model.class_model import Post


def deco_register():
    data = request.json
    new_post = Post(**data)

    new_post.register()
    new_post.created_at()

    return new_post


def deco_show():
    all_posts = Post.show_all()
    return jsonify(all_posts)


def deco_show_by_id(id):
    specific_post = Post.show_by_id(id)
    return jsonify(specific_post)


def deco_update():
    return "em fase"


def deco_delete(id):
    delete_post = Post.delete(id)
    return delete_post
