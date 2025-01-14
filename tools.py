from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from dotenv import load_dotenv

load_dotenv()

docs_scrape_tool = ScrapeWebsiteTool(
    website_url="https://www.socialhardware.in/"
)

search_tool = SerperDevTool(
    search_url="https://google.serper.dev/search",
    n_results=4,
)