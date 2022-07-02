from __future__ import print_function

import logging

import grpc
import vcosmos_pb2
import vcosmos_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = vcosmos_pb2_grpc.ImpacketStub(channel)
        p = stub.wmiexec(vcosmos_pb2.CmdRequest(cmd="echo 123"))
        print(f"Impacket client received: {p.returncode=} {p.stdout=} {p.stderr=}")


if __name__ == '__main__':
    logging.basicConfig()
    run()
