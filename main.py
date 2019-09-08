import socket
import time


def Main():
    host = '127.0.0.1'
    port = 8890

    #server = ('127.0.0.1', 8889)

    #s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #s.bind((host,port))

    dispatcher = DroneDispatcher(host, port)

    print("Welcome to the tello drone client, press q to quit, or enter 1 2 or 3 to fly a pretend mission, enter test to test command")
    message = input("-> ")
    while message != 'q':
        response = dispatcher.execute_mission(message)
        print(reponse)
        message = input("-> ")
    s.close()

class DroneDispatcher:

    def __init__(self, host, port):
        self.host = host 
        self.server = (self.host, port)
        self.port = port + 1 
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((host,port))

    def execute_mission(mission_num):
        mission_one = ['up 50','left 50','right 100','left 50', 'down 50']
        mission_two = ['up 50','right 50','left 100','right 50', 'down 50']
        mission_three = ['up 25','right 25','left 50','right 25', 'down 25']
        mission = []
        if mission_num == '1':
            mission = mission_one
        elif mission_num == '2':
            mission = mission_two
        elif mission_num == '3':
            mission = mission_three
        else:
            return "invalid mission"
        send_command('command')    
        send_command('takeoff')    
        for command in mission:
            send_command(command)
        send_command('land')    
        return 'you flew mission ' + message
    
    def send_command(command):
        self.socket.sendto(command.encode(), self.server)
        data, addr = self.socket.recvfrom(1024)
        print( 'Recieved from server: ' + str(data.decode()))
        time.sleep(5)
 




     











if __name__ == '__main__':
    Main()
