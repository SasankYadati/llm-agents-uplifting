from termcolor import colored
import json
from tools import sampleQuestionsFromMMLU, callLLM, calculateAccuracy

def pretty_print_conversation(messages):
    role_to_color = {
        "system": "red",
        "user": "green",
        "assistant": "blue",
        "function": "magenta",
    }
    
    for message in messages:
        if message["role"] == "system":
            print(colored(f"system: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "user":
            print(colored(f"user: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "assistant" and message.get("function_call"):
            print(colored(f"assistant: {message['function_call']}\n", role_to_color[message["role"]]))
        elif message["role"] == "assistant" and not message.get("function_call"):
            print(colored(f"assistant: {message['content']}\n", role_to_color[message["role"]]))
        elif message["role"] == "function":
            print(colored(f"function ({message['name']}): {message['content']}\n", role_to_color[message["role"]]))

def requires_tool_calls(response):
    return response.choices[0].finish_reason == "tool_calls"

def gpt_process_function_calling(response):
    output = ""
    if requires_tool_calls(response):
        print(f"Tool calls {list(map(lambda x: x.function.name, response.choices[0].message.tool_calls))}")
        for tool_call in response.choices[0].message.tool_calls:
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            func = globals()[function_name]
            output += func(**arguments) + "\n\n "
        return output
    else:
        output += response.choices[0].message.content
        return response.choices[0].message.content