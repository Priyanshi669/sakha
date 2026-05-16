def get_client(path: str):
    from chromadb import PersistentClient

    return PersistentClient(path=path)
