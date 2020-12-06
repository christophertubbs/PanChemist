"""
Mechanism for finding an appropriate database connector
"""

import PanChemist.DatabaseType as DatabaseType

from PanChemist.connectors._connector import _Connector
from PanChemist.connectors.postgres import PostgresDBConnector
from PanChemist.connectors.maria import MariaDBConnector
from PanChemist.connectors.sqlite import SQLiteDBConnector
from PanChemist.connectors.mongo import MongoDBConnector
from PanChemist.connectors.mssql import SqlServerConnector
from PanChemist.connectors.mysql import MySQLDBConnector


def get_connector(
            database_type: str,
            host: str = None,
            username: str = None,
            password: str = None,
            database: str = None,
            port: int = None,
            minimum_connections: int = None,
            maximum_connections: int = None
    ) -> _Connector:
    if database_type == DatabaseType.POSTGRES:
        constructor = PostgresDBConnector
    elif database_type == DatabaseType.SQLITE:
        constructor = SQLiteDBConnector
    elif database_type == DatabaseType.SQL_SERVER:
        constructor = SqlServerConnector
    elif database_type == DatabaseType.MARIADB:
        constructor = MariaDBConnector
    elif database_type == DatabaseType.MONGODB:
        constructor = MongoDBConnector
    elif database_type == DatabaseType.MYSQL:
        constructor = MySQLDBConnector
    else:
        raise ValueError('"{}" is not a supported database type.'.format(database_type))

    return constructor(
            host,
            username,
            password,
            database,
            port,
            minimum_connections,
            maximum_connections
    )
