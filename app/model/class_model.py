import pymongo
from datetime import datetime
from exceptions.exceptions import IncompleteRegisterError, NotFoundError

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["kenzie"]


class Post:
    def __init__(self, id: int, title: str, author: str, tags: list, content: str) -> None:
        if db.post.count_documents() == 0:
            self.id = 1
        else:
            self.id = db.post.count_documents() + 1
        self.title = title
        self.author = author
        self.content = content
        self.tags = []

    def creator(self):
        self.created_at = {"Created at": datetime.today().strftime("%d/%m/%Y %H:%M:%S %p")}
    
    def updator(self):
        self.updated_at = {"Updated at": datetime.today().strftime("%d/%m/%Y %H:%M:%S %p")}

    @staticmethod
    def show_all():
        posts_list = list(db.post.find())
        return posts_list, 200
    
    @staticmethod
    def show_by_id(id):
        try:
            found = db.post.find({"id": id})
            # if not found: #
            #     raise NotFoundError
            return found, 200

        except NotFoundError as e:
            return e.message
        # posts_list = list(db.post.find())
        # for document in posts_list:

    def register(self):
        try:
            new_post = db.post.insert_one(self.__dict__)
            # if not new_post: # new_post incompleto de algum modo
            #     raise IncompleteRegisterError
            return new_post, 201

        except IncompleteRegisterError as err:
            return err.message

    @staticmethod #vou alterar o que já existe. não preciso instanciar já que vou atualizar.
    def update(self, key):
        things_you_can_update = ['author', "title", "content", "tags"]
        try:
            if key in things_you_can_update:
                to_update = db.post.update_one(f"{key}": "")
                #como inserir aqui um updated_at?
                return to_update
            else:
                raise 

        except:

        
        pass

    @staticmethod
    def delete(id):
        try:
            delete_post = db.post.deleteOne({"id": id})
            # if not delete_post: # se nã
            #     raise NotFoundError
            return delete_post

        except NotFoundError as e:
            return e.message
 

    
