import socket
import time


def Main():
    host = '127.0.0.1'
    drone_port = 8889

    dispatcher = DroneDispatcher(host, drone_port)

    print("Welcome to the tello drone client, press q to quit, or enter 1 2 or 3 to fly a mission")
    message = input("-> ")
    while message != 'q':
        response = dispatcher.execute_mission(message)
        print(response)
        message = input("-> ")

class DroneDispatcher:

    def __init__(self, host, port):
        self.host = host 
        self.drone = (self.host, port)
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((host, port + 1))
        return
    
    def __del__(self):
        self.socket.close()

    def execute_mission(self, mission_num):
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
        self.send_command('command')    
        self.send_command('takeoff')    
        for command in mission:
            self.send_command(command)
        self.send_command('land')    
        return 'you flew mission ' + mission_num
    
    def send_command(self, command):
        self.socket.sendto(command.encode(), self.drone)
        data, addr = self.socket.recvfrom(1024)
        print( 'Recieved from server: ' + str(data.decode()))
        time.sleep(5)
        return
 




     











if __name__ == '__main__':
    Main()
