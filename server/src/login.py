import test_pb2
import test_pb2_grpc

import logging

class Login(test_pb2_grpc.LoginServicer):

    def login(self, request, context):
        return test_pb2.LoginResponse(
            status = 200,
            statusMessage = 'OK',
            sessionId = 'sessionId'
        )

    def logout(self, request, context):
        return test_pb2.LoginResponse(
            status = 200,
            statusMessage = 'OK',
            sessionId = ''
        )