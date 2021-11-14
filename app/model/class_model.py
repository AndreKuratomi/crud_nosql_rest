import pymongo
from datetime import datetime
from exceptions.exceptions import IncompleteRegisterError, NotFoundError

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["kenzie"]


class Post:
    def __init__(self, id: int, title: str, author: str, tags: list, content: str) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.content = content
        self.tags = tags

    def creator(self):
        self.created_at = {"Created at": datetime.today().strftime("%d/%m/%Y %H:%M:%S %p")}

    def updator(self):
        self.updated_at = {"Updated at": datetime.today().strftime("%d/%m/%Y %H:%M:%S %p")}

    @staticmethod
    def show_all():
        try:
            posts_list = list(db.post.find())
            if not posts_list:
                raise NotFoundError
            return posts_list, 200
        except NotFoundError as e:
            return e.message, 404

    @staticmethod
    def show_by_id(id):
        try:
            found = db.post.find({"id": id})
            if not found:
                raise NotFoundError
            return found, 200

        except NotFoundError as e:
            return e.message, 404

    def register(self):
        try:
            new_post = db.post.insert_one(self.__dict__).inserted_id
            if not new_post:
                raise IncompleteRegisterError
            return new_post, 201

        except IncompleteRegisterError as err:
            return err.message

    # @staticmethod #vou alterar o que já existe. não preciso instanciar já que vou atualizar.
    # def update(self, key):
    #     things_you_can_update = ['author', "title", "content", "tags"]
    #     try:
    #         if key in things_you_can_update:
    #             to_update = db.post.update_one(f"{key}": "")
    #             #como inserir aqui um updated_at?
    #             return to_update, 204
    #         else:
    #             raise 

    #     except:

    @staticmethod
    def delete(id):
        try:
            delete_post = db.post.deleteOne({"id": id})
            if not delete_post:
                raise NotFoundError
            return delete_post, 204

        except NotFoundError as e:
            return e.message, 404
