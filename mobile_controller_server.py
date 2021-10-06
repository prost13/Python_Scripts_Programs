import webbrowser
import socket
import os
import subprocess

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 4444))

server.listen()

while True:
    user, address = server.accept()

    while True:
        data = user.recv(1024).decode("utf-8").lower()
        print(data)

        # URL LINK
        if data == "youtube":
            webbrowser.open("https://www.youtube.com")
        if data == "google":
            webbrowser.open("https://www.google.com")
        if data == "vk":
            webbrowser.open("https://www.vk.com")

        #STARTFILE
        elif data == "telegram":
            os.startfile("C:/Users/abogo/AppData/Roaming/Telegram Desktop/Telegram.exe")
        elif data == "telegram":
            os.startfile("E:/virtual/VirtualBox.exe")

        else:
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
