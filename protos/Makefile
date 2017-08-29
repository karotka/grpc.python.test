all :
	python -m grpc_tools.protoc -I. --python_out=../server/src --grpc_python_out=../server/src test.proto
	python -m grpc_tools.protoc -I. --python_out=../client/src --grpc_python_out=../client/src test.proto

clean :
	rm ../server/src/*_pb2*.py
	rm ../server/src/*.pyc
	rm ../client/src/*_pb2*.py
	rm ../client/src/*.pyc

