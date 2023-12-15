from gptpy3.chat_client import ChatClient

client = ChatClient(name='gpt', openai_key_path='secret_key.txt', port=7788)
client.run()
