import datasets
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.retrievers import BM25Retriever
from smolagents import Tool
import os


class DocProcessor:
    def __init__(self, doc_location):
        """
        Initialize the DocProcessor with a location of documents.
        
        Args:
            doc_location (str): Path to the folder containing documents.
        """
        self.__doc_location = doc_location
        self.__source_docs = None

    def process_docs(self):
        """
        Process and split documents into smaller chunks using a text splitter.
        
        Returns:
            List: List of split document chunks.
        """
        if self.__source_docs is None:
            self._init_docs()  # Initialize the documents if not already done.
        
        
        return self.__source_docs
        
    def _init_docs(self):
        """
        Initialize the documents by reading files from the specified location.
        """
        self.__source_docs = []
        for filename in os.listdir(self.__doc_location):
            file_path = os.path.join(self.__doc_location, filename)
            if os.path.isfile(file_path) and filename.endswith(".md"):
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    document = Document(
                        page_content=content,
                        metadata={"filename": filename, "path": file_path}
                    )
                    self.__source_docs.append(document)





class RetrieverTool(Tool):
    name = "retriever"
    description = "Uses semantic search to retrieve the parts of transformers documentation that could be most relevant to answer your query."
    inputs = {
        "query": {
            "type": "string",
            "description": "The query to perform. This should be semantically close to your target documents. Use the affirmative form rather than a question.",
        }
    }
    output_type = "string"

    def __init__(self, docs, **kwargs):
        super().__init__(**kwargs)
        self.retriever = BM25Retriever.from_documents(
            docs, k=10
        )

    def forward(self, query: str) -> str:
        assert isinstance(query, str), "Your search query must be a string"

        docs = self.retriever.invoke(
            query,
        )
        return "\nRetrieved documents:\n" + "".join(
            [
                f"\n\n===== Document {str(i)} =====\n" + doc.page_content
                for i, doc in enumerate(docs)
            ]
        )


