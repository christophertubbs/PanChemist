"""
Manages and creates connections to PostgreSQL instances
"""
import io
import logging
import typing
import multiprocessing

import pandas
import psycopg2
import psycopg2.pool

import PanChemist.connectors._connector as _connector
import PanChemist.DatabaseType as DatabaseType


def _copy_dataframe(connector, table_name: str, iteration: int, subset: pandas.DataFrame) -> bool:
    buffer = io.StringIO()
    subset.to_csv(buffer, sep="|", header=False, index=False, na_rep="NULL")
    buffer.seek(0)
    try:
        with connector.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.copy_from(buffer, table_name, sep="|", columns=list(subset.keys()), null="NULL")
            connection.commit()
            logging.debug(
                "PanChemist Copy: Subset chunk {} has been copied to {}".format(iteration, table_name)
            )
            return True
    except Exception as e:
        logging.error(
            "PanChemist Copy: An error occured when copying subset chunk {} to {}".format(
                iteration,
                table_name
            )
        )
        logging.error(e)
        return False


class PostgresDBConnector(_connector._Connector):
    """
    Manages and creates connections to PostgreSQL instances
    """

    @staticmethod
    def database_type():
        return DatabaseType.POSTGRES

    def __init__(
            self,
            host: str = None,
            username: str = None,
            password: str = None,
            database: str = None,
            port: int = None,
            minimum_connections: int = None,
            maximum_connections: int = None,
            **kwargs
    ):
        self.__pool = psycopg2.pool.ThreadedConnectionPool(
            minconn=minimum_connections if minimum_connections else 1,
            maxconn=maximum_connections if maximum_connections else 1,
            user=username if username else "postgres",
            password=password if password else "postgres",
            host=host if host else 'localhost',
            port=port if port else 5432,
            database=database if database else "postgres"
        )
        self.version = None

    def get_connection(self):
        return self.__pool.getconn()

    def get_version(self) -> typing.Union[None, str]:
        if self.version is None:
            try:
                with self.get_connection() as connection:
                    with connection.cursor() as cursor:
                        cursor.execute("SELECT version();")
                        self.version = cursor.fetchone()[0]
            except Exception:
                return None
        return self.version

    def copy_dataframe(self, frame: pandas.DataFrame, table_name: str, commit_cutoff: int=None):

        if commit_cutoff is None or commit_cutoff < 1:
            commit_cutoff = 50000

        row_count = frame.index.size

        chunks = row_count // commit_cutoff

        if row_count % commit_cutoff != 0:
            chunks += 1

        copy_attempts = list()
        get_attempt_count = {chunk: 0 for chunk in range(chunks)}
        completions = {chunk: False for chunk in range(chunks)}
        get_limit = 50

        with multiprocessing.Pool() as pool:
            for chunk in range(chunks):
                subset = frame.iloc[chunk * commit_cutoff:chunk * commit_cutoff + commit_cutoff]

                copy_attempts.append(
                    (chunk, pool.apply_async(_copy_dataframe, args=(table_name, chunk, subset,))))

            while len(copy_attempts) > 0:
                chunk, attempt = copy_attempts.pop(0)

                try:
                    completions[chunk] = attempt.get(500)

                    if not attempt.successful():
                        raise Exception(
                            "Data for chunk {} could not be copied to the {} table".format(chunk, table_name))
                except TimeoutError as error:
                    get_attempt_count[chunk] += 1
                    logging.debug(error)

                    if get_attempt_count[chunk] > get_limit:
                        logging.error("Data could not be copied to the database")
                        raise

                    logging.debug("Will try chunk {} again".format(chunk))
                    copy_attempts.append((chunk, attempt))

    def get_table_schema_query(self) -> str:
        # TODO: Implement PostgresDBConnector.get_table_schema_query
        pass

    def get_database_details_query(self) -> str:
        # TODO: Implement PostgresDBConnector.get_database_details_query
        pass

    def __del__(self):
        self.__pool.closeall()

    def __repr__(self):
        return self.get_version()

    def __str__(self):
        return self.get_version()
