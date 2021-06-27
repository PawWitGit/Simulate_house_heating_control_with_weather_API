class PgDatabase:
    def __init__(
        self, db_name, db_user, db_pass, db_host, db_port, id, temp_data, temp_value
    ):
        self.db_name = db_name
        self.db_user = db_user
        self.db_host = db_host
        self.db_pass = db_pass
        self.db_port = db_port
        self.id = id
        self.temp_data = temp_data
        self.temp_value = temp_value
