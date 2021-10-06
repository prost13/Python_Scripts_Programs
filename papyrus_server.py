from papyrus_socket import Socket
import asyncio

class Server(Socket):
    def __init__(self):
        super(Server, self).__init__()


        self.socket.listen(5)

        self.users = []

    def set_up(self):
        self.socket.bind(('Ip', 4444))
        self.socket.setblocking(False)
        print("Server is listening")

    async def send_data(self, data):
        for user in self.users:
            await self.main_loop.sock_senall(user, data)

    async def listen_socket(self, listened_socket=None):
        if not listened_socket:
            return
        while True:
            try:
                data = self.main_loop.sock_recv(listened_socket, 1024)
                print(f'User sent {data}')
                await self.send_data(data)
            except ConnectionResetError:
                self.users.remove(listened_socket)
                return

    async def accept_sockets(self):
        while True:
            user_socket, address = await self.main_loop.sock_accept(self.socket)
            print(f"User <{address[0]}> connected!")

            self.users.append(user_socket)
            self.main_loop.create_task(self.listen_socket(user_socket))

    async def main(self):
        await self.main_loop.create_task(self.accept_sockets())

if __name__ == '__main__':
    server = Server()
    server.set_up()

    server.start()
