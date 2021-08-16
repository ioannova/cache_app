from app import db, app

def db_commit(model):
    if model:
        db.session.add(model)
    try:
        db.session.commit()
    except Exception as e:
        app.logger.error('[db_commit] Error: %s' % e)
        db.session.rollback()

def db_delete(model):
    if model:
        app.logger.info('[db_delete] Delete: %s' % model.key)
        db.session.delete(model)
        try:
            db.session.commit()
        except Exception as e:
            app.logger.error('[db_delete] Error: %s' % e)
            db.session.rollback()