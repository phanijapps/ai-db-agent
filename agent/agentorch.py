from smolagents.agents import ToolCallingAgent, CodeAgent
from smolagents import tool, LiteLLMModel, Tool
from typing import Optional
from .dbtool import execute_query
from .kbase import DocProcessor, RetrieverTool
from dotenv import load_dotenv
import os


class AgentOrch:

    def __init__(self, model = LiteLLMModel(model_id="gpt-4o"),max_steps=8):
        """
        Initializes the AgentOrch class with a LiteLLM model, RAG retriever tool, and SQL tool.
        """
        load_dotenv()
        self.__model__ = model
        self.__max_steps__ = max_steps
        self.retriever_tool = self.__init_rag__()
        self.__agent__ = CodeAgent(tools=[self.retriever_tool, execute_query], 
                    model=self.__model__,
                    add_base_tools=True,
                    max_steps = self.__max_steps__,
                    additional_authorized_imports=['json','pandas','numpy','requests']
                    )

    def __init_rag__(self):
        """
        Initializes the RAG (retrieval-augmented generation) retriever tool.
        
        Returns:
            Object: The initialized RAG retriever tool.
        """
        docs = DocProcessor(doc_location="./docs").process_docs()
        
        # Replace with actual RAG retriever initialization logic
        retriever = RetrieverTool(docs)
        return retriever  # Placeholder for the actual retriever tool

    def set_model(self, model):
        self.del_model()
        self.__model__ = model
        self.__agent__ = CodeAgent(tools=[self.retriever_tool, execute_query], 
                    model=self.__model__,
                    add_base_tools=True,
                    max_steps = self.__max_steps__,
                    additional_authorized_imports=['json','pandas','numpy','requests']
                    )

    def del_model(self):
        del self.__model__

    def get_prompt(self):
        return self.__agent__.system_prompt_template

    def set_prompt(self, prompt_template):
        self.__agent__.system_prompt_template = prompt_template

    def agent_query(self,query):
        """
        """
        agent_output = self.__agent__.run(query)
        return agent_output
