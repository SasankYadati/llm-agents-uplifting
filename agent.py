from openai import OpenAI
import replicate

client = OpenAI()

sys_prompt = {
    "role": "system",
    "content": "You are an agent that evaluates other LLMs, calculates their accuracy and report the results. You will call appropriate functions to achieve this goal."
}


