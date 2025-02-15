# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import mlab_pyprotos.runner_pb2 as runner__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in runner_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class RunnerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_runner = channel.unary_unary(
                '/runner.Runner/get_runner',
                request_serializer=runner__pb2.GetRunnerRequest.SerializeToString,
                response_deserializer=runner__pb2.GetRunnerResponse.FromString,
                _registered_method=True)
        self.stop_task = channel.unary_unary(
                '/runner.Runner/stop_task',
                request_serializer=runner__pb2.StopTaskRequest.SerializeToString,
                response_deserializer=runner__pb2.StopTaskResponse.FromString,
                _registered_method=True)
        self.remove_task_environment = channel.unary_unary(
                '/runner.Runner/remove_task_environment',
                request_serializer=runner__pb2.RemoveTaskRequest.SerializeToString,
                response_deserializer=runner__pb2.RemoveTaskResponse.FromString,
                _registered_method=True)
        self.create_task_environment = channel.unary_unary(
                '/runner.Runner/create_task_environment',
                request_serializer=runner__pb2.CreateTaskRequest.SerializeToString,
                response_deserializer=runner__pb2.CreateTaskResponse.FromString,
                _registered_method=True)
        self.get_task_environment = channel.unary_unary(
                '/runner.Runner/get_task_environment',
                request_serializer=runner__pb2.GetTaskEnvironmentRequest.SerializeToString,
                response_deserializer=runner__pb2.GetTaskEnvironmentResponse.FromString,
                _registered_method=True)
        self.run_task = channel.unary_stream(
                '/runner.Runner/run_task',
                request_serializer=runner__pb2.RunTaskRequest.SerializeToString,
                response_deserializer=runner__pb2.RunTaskResponse.FromString,
                _registered_method=True)
        self.submit_result = channel.unary_unary(
                '/runner.Runner/submit_result',
                request_serializer=runner__pb2.SubmitResultRequest.SerializeToString,
                response_deserializer=runner__pb2.SubmitResultResponse.FromString,
                _registered_method=True)


class RunnerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_runner(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stop_task(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def remove_task_environment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def create_task_environment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_task_environment(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def run_task(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def submit_result(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RunnerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_runner': grpc.unary_unary_rpc_method_handler(
                    servicer.get_runner,
                    request_deserializer=runner__pb2.GetRunnerRequest.FromString,
                    response_serializer=runner__pb2.GetRunnerResponse.SerializeToString,
            ),
            'stop_task': grpc.unary_unary_rpc_method_handler(
                    servicer.stop_task,
                    request_deserializer=runner__pb2.StopTaskRequest.FromString,
                    response_serializer=runner__pb2.StopTaskResponse.SerializeToString,
            ),
            'remove_task_environment': grpc.unary_unary_rpc_method_handler(
                    servicer.remove_task_environment,
                    request_deserializer=runner__pb2.RemoveTaskRequest.FromString,
                    response_serializer=runner__pb2.RemoveTaskResponse.SerializeToString,
            ),
            'create_task_environment': grpc.unary_unary_rpc_method_handler(
                    servicer.create_task_environment,
                    request_deserializer=runner__pb2.CreateTaskRequest.FromString,
                    response_serializer=runner__pb2.CreateTaskResponse.SerializeToString,
            ),
            'get_task_environment': grpc.unary_unary_rpc_method_handler(
                    servicer.get_task_environment,
                    request_deserializer=runner__pb2.GetTaskEnvironmentRequest.FromString,
                    response_serializer=runner__pb2.GetTaskEnvironmentResponse.SerializeToString,
            ),
            'run_task': grpc.unary_stream_rpc_method_handler(
                    servicer.run_task,
                    request_deserializer=runner__pb2.RunTaskRequest.FromString,
                    response_serializer=runner__pb2.RunTaskResponse.SerializeToString,
            ),
            'submit_result': grpc.unary_unary_rpc_method_handler(
                    servicer.submit_result,
                    request_deserializer=runner__pb2.SubmitResultRequest.FromString,
                    response_serializer=runner__pb2.SubmitResultResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'runner.Runner', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('runner.Runner', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Runner(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_runner(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/runner.Runner/get_runner',
            runner__pb2.GetRunnerRequest.SerializeToString,
            runner__pb2.GetRunnerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def stop_task(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/runner.Runner/stop_task',
            runner__pb2.StopTaskRequest.SerializeToString,
            runner__pb2.StopTaskResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def remove_task_environment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/runner.Runner/remove_task_environment',
            runner__pb2.RemoveTaskRequest.SerializeToString,
            runner__pb2.RemoveTaskResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def create_task_environment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/runner.Runner/create_task_environment',
            runner__pb2.CreateTaskRequest.SerializeToString,
            runner__pb2.CreateTaskResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def get_task_environment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/runner.Runner/get_task_environment',
            runner__pb2.GetTaskEnvironmentRequest.SerializeToString,
            runner__pb2.GetTaskEnvironmentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def run_task(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/runner.Runner/run_task',
            runner__pb2.RunTaskRequest.SerializeToString,
            runner__pb2.RunTaskResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def submit_result(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/runner.Runner/submit_result',
            runner__pb2.SubmitResultRequest.SerializeToString,
            runner__pb2.SubmitResultResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
