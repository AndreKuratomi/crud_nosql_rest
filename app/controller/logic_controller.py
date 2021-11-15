from flask import jsonify, request
from app.model.class_model import Post


def deco_register():
    data = request.json
    new_post = Post(**data)

    new_post.register()
    new_post.creator()

    return new_post.__dict__


def deco_show():
    all_posts = Post.show_all()
    return jsonify(all_posts)


def deco_show_by_id(id):
    specific_post = Post.show_by_id(id)
    return jsonify(specific_post)


def deco_update(id):
    to_update = Post.update(id)
    to_update.updator()
    return jsonify(to_update)


def deco_delete(id):
    delete_post = Post.delete(id)
    return delete_post
