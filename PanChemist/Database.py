#!/bin/env python
import os
import io
import csv
import typing

import pandas

import pandas.io.sql as sql

import PanChemist.DatabaseType as DatabaseType
import PanChemist.connectors.connectors as connectors


class Database(object):
    def __init__(
            self,
            database_type: str,
            host: str = None,
            username: str = None,
            password: str = None,
            database: str = None,
            port: int = None,
            minimum_connections: int = None,
            maximum_connections: int = None
    ):
        self.__connector = connectors.get_connector(
            database_type=database_type,
            host=host,
            username=username,
            password=password,
            database=database,
            port=port,
            minimum_connections=minimum_connections,
            maximum_connections=maximum_connections
        )

    def read(self, query: str, parameters: typing.Dict[str, str] = None) -> pandas.DataFrame:
        with self.__connector.get_connection() as connection:
            return sql.read_sql_query(query, connection, params=parameters)

    def execute(self, query: str, parameters: dict = None):
        with self.__connector.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, vars=parameters)

    def execute_many(self, query: str, parameters: typing.List[typing.Dict[str, str]] = None):
        with self.__connector.get_connection() as connection:
            with connection.cursor() as cursor:
                for arguments in parameters:
                    cursor.execute(query, vars=arguments)

    def import_dataframe(self, frame: pandas.DataFrame, table_name: str):
        buffer = io.StringIO()
        frame.to_csv(buffer, sep=',')
        buffer.seek(0)
        reader = csv.DictReader(buffer)

        fieldnames = [name for name in reader.fieldnames if name != '']

        insert_header = "INSERT INTO {} ({}) VALUES {}".format(table_name, ",".join(fieldnames), os.linesep)
        placeholders = ["%(" + name + ")s" for name in fieldnames]
        insert_header += " (" + ", ".join(placeholders) + ")"

        with self.__connector.get_connection() as connection:
            with connection.cursor() as cursor:
                for row in reader:
                    params = dict()

                    for field in fieldnames:
                        if str(row[field]) == '':
                            params[field] = None
                        else:
                            params[field] = row[field]

                    cursor.execute(insert_header, params)
                connection.commit()

    def copy_dataframe(self, frame: pandas.DataFrame, table_name: str, commit_cutoff: int=None):
        """
        Perform a high speed data copy

        :param frame: The data to copy
        :param table_name: The name of the table to copy into
        :param commit_cutoff: The number of rows that may be copied at a time
        :return:
        """
        if self.__connector.database_type() == DatabaseType.POSTGRES:
            self.__connector.copy_dataframe(frame, table_name, commit_cutoff)
        return self.import_dataframe(frame, table_name)

    def create_table(self, table_name: str, frame: pandas.DataFrame) -> bool:
        """
        :param table_name: The name of the newly created table
        :param frame: Details of what to create
        :return Whether or not the table was created
        """
        # TODO: Implement Database.create_table()
        pass

    def get_database_details(self) -> pandas.DataFrame:
        """
        :return: A dataframe containing all views and tables
        """
        # TODO: Implement Database.get_database_details()
        pass

    def get_table_schema(self, table_name) -> pandas.DataFrame:
        """
        :param table_name: The name of the table
        :return:
        """
        # TODO: Implement Database.get_table_schema()
        pass
