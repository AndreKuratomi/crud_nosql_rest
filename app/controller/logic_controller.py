from datetime import datetime
from flask import request
from ipdb import set_trace
from app.model.class_model import Post
from exceptions.exceptions import IncompleteSendError, NotFoundError

valid_keys = {"title", "author", "content", "tags"}
updating_valid_keys = {'author', 'id', 'title', 'content', 'tags', 'created_at', 'updated_at'}


def deco_register():
    try:
        data = request.json
        data_keys = data.keys()
        set_data = set(data_keys)
        comparison = valid_keys.difference(set_data)

        if comparison != set():
            raise IncompleteSendError

        else:
            new_object = Post(**data)
            new_object.register()
            new_post = new_object.__dict__
            del new_post["_id"]

            return new_post, 201

    except IncompleteSendError as err:
        return err.message, 400


def deco_show():
    all_posts = Post.show_all()
    return all_posts


def deco_show_by_id(id):
    specific_post = Post.show_by_id(id)
    return specific_post


def deco_update(id):
    try:
        data = request.json
        to_update = Post.update(id, data)

        if not to_update:
            raise NotFoundError

        new_dict = to_update[0]
        new_dict['updated_at'] = datetime.today().strftime("%d/%m/%Y %H:%M:%S %p")

        set_new_dict_keys = set(new_dict.keys())
        comparison = set_new_dict_keys.difference(updating_valid_keys)

        if comparison != set():
            raise IncompleteSendError

        return new_dict, 201

    except NotFoundError as e:
        return e.message, 404

    except IncompleteSendError as err:
        return err.message, 400


def deco_delete(id):
    to_delete = Post.delete(id)
    return "", 204
