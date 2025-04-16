from chatterbot.storage import SQLStorageAdapter
from sqlalchemy import create_engine

class CustomSQLStorageAdapter(SQLStorageAdapter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.engine = create_engine(
            self.database_uri,
            pool_size=20,         
            max_overflow=20,      
            connect_args={"check_same_thread": False}
        )
