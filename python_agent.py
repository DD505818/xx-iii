
# python_agent.py
# Python Agent for XXIII Turbo Framework

from phi.agent.python import PythonAgent
from phi.model.openai import OpenAIChat
from phi.file.local.csv import CsvFile

python_agent = PythonAgent(
    model=OpenAIChat(id="gpt-4o"),
    files=[
        CsvFile(
            path="https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv",
            description="Contains information about movies from IMDB.",
        )
    ],
    markdown=True,
    pip_install=True,
    show_tool_calls=True,
)

python_agent.print_response(" $$$")
