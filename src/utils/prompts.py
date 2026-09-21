analyst_instructions = """
You are tasked with creating a set of AI analyst personas. Follow these instructions carefully:
1. First, review the research topic:
{topic}
2. Examine any editorial feedback that has been optionally provided to guide creation of the analyst:
{human_analyst_feedback}
3. Determine the most interesting themes based upon documents and / or feedback above.
4. Pick the top {max_analysts} themes.Total count of analysts should be {max_analysts}
5. Assign one analyst to each theme.
"""