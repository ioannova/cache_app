# -*- encoding: utf-8 -*-

from flask_migrate import Migrate
from app import app, db
from app.settings import Development, Production
import sqlite3

# Alembic
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run()

def reset():
    from os import system, getcwd, path
    import sqlite3

    system('rm %s' % path.join(os.getcwd(), 'app/database.db'))
    system('rm -rf %s' % path.join(os.getcwd(), 'migrations'))
    sqlite3.connect('%s' % path.join(os.getcwd(), 'app/database.db'))
    system('%s db init' % path.join(os.getcwd(), 'env/bin/flask'))
    system('%s db migrate -m "initial"' % path.join(os.getcwd(), 'env/bin/flask'))
    system('%s db upgrade' % path.join(os.getcwd(), 'env/bin/flask'))
