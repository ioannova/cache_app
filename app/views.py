from app import app
from app.utils import db_commit, db_delete
from app.models import Cache
from flask import request, abort, jsonify

@app.route('/<string:_key>', methods=['GET', 'POST', 'DELETE'])
def root(_key):
    if len(_key) > 64:
        return jsonify(erro='Key max length is 64'), 406

    if request.method == 'GET' and _key:
        element = Cache.query.filter_by(key=_key).first()
        if element:
            return jsonify(data=element.value)
        else:
            return jsonify(data=False), 404
    
    elif request.method == 'POST' and _key:
        value = request.json.get('data')

        if value is None or len(value) > 512:
            return jsonify(erro='Data max length is 512'), 406

        element = Cache.query.filter_by(key=_key).first()
        if request.json.get('force') and element:
            element = Cache.query.filter_by(key=_key).first()
            if element:
                element.value = value
                db_commit(element)
                return jsonify(data=True), 200

        elif not element:
            db_commit(Cache(key=_key, value=value))
            return jsonify(data=True)

        return jsonify(data=False), 406

    elif request.method == 'DELETE' and _key:
        element = Cache.query.filter_by(key=_key).first()
        if element:
            db_delete(element)
            return jsonify(data=True)
        return jsonify(data=False)


    return jsonify(erro='Invalid request'), 400
