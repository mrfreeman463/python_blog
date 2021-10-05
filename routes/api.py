from app import db
from flask import Blueprint, request
from controllers.ArticlesController import ArticlesController

api = Blueprint("api", __name__)

@api.route("/api/articles/list", methods=["GET"])
def getArticles():
    return ArticlesController.list()

@api.route("/api/articles/store", methods=["POST"])
def storeArticle():
    return ArticlesController.store()

@api.route("/api/articles/update", methods=["POST"])
def updateArticle():
    return ArticlesController.update()

@api.route("/api/articles/delete", methods=["POST"])
def deleteArticle():
    return ArticlesController.delete()