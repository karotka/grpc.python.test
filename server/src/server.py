#!/usr/bin/env python
from concurrent import futures
import time
import grpc
import logging

from config import c
from test import Test
from login import Login

import test_pb2_grpc

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# SERVER
def registerMethods(server):
    test_pb2_grpc.add_TestServicer_to_server(Test(), server)
    test_pb2_grpc.add_LoginServicer_to_server(Login(), server)

def serve():
    _ONE_DAY_IN_SECONDS = 60 * 60 * 24

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers = c.server.maxWorkers))

    registerMethods(server)

    server.add_insecure_port('%s:%d' % (c.server.host, c.server.port))

    server.start()
    logger.info('Server started at host: <%s> port:<%d>.',
                c.server.host, c.server.port)
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
