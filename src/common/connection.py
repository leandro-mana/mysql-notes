"""Database connection utilities for Jupyter notebooks.

Provides helper functions to establish MySQL connections using JupySQL magic.
"""

# Connection string for the MySQL Docker container
MYSQL_CONNECTION_STRING = "mysql+pymysql://root:root_password@localhost:3306/mysql_notes"


def get_connection_string() -> str:
    """Return the MySQL connection string for JupySQL.

    Returns:
        MySQL connection string for the Docker container.
    """
    return MYSQL_CONNECTION_STRING
