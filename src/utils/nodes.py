from dotenv import load_dotenv
from src.utils.states import GenerateAnalystsState
from src.utils.models import llm
from src.utils.objects import Analyst, Perspectives
from src.utils.prompts import analyst_instructions
from langchain.messages import SystemMessage,HumanMessage
load_dotenv()

#nodes

def create_analysts(state:GenerateAnalystsState):
    """Create analysts"""

    topic = state["topic"]
    max_analysts = state["max_analysts"]
    human_analyst_feedback = state.get("human_analyst_feedback","")

    #Enforce structure output
    structured_llm = llm.with_structured_output(Perspectives)

    #System_Message
    system_message = analyst_instructions.format(topic=topic,
                                                 human_analyst_feedback=human_analyst_feedback,
                                                 max_analysts=max_analysts)

    #Generate analyst
    analysts = structured_llm.invoke([SystemMessage(content=system_message)]+[HumanMessage(content="Please Generate the set of analysts")])
    return {"analysts":analysts.analysts}











