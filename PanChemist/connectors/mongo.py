"""
Manages and creates connections to MongoDB instances
"""

import PanChemist.connectors._connector as _connector
import PanChemist.DatabaseType as DatabaseType


class MongoDBConnector(_connector._Connector):
    """
    Manages and creates connections to MongoDB instances
    """

    @staticmethod
    def database_type():
        return DatabaseType.MONGODB

    def __init__(self, host: str, username: str, password: str, database: str, port: int, **kwargs):
        raise NotImplementedError("The PanChemist MongoDB connector has not been implemented")

    def get_connection(self):
        raise NotImplementedError("The PanChemist MongoDB connector has not been implemented")

    def get_version(self) -> str:
        raise NotImplementedError("The PanChemist MongoDB connector has not been implemented")

    def get_table_schema_query(self) -> str:
        raise NotImplementedError("The PanChemist MongoDB connector has not been implemented")

    def get_database_details_query(self) -> str:
        raise NotImplementedError("The PanChemist MongoDB connector has not been implemented")
