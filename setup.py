from setuptools import setup, find_packages

setup(
    name="db_agent",
    version="1.0",
    packages=find_packages(where="agent"),  # Only include src/
    package_dir={"": "agent"},  # Use src as the package directory
    install_requires=[
        "psycopg2",
        "streamlit",
        "langchain",
        "smolagents",
        "dotenv"
    ],
    entry_points={
        "console_scripts": [
            "run-db-bot=db_agent.bot:main",
        ],
    },
)
