#!/usr/bin/env python

from __future__ import print_function

import grpc

import test_pb2
import test_pb2_grpc

# CLIENT

def run():
    channel = grpc.insecure_channel('[::]:50000')

    # Test/hello method
    server = test_pb2_grpc.TestStub(channel)
    data = test_pb2.HelloRequest(
            id = 1234567890,
            name = 'Karotka testuje'
    )  
    response = server.hello(data)
    print("%s <= was received from the server" % response)

    # Login/login method
    server = test_pb2_grpc.LoginStub(channel)
    data = test_pb2.LoginRequest(
            username = 'karotka@seznam.cz',
            password = 'heslo.do.mailu.treba'
    )  
    response = server.login(data)
    print("%s <= was received from the server" % response)

if __name__ == '__main__':
  run()
