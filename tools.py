tools = [
    {
        "name": "get_weather",
        "description": "使用此工具获取特定地点的天气信息",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "location name",
                }
            },
            "required": ["name"]
        },
    },
]

def get_weather(name):
    if name == "北京":
        return "37.9"
    elif name == "云南":
        return "28.2"
    else:
        return "未搜到该地区天气情况"