from pymongo import MongoClient


def get_db_handle(planningServiceDB, localhost, port=27017):
    client = MongoClient(host=localhost,
                         port=port
                         )

    db_handle = client['planningServiceDB']
    return db_handle, client
