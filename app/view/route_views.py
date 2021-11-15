from flask import Flask
from app.controller.logic_controller import deco_delete, deco_register, deco_show, deco_show_by_id, deco_update


def init_app(app: Flask):

    app.post("/posts")(deco_register)

    app.get("/posts")(deco_show)

    app.get("/posts/<id>")(deco_show_by_id)

    app.patch("/posts/<id>")(deco_update)

    app.delete("/posts/<id>")(deco_delete)
