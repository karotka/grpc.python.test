from __future__ import print_function

import grpc

import test_pb2
import test_pb2_grpc

# CLIENT

def run():
    channel = grpc.insecure_channel('10.0.4.99:50000')
    server = test_pb2_grpc.TestStub(channel)

    data = test_pb2.HelloRequest(
            id = 1234567890,
            name = 'Karotka testuje'
    )
    print("------------ Client  ---------------")
    print("%s => send it to the server" % data)
  
    response = server.hello(data)
    print("------------ Server  ---------------")
    print("%s <= was received from the server" % response)


if __name__ == '__main__':
  run()
