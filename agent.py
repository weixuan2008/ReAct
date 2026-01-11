import json
import os
import re

from llm import client
from prompt import REACT_PROMPT
from tools import tools, get_weather


def send_messages(message):
    resp = client.chat.completions.create(
        model=os.getenv("azure_model_name"),
        messages=message,
        temperature=0.3
    )
    return resp


if __name__ == "__main__":
    instructions = "你是一个天气小助手"

    query = "请比较今天北京和云南的天气，哪一个更热？"

    prompt = REACT_PROMPT.replace("{tools}", json.dumps(tools)).replace("{input}", query)
    messages = [{"role": "user", "content": prompt}]

    while True:
        # 1.调用大模型做回复
        response = send_messages(messages)
        response_text = response.choices[0].message.content

        print("------本轮，大模型的回复：")
        print(response_text)

        # 2. 判断是否为最终答案，如果是就直接返回结束对话
        final_answer_match = re.search(r'Final Answer:\s*(.*)', response_text)
        if final_answer_match:
            final_answer = final_answer_match.group(1)
            print("最终答案:", final_answer)
            break

        # 3.若不是最终答案，需要进行下一轮思考
        # 将模型的回复添加到对话历史中，以便维持上下文
        messages.append(response.choices[0].message)

        # 4. 搜索是否需要接入工具
        # 获取模型执行工具名称和参数
        action_match = re.search(r'Action:\s*(\w+)', response_text)
        action_input_match = re.search(r'Action Input:\s*({.*?}|".*?")', response_text, re.DOTALL)

        if action_match and action_input_match:
            # 工具名称
            tool_name = action_match.group(1)
            # 解析动作输入参数为JSON对象
            params = json.loads(action_input_match.group(1))

            observation = ""
            if tool_name == "get_weather":
                observation = get_weather(params['name'])
                print("天气工具的回复：Observation:", observation)

                # 将工具调用的结果添加到对话历史中，给下一轮对话
            messages.append({"role": "user", "content": f"Observation: {observation}"})
