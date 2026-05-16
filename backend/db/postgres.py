def get_engine(database_url: str):
    from sqlalchemy import create_engine

    return create_engine(database_url)
