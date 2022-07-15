# Connect4 Game using Python Websockets

This is an implementation of the *Getting Started* section of **websockets** tutorials.

[Part 1 - Send & receive](https://websockets.readthedocs.io/en/stable/intro/tutorial1.html)

## Run the code

Open a shell, navigate to the directory containing app.py, and start the server:

`$ python app.py`

This doesn’t display anything. Hopefully the WebSocket server is running. Let’s make sure that it works. You cannot test the WebSocket server with a web browser like you tested the HTTP server. However, you can test it with websockets’ interactive client.

Open another shell and run this command:

`$ python -m websockets ws://localhost:8001/`

You get a prompt. Type a message and press “Enter”. Switch to the shell where the server is running and check that the server received the message. Good!

Exit the interactive client with Ctrl-C or Ctrl-D.