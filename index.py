#--web true
import json

def main(_):
    data = {
        "services": [
            {
                "name": "Ambra",
                "url": "openai/ambra"
            },
            {
                "name": "OpenAI",
                "url": "openai/chat"
            },
            {
                "name": "Wordpress",
                "url": "openai/wordpress"
            },
            { 
                "name": "Demo", 
                "url": "mastrogpt/demo",
            },
            {
                "name": "Reclamo-MistralAI",
                "url": "mastrogpt/mistral"
            },
            {
                "name": "Reclamo-OpenAI",
                "url": "mastrogpt/openaimod"
            },
        ]
    }
    return {"body": data}