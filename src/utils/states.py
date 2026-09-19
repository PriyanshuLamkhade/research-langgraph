from typing_extensions import TypedDict,NotRequired
from typing import Optional, List
from src.utils.objects import Analyst

class GenerateAnalystsState(TypedDict):
    topic: str #Research Topic
    max_analysts: int
    human_analyst_feedback: NotRequired[Optional[str]] #Human feedback for what is generated
    analysts: NotRequired[List[Analyst]] #List of all Analysts