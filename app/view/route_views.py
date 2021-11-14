from flask import Flask
from app.controller.logic_controller import deco_delete, deco_register, deco_show, deco_show_by_id, deco_update


def init_app(app: Flask):

    app.post("/post")(deco_register)

    app.get("/post")(deco_show)

    app.get("post/<int:id>")(deco_show_by_id)

    app.patch("/update")(deco_update)

    app.delete("/delete/<int:id>")(deco_delete)
