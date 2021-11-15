class NotFoundError(Exception):
    def __init__(self):
        self.message = {"message": "Não encontrado ou inexistente!"}
        super.__init__(self.message)


class IncompleteRegisterError(Exception):
    def __init__(self):
        self.message = {"message": "JSON incompleto!"}
        super.__init__(self.message)


class WrongTypesError(Exception):
    types = {
        str: "string",
        int: "integer",
        float: "float",
        bool: "boolean",
        list: "list",
        dict: "dict"
    }

    def __init__(self, title, author, tags, content):
        self.message = {
            "received fields": [
                {
                    "title": f"{self.types[type(title)]}"
                },
                {
                    "author": f"{self.types[type(author)]}"
                },
                # {
                #     "tags": f"{self.types[type(tags)]}"
                # },
                {
                    "content": f"{self.types[type(content)]}"
                }
            ]
        }
        super().__init__(self.message)
