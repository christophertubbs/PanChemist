"""
Represents the absolute base functionality for a connector to the database
"""

import abc


class _Connector(abc.ABC):
    """
    Represents the absolute base functionality for a connector to the database
    """

    @abc.abstractmethod
    def get_connection(self):
        pass

    @staticmethod
    @abc.abstractmethod
    def database_type() -> str:
        pass

    def can_connect(self) -> bool:
        return self.get_version() is not None

    def copy_dataframe(self, frame, table_name: str, commit_cutoff: int=None):
        raise NotImplementedError("Only a postgres connector may perform a high speed copy")

    @abc.abstractmethod
    def get_version(self) -> str:
        pass

    @abc.abstractmethod
    def get_table_schema_query(self) -> str:
        pass

    @abc.abstractmethod
    def get_database_details_query(self) -> str:
        pass
