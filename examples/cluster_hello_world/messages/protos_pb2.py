# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: examples/cluster_hello_world/messages/protos.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='examples/cluster_hello_world/messages/protos.proto',
  package='messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n2examples/cluster_hello_world/messages/protos.proto\x12\x08messages\"\x0e\n\x0cHelloRequest\" \n\rHelloResponse\x12\x0f\n\x07message\x18\x01 \x01(\tb\x06proto3')
)




_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='messages.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=78,
)


_HELLORESPONSE = _descriptor.Descriptor(
  name='HelloResponse',
  full_name='messages.HelloResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='messages.HelloResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=112,
)

DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloResponse'] = _HELLORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'examples.cluster_hello_world.messages.protos_pb2'
  # @@protoc_insertion_point(class_scope:messages.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloResponse = _reflection.GeneratedProtocolMessageType('HelloResponse', (_message.Message,), {
  'DESCRIPTOR' : _HELLORESPONSE,
  '__module__' : 'examples.cluster_hello_world.messages.protos_pb2'
  # @@protoc_insertion_point(class_scope:messages.HelloResponse)
  })
_sym_db.RegisterMessage(HelloResponse)


# @@protoc_insertion_point(module_scope)
