from openai import OpenAI
import replicate, json
from tools import sampleQuestionsFromMMLU, callLLM, calculateAccuracy
from langchain_core.utils.function_calling import convert_to_openai_tool
from langchain.agents import tool

client = OpenAI()

sys_prompt = {
    "role": "system",
    "content": "You are an agent that evaluates exactly three other LLMs on sample MMLU questions. The three models are gpt-2, gpt-3, gpt-3. You will call appropriate functions to achieve this goal."
}

workflow = [
    ("Sample 2 questions from MMLU dataset.", [sampleQuestionsFromMMLU]),
    ("Ask each one of the following LLMs to answer these 20 questions with the correct choice and check their answers.",[callLLM]),
    ("Calculate the number of correct answers for each model and then calculate the accuracy of each model", [calculateAccuracy]),
    ("Report the best model and its accuracy.", [])
]


def gpt_process_function_calling(gpt_response):
    finish_reason = gpt_response.choices[0].finish_reason
    # We check if we finished for an explicit function call
    if finish_reason == "tool_calls":
        function_name = gpt_response.choices[0].message.tool_calls[0].function.name
        arguments = json.loads(gpt_response.choices[0].message.tool_calls[0].function.arguments)
        func = globals()[function_name]
        return func(**arguments)
    else:
        return gpt_response.choices[0].message.content

outputs = []
output = ""
for instruction, functions in workflow:
    kwargs = {}
    if len(functions) > 0:
        functions = [convert_to_openai_tool(tool(f)) for f in functions]
        kwargs = {"tools": functions}
    messages = [sys_prompt,
                {"role": "user", "content": instruction + f" {output}"}]
    output = client.chat.completions.create(model='gpt-3.5-turbo-0125',
                                            messages=messages,
                                            **kwargs)
    print(messages)
    output = gpt_process_function_calling(output)
    outputs.append(output)
print(output)