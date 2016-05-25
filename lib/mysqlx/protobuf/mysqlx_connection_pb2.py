# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mysqlx_connection.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import mysqlx_datatypes_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mysqlx_connection.proto',
  package='Mysqlx.Connection',
  serialized_pb=_b('\n\x17mysqlx_connection.proto\x12\x11Mysqlx.Connection\x1a\x16mysqlx_datatypes.proto\"@\n\nCapability\x12\x0c\n\x04name\x18\x01 \x02(\t\x12$\n\x05value\x18\x02 \x02(\x0b\x32\x15.Mysqlx.Datatypes.Any\"C\n\x0c\x43\x61pabilities\x12\x33\n\x0c\x63\x61pabilities\x18\x01 \x03(\x0b\x32\x1d.Mysqlx.Connection.Capability\"\x11\n\x0f\x43\x61pabilitiesGet\"H\n\x0f\x43\x61pabilitiesSet\x12\x35\n\x0c\x63\x61pabilities\x18\x01 \x02(\x0b\x32\x1f.Mysqlx.Connection.Capabilities\"\x07\n\x05\x43loseB\x1e\n\x1c\x63om.mysql.cj.mysqlx.protobuf')
  ,
  dependencies=[mysqlx_datatypes_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CAPABILITY = _descriptor.Descriptor(
  name='Capability',
  full_name='Mysqlx.Connection.Capability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Mysqlx.Connection.Capability.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Mysqlx.Connection.Capability.value', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=134,
)


_CAPABILITIES = _descriptor.Descriptor(
  name='Capabilities',
  full_name='Mysqlx.Connection.Capabilities',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='capabilities', full_name='Mysqlx.Connection.Capabilities.capabilities', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=203,
)


_CAPABILITIESGET = _descriptor.Descriptor(
  name='CapabilitiesGet',
  full_name='Mysqlx.Connection.CapabilitiesGet',
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
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=205,
  serialized_end=222,
)


_CAPABILITIESSET = _descriptor.Descriptor(
  name='CapabilitiesSet',
  full_name='Mysqlx.Connection.CapabilitiesSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='capabilities', full_name='Mysqlx.Connection.CapabilitiesSet.capabilities', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=224,
  serialized_end=296,
)


_CLOSE = _descriptor.Descriptor(
  name='Close',
  full_name='Mysqlx.Connection.Close',
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
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=298,
  serialized_end=305,
)

_CAPABILITY.fields_by_name['value'].message_type = mysqlx_datatypes_pb2._ANY
_CAPABILITIES.fields_by_name['capabilities'].message_type = _CAPABILITY
_CAPABILITIESSET.fields_by_name['capabilities'].message_type = _CAPABILITIES
DESCRIPTOR.message_types_by_name['Capability'] = _CAPABILITY
DESCRIPTOR.message_types_by_name['Capabilities'] = _CAPABILITIES
DESCRIPTOR.message_types_by_name['CapabilitiesGet'] = _CAPABILITIESGET
DESCRIPTOR.message_types_by_name['CapabilitiesSet'] = _CAPABILITIESSET
DESCRIPTOR.message_types_by_name['Close'] = _CLOSE

Capability = _reflection.GeneratedProtocolMessageType('Capability', (_message.Message,), dict(
  DESCRIPTOR = _CAPABILITY,
  __module__ = 'mysqlx_connection_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Connection.Capability)
  ))
_sym_db.RegisterMessage(Capability)

Capabilities = _reflection.GeneratedProtocolMessageType('Capabilities', (_message.Message,), dict(
  DESCRIPTOR = _CAPABILITIES,
  __module__ = 'mysqlx_connection_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Connection.Capabilities)
  ))
_sym_db.RegisterMessage(Capabilities)

CapabilitiesGet = _reflection.GeneratedProtocolMessageType('CapabilitiesGet', (_message.Message,), dict(
  DESCRIPTOR = _CAPABILITIESGET,
  __module__ = 'mysqlx_connection_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Connection.CapabilitiesGet)
  ))
_sym_db.RegisterMessage(CapabilitiesGet)

CapabilitiesSet = _reflection.GeneratedProtocolMessageType('CapabilitiesSet', (_message.Message,), dict(
  DESCRIPTOR = _CAPABILITIESSET,
  __module__ = 'mysqlx_connection_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Connection.CapabilitiesSet)
  ))
_sym_db.RegisterMessage(CapabilitiesSet)

Close = _reflection.GeneratedProtocolMessageType('Close', (_message.Message,), dict(
  DESCRIPTOR = _CLOSE,
  __module__ = 'mysqlx_connection_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Connection.Close)
  ))
_sym_db.RegisterMessage(Close)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\034com.mysql.cj.mysqlx.protobuf'))
# @@protoc_insertion_point(module_scope)
