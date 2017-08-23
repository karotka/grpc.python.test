#!/usr/bin/env python

from concurrent import futures
import time
import grpc
import logging

import test_pb2
import test_pb2_grpc

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# SERVER

class Test(test_pb2_grpc.TestServicer):

  def hello(self, request, context):
    logger.info('Receive request ....')
    return test_pb2.Response(
        data = request,
        statusMessage = 'OK',
        status = 200
    )

def serve():
    _ONE_DAY_IN_SECONDS = 60 * 60 * 24
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_TestServicer_to_server(Test(), server)
    server.add_insecure_port('[::]:%d' % 50051)
    server.start()
    logger.info('Server started at port:<%s>.', 50051)
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
