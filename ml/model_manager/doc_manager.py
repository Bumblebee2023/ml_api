from docx import Document

from ml.data_preprocessing import DocProcessor, InlineDocProcessor
from .base_manager import BaseManager


class DocManager(BaseManager):
    def __init__(self, *kwargs):
        pass

    def parsing_with_sentences(self, doc: Document):
        return DocProcessor.preprocess_doc_splitted_by_sentences(doc)

    def parsing_with_brackets(self, doc: Document):
        return DocProcessor.preprocess_doc_splitted_by_brackets(doc)

    def colorize_doc_inline(self, doc: Document):
        return InlineDocProcessor.process(doc)

