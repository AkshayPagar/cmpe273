from concurrent import futures

import time

import grpc


import calculator
import calculator_pb2
import calculator_pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
	response=calculator_pb2.res();	
	response.res=calculator.add(request.num1,request.num2)
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
