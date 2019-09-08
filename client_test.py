import socket

def Main():
    host = '127.0.0.1'
    port = 8890

    server = ('127.0.0.1', 8889)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))

    print("Welcome to the tello drone client, press q to quit, or enter 1 2 or 3 to fly a mission")
    message = input("-> ")
    while message != 'q':
        if message == '1':
            print('you flew mission 1')
        elif message == '2':
            print('you flew mission 2')
        elif message == '3':
            print('you flew mission 3')
        s.sendto(message.encode(), server)
        data, addr = s.recvfrom(1024)
        print( 'Recieved from server: ' + str(data.decode()))
        message = input("-> ")
    s.close()

if __name__ == '__main__':
    Main()
