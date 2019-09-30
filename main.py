
import random
from bottle import Bottle, template, static_file, request, redirect, abort

import model
import session

app = Bottle()


@app.route('/')
def index(db):

    info = {
        'title': "The WT Store"
    }

    return template('index', info)


@app.route('/static/<filename:path>')
def static(filename):
    return static_file(filename=filename, root='static')


if __name__ == '__main__':

    from bottle import run
    from bottle.ext import sqlite, beaker
    from dbschema import DATABASE_NAME
    # install the database plugin
    app.install(sqlite.Plugin(dbfile=DATABASE_NAME))

    # install beaker
    session_opts = {
        'session.type': 'memory',
    }
    beaker_app = beaker.middleware.SessionMiddleware(app, session_opts)
    run(app=beaker_app, debug=True, port=8010)
