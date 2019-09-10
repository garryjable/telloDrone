import socket
import time
from abc import ABC, abstractmethod

class DroneDispatcher:
    _host = '127.0.0.1'
    _port = 8889
    

    def __init__(self, host=None, port=None):
        self._init_missions()
        if host:
            self._host = host 
        if port:
            self._port = port
        self._drone = (self._host, self._port)
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind((self._host, self._port + 1))
        return
    
    def __del__(self):
        try:
            self._socket.close()
        except AttributeError as e:
            return

    def get_mission_names(self):
        names = []
        for key, val in self.missions.items():
            names.append(key)
        return names

    def _init_missions(self):
        import mission_data
        self._missions = {}
        for data_obj in mission_data.data:
            if data_obj['type'] == 'fast':
                mission = FastMission(data_obj['commands'], data_obj['name'])
            elif data_obj['type'] == 'slow':
                mission = SlowMission(data_obj['commands'], data_obj['name'])
            elif data_obj['type'] == 'verbosefast':
                mission = VerboseFastMission(data_obj['commands'], data_obj['name'])
            self._missions[data_obj['name']] = mission

    def fly_mission(self, name):
        try:
            mission = self._missions[name]
            return mission.execute_commands(self._send_command) 
        except KeyError as e:
            return "invalid mission"

    def _send_command(self, command):
        self._socket.sendto(command.encode(), self._drone)
        data, addr = self._socket.recvfrom(1024)
        return 'Recieved from server: ' + str(data.decode())
    

class Mission(ABC):
    _name = 'default mission'
    _commands = []
    
    def __init__(self, command_list, name):
        command_list.insert(0, 'takeoff')
        command_list.insert(0, 'command')
        command_list.append('land')
        self._commands = command_list
        self._name = name

    def execute_commands(self, send_method):
        for command in self._commands:           
            self._execute_command(command, send_method)                       
        return 'you flew mission ' + self._name

    @abstractmethod
    def _execute_command(self, command, send_method):
        send_method(command)
        time.sleep(.01)

class FastMission(Mission):

    def _execute_command(self, command, send_method):
        send_method(command)
        time.sleep(.01)

class SlowMission(Mission):

    def _execute_command(self, command, send_method):
        send_method(command)
        time.sleep(5)

class VerboseFastMission(Mission):

    def _execute_command(self, command, send_method):
        print(send_method(command))
        time.sleep(.01)
 

class ClientCli():
    _dispatcher = None

    def __init__(self, host=None, drone_port=None):
        self._dispatcher = DroneDispatcher(host, drone_port)

    def _list_missions(self):
        print('Availible missions:')
        for name in self._dispatcher.get_mission_names():
            print('                ' + name)

    def start_client(self):
        print("Welcome to the tello drone client, press q to quit, or enter mission name to fly a mission, enter ls to list possible missions")
        message = input("-> ")
        while message != 'q':
            if message == 'ls':
                self._list_missions()
            else:
                response = self._dispatcher.fly_mission(message)
                print(response)
            message = input("-> ")




