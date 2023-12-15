from gptpy3.chat_client import ChatClient

client = ChatClient(name='gpt', openai_key_path='secret_key.txt', host='192.168.1.35', port=7788)
client.run()
