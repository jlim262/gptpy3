# gptpy3
gptpy3 is an efficient socket client that connects to a gptpy2 server within a Python 3 environment. It is designed to receive messages from the gptpy2 server, interact with the ChatGPT API, and relay ChatGPT's responses back to the gptpy2 server. To operate the gptpy3 client, an OpenAI API key is required.

## Prerequisites
Ensure you have Python 3.8 installed on your machine before proceeding.

## Installation of gptpy3
To set up gptpy3, first clone its GitHub repository and then execute the setup script:
```
git clone git@github.com:jlim262/gptpy3.git
cd gptpy3
python setup.py install
```

## How to Use gptpy3
Utilizing gptpy3 involves importing the ChatClient class, creating an instance with the specified host and port, and then invoking the `run()` method. Make sure your gptpy2 server is active. Additionally, you need to provide a file containing your OpenAI API key.

```python
from gptpy3.chat_client import ChatClient

# Initializing and running the ChatClient
client = ChatClient(name='gpt', openai_key_path='secret_key.txt', host='localhost', port=7788)
client.run()
```
In this setup, the gptpy3 client connects to the gptpy2 server and facilitates communication with the ChatGPT API, using the provided API key.