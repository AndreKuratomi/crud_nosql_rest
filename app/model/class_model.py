import pymongo
from flask import jsonify
from datetime import datetime
from exceptions.exceptions import NotFoundError
from ipdb import set_trace

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["kenzie"]


class Post:
    def __init__(self, title: str, author: str, tags: list, content: str) -> None:
        self.id = self.create_id()
        self.title = title
        self.author = author
        self.content = content
        self.tags = tags
        self.created_at = datetime.today().strftime("%d/%m/%Y %H:%M:%S %p")

    def create_id(self):
        arr = list(db.posts.find())
        if arr:
            return arr[-1]['id'] + 1
            
        else:
            return 1

    def updator(self):
        self.updated_at = {"Updated at": datetime.today().strftime("%d/%m/%Y %H:%M:%S %p")}

    @staticmethod
    def show_all():
        try:
            posts_list = db.posts.find()

            if not posts_list:
                raise NotFoundError

            posts = []
            for post in posts_list:
                del post['_id']
                posts.append(post)

            return jsonify(posts), 200

        except NotFoundError as e:
            return e.message, 404

    @staticmethod
    def show_by_id(id):
        try:
            arr = db.posts.find()
            for found in arr:
                if found['id'] == int(id):
                    del found['_id']

                    return jsonify(found), 200
            else:
                raise NotFoundError

        except NotFoundError as e:
            return e.message, 404

    def register(self):
        db.posts.insert_one(self.__dict__)

    @staticmethod
    def update(id):
        try:
            to_update = db.posts.update_one({"id": id})
            return to_update, 204

        except:
            ...

    @staticmethod
    def delete(id):
        try:
            surv_arr = []

            arr = db.posts.find()
            for to_delete in arr:
                if to_delete['id'] == int(id):
                    del to_delete['_id']
                    surv_arr.append(to_delete)
                    db.posts.find_one_and_delete(to_delete)

                    return jsonify(surv_arr), 200
                    # dúvida no porquê de estar retornando uma lista mesmo com o jsonify
            else:
                raise NotFoundError

        except NotFoundError as e:
            return e.message, 404
