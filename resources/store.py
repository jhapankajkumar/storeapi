from flask_restful import Resource, reqparse
from models.store import  StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "No record found"}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A store with name '{}' already exists.".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "Error occured while creating store"}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name=name)
        if store is None:
            return {"message": "Store does exists"}, 400
        store.delete_from_db()
        return {"message": "Store deleted"}, 200


class StoreList(Resource):
    def get(self):
        stores = StoreModel.get_all_stores()
        return {'stores': stores}

