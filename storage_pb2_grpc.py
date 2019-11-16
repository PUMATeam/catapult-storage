# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import storage_pb2 as storage__pb2


class StorageStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Create = channel.unary_unary(
        '/Storage/Create',
        request_serializer=storage__pb2.Volume.SerializeToString,
        response_deserializer=storage__pb2.Response.FromString,
        )
    self.Remove = channel.unary_unary(
        '/Storage/Remove',
        request_serializer=storage__pb2.UUID.SerializeToString,
        response_deserializer=storage__pb2.Response.FromString,
        )
    self.List = channel.unary_unary(
        '/Storage/List',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=storage__pb2.VolumeList.FromString,
        )


class StorageServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Create(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Remove(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def List(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StorageServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=storage__pb2.Volume.FromString,
          response_serializer=storage__pb2.Response.SerializeToString,
      ),
      'Remove': grpc.unary_unary_rpc_method_handler(
          servicer.Remove,
          request_deserializer=storage__pb2.UUID.FromString,
          response_serializer=storage__pb2.Response.SerializeToString,
      ),
      'List': grpc.unary_unary_rpc_method_handler(
          servicer.List,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=storage__pb2.VolumeList.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Storage', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
