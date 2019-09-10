import test_server
from models import DroneDispatcher
from models import command_line_interface
import unittest
import socket
import time

class test_drone_dispatcher(unittest.TestCase):

    def setUp(self):
        host = '127.0.0.1'
        drone_port = 8889
        self.dispatcher = DroneDispatcher(host, drone_port)

    def test_mission_one(self):
        response = self.dispatcher.execute_mission('1')
        self.assertEqual(response, "you flew mission 1")

    
    def test_mission_two(self):
        response = self.dispatcher.execute_mission('2')
        self.assertEqual(response, "you flew mission 2")
    
    def test_mission_three(self):
        response = self.dispatcher.execute_mission('3')
        self.assertEqual(response, "you flew mission 3")
    
    def test_cli(self):
        print("this is a test")
        self.assertEqual(1, 1)
        
    def test_missions_model(self):
        print("this is a test")
        self.assertEqual(1, 1)

    def test_missions_model(self):
        print("this is a test")
        self.assertEqual(1, 1)
