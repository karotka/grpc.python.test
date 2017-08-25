import test_pb2
import test_pb2_grpc

class Test(test_pb2_grpc.TestServicer):

    def hello(self, request, context):
        return test_pb2.Response(
            data = request,
            statusMessage = 'OK',
            status = 200
        )