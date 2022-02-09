class ProcessManager():
    def __init__(self, api_connector, db_connector) -> None:
        self._ac = api_connector
        self._dc = db_connector

    def transfer_by_parameter(self):
        self._dc.store_in_db(self._ac.get_from_api())


class ApiConnector():
    def __init__(self, api) -> None:
        self._api = api

    def get_from_api(self):
        return self._api.get()


class Api():
    def __init__(self) -> None:
        pass

    def get(self):
        return "Api data"


class DatabaseConnector():
    def __init__(self, database) -> None:
        self._database = database

    def store_in_db(self, data):
        self._database.store(data)


class Database():
    def __init__(self) -> None:
        pass

    def store(self, data):
        print(f"Stored data '{data}'.")


def main():
    api = Api()
    api_connector = ApiConnector(api=api)

    database = Database()
    db_connector = DatabaseConnector(database=database)

    pm = ProcessManager(api_connector=api_connector, db_connector=db_connector)
    pm.transfer_by_parameter()


if __name__ == "__main__":
    main()
