from __future__ import annotations
from rich import print
from .db.database import KnowledgeBaseBase, DefaultBase
from .configs.dev import Config

class CryptFlowsApp:
    
    def __init__(self) -> None:
        # load config
        self.config = Config()
        # load db
        self.knowledge_base = KnowledgeBaseBase.metadata.create_all(KnowledgeBaseBase.engine)
        self.default_base = DefaultBase.metadata.create_all(DefaultBase.engine)
        print("Database created successfully!")
        
        