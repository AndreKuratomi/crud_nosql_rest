import pymongo
from datetime import datetime
from exceptions.exceptions import IncompleteRegisterError, NotFoundError, WrongTypesError

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["kenzie"]


class Post:
    def __init__(self, id: int, title: str, author: str, tags: list, content: str) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.content = content
        self.tags = tags # ???

    def creator(self):
        self.created_at = {"Created at": datetime.today().strftime("%d/%m/%Y %H:%M:%S %p")}

    def updator(self):
        self.updated_at = {"Updated at": datetime.today().strftime("%d/%m/%Y %H:%M:%S %p")}

    @staticmethod
    def show_all():
        try:
            posts_list = list(db.posts.find())
            if not posts_list:
                raise NotFoundError
            return posts_list, 200
        except NotFoundError as e:
            return e.message, 404

    @staticmethod
    def show_by_id(id):
        try:
            found = db.posts.find({"id": id})
            if not found:
                raise NotFoundError
            return found, 200

        except NotFoundError as e:
            return e.message, 404

    def register(self):
        try:
            new_post = db.posts.insert_one(self.__dict__).inserted_id
            
            if not new_post:
                raise IncompleteRegisterError
            elif type(self.title) != str or type(self.author) != str or type(self.content) != str:
                raise WrongTypesError
                
            return new_post, 201

        except IncompleteRegisterError as err:
            return err.message

        except WrongTypesError as err:
            return err.message

    @staticmethod
    def update(id):
        try:
            to_update = db.posts.update_one({"id": id})
            return to_update, 204

        # except:
        #     raise 

    @staticmethod
    def delete(id):
        try:
            delete_post = db.posts.deleteOne({"id": id})
            if not delete_post:
                raise NotFoundError
            return delete_post, 204

        except NotFoundError as e:
            return e.message, 404
