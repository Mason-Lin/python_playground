# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

import logging
import subprocess
from concurrent import futures

import grpc
import vcosmos_pb2
import vcosmos_pb2_grpc


class Greeter(vcosmos_pb2_grpc.ImpacketServicer):

    def wmiexec(self, request, context):
        p = subprocess.run(request.cmd, shell=True, capture_output=True)
        return vcosmos_pb2.CmdReply(returncode=int(p.returncode), stdout=p.stdout, stderr=p.stderr)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    vcosmos_pb2_grpc.add_ImpacketServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
