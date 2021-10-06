from papyrus_socket import Socket
import asyncio
from datetime import datetime
from papyrus_encryption import Encryptor
from os import system

class Client(Socket):
    def __init__(self):
        super(Client, self).__init__()
        self.messages = ""
        self.encryptor = Encryptor()

    def set_up(self):
        try:
            self.socket.connect(("10.0.2.15", 4444))
            self.socket.setblocking(False)
        except ConnectionRefusedError:
            print('Sorry, server is offline')
            exit(0)

    async def listen_socket(self, listened_socket=None):
        while True:
            data = await self.main_loop.sock_recv(self.socket, 1024)
            clean_data = self.encryptor.decrypt(data.decode("utf-8"))
            self.messages += f"{datetime.now().date()}: {clean_data}\n"
            system("cls")
            print(self.messages)

    async def send_data(self, data=None):
        while True:
            data = await self.main_loop.run_in_executor(None, input)
            encrypted_data = self.encryptor.encrypt(data)
            await self.main_loop.sock_sendall(self.socket, encrypted_data.encode("utf-8"))

    async def main(self):
        listening_task = self.main_loop.creat_task(self.listen_socket())
        sending_task = self.main_loop.creat_task(self.send_data())

        await asyncio.gather([listening_task, sending_task])

if __name__ == '__name__':
    client = Client()
    client.set_up()
    client.start()

