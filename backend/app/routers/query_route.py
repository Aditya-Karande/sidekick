from services.chatbot import chatbot

# get user req. 
def query_process(query:str):

    res = chatbot.invoke({"messages":[("user",query.req)]},config={"configurable":{"thread_id":query.thread_id}})

    return res["messages"][-1].content