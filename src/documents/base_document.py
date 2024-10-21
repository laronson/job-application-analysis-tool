from langchain_core.documents import Document
from langchain.document_loaders import TextLoader
from typing import Literal, List

DocTypes = Literal["docx", "pdf", "text"]


class BaseDocument:
    def __init__(self, file_name: str, file_path: str, doc_type: DocTypes):
        self.file_name = file_name
        self.file_path = file_path
        self.doc_type: DocTypes = doc_type

    def document_from_text(self) -> Document:
        if self.doc_type != "text":
            raise Exception(
                f"Invalid Document type: trying to convert from text when document type is: {self.doc_type}"
            )

        file_location = f"{self.file_path}{self.file_name}"
        loader = TextLoader(file_location)  # TODO: Could probably initialize this at a higher level
        documents = loader.load()[0]
        print(documents)
        return documents
