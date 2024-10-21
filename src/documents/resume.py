from .base_document import BaseDocument, DocTypes


class Resume(BaseDocument):
    def __init__(self, file_name: str, file_path: str, doc_type: DocTypes):
        super().__init__(file_name=file_name, file_path=file_path, doc_type=doc_type)
