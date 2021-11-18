from flask import jsonify, request
from ipdb import set_trace
from app.model.class_model import Post
from exceptions.exceptions import IncompleteRegisterError, NotFoundError, WrongTypesError


def deco_register():
    valid_keys = {"title", "author", "content", "tags"}
    try:
        data = request.json
        data_keys = data.keys()
        set_data = set(data_keys)
        comparison = valid_keys.difference(set_data)

        if comparison != set():
            raise IncompleteRegisterError

        # elif type(data['title']) != str or type(data['author']) != str or type(data['tags']) != list or type(data['content']) != str:
        #     raise WrongTypesError(data['title'], data['author'], data['tags'], data['content'])

        else:
            new_object = Post(**data)
            new_object.register()
            new_post = new_object.__dict__
            del new_post["_id"]

            return new_post, 201

    except IncompleteRegisterError as err:
        return err.message

    except WrongTypesError as err:
        return err.message


def deco_show():
    all_posts = Post.show_all()
    return all_posts


def deco_show_by_id(id):
    specific_post = Post.show_by_id(id)
    return specific_post


def deco_update(id):
    to_update = Post.update(id)
    # set_trace()
    # to_update.updator()
    return to_update


def deco_delete(id):
    to_delete = Post.delete(id)
    return to_delete
