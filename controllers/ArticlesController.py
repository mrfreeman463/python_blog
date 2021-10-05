from flask.json import jsonify
from app import db
from flask import redirect, abort, render_template, url_for, request
from models.Articles import Articles

class ArticlesController():

    def list():
        articles = Articles.query.all()
        response = []
        for value in articles:
            item = {
                "title": value.title,
                "content": value.content
            }
            response.append(item)

        return str(response)

    def store():
        title = request.form["title"]
        content = request.form["content"]

        article = Articles(title=title, content=content)
        db.session.add(article)
        db.session.commit()

        return "Article was store: " + str(article.id)

    def update():
        article_id = request.form["article_id"]        

        if request.form["title"] is not None:
            title = request.form["title"]

        if request.form["content"] is not None:
            content = request.form["content"]

        article = Articles.query.get(article_id)
        article.title = title
        article.content = content

        db.session.commit()

        return "Article was update: " + str(article.id)

    def delete():
        article_id = request.form["article_id"]

        article = Articles.query.get(article_id)
        db.session.delete(article)
        db.session.commit()

        return "Article was delete: " + str(article_id)
