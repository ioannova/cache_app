from app import app, db
from app.models import Cache
from app.utils import db_delete

from flask_script import Manager

manager = Manager(app)

@manager.command
def delete_all_no_expiration():
    app.logger.info('Init delete_all_no_expiration')
    for expirated in Cache.query.filter_by(no_expiration=True):
        db.session.remove(expirated)
        db.session.commit()
    app.logger.info('Done delete_all_no_expiration')

if __name__ == "__main__":
    manager.run()
