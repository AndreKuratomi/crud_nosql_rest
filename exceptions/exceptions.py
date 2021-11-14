class NotFoundError(Exception):
    def __init__(self):
        self.message = {"message": "Não encontrado ou inexistente!"}
        super.__init__(self.message)


class IncompleteRegisterError(Exception):
    def __init__(self):
        self.message = {"message": "JSON incompleto!"}
        super.__init__(self.message)


class WrongRegisterError:
    pass
