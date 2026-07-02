from langchain_core.messages import HumanMessage, ToolMessage

def run_with_tools(llm, prompt, tools_map):
    msgs = [HumanMessage(content=prompt)]
    res = llm.invoke(msgs)
    while res.tool_calls:
        msgs.append(res)
        for tc in res.tool_calls:
            out = tools_map[tc["name"]].invoke(tc["args"])
            msgs.append(ToolMessage(content=str(out), tool_call_id=tc["id"]))
        res = llm.invoke(msgs)
    return res.content
