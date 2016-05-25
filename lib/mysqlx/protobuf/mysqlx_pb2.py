# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mysqlx.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import mysqlx_sql_pb2
import mysqlx_resultset_pb2
import mysqlx_crud_pb2
import mysqlx_session_pb2
import mysqlx_connection_pb2
import mysqlx_expect_pb2
import mysqlx_notice_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mysqlx.proto',
  package='Mysqlx',
  serialized_pb=_b('\n\x0cmysqlx.proto\x12\x06Mysqlx\x1a\x10mysqlx_sql.proto\x1a\x16mysqlx_resultset.proto\x1a\x11mysqlx_crud.proto\x1a\x14mysqlx_session.proto\x1a\x17mysqlx_connection.proto\x1a\x13mysqlx_expect.proto\x1a\x13mysqlx_notice.proto\"\xb4\x02\n\x0e\x43lientMessages\"\xa1\x02\n\x04Type\x12\x18\n\x14\x43ON_CAPABILITIES_GET\x10\x01\x12\x18\n\x14\x43ON_CAPABILITIES_SET\x10\x02\x12\r\n\tCON_CLOSE\x10\x03\x12\x1b\n\x17SESS_AUTHENTICATE_START\x10\x04\x12\x1e\n\x1aSESS_AUTHENTICATE_CONTINUE\x10\x05\x12\x0e\n\nSESS_RESET\x10\x06\x12\x0e\n\nSESS_CLOSE\x10\x07\x12\x14\n\x10SQL_STMT_EXECUTE\x10\x0c\x12\r\n\tCRUD_FIND\x10\x11\x12\x0f\n\x0b\x43RUD_INSERT\x10\x12\x12\x0f\n\x0b\x43RUD_UPDATE\x10\x13\x12\x0f\n\x0b\x43RUD_DELETE\x10\x14\x12\x0f\n\x0b\x45XPECT_OPEN\x10\x18\x12\x10\n\x0c\x45XPECT_CLOSE\x10\x19\"\xe2\x02\n\x0eServerMessages\"\xcf\x02\n\x04Type\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\x15\n\x11\x43ONN_CAPABILITIES\x10\x02\x12\x1e\n\x1aSESS_AUTHENTICATE_CONTINUE\x10\x03\x12\x18\n\x14SESS_AUTHENTICATE_OK\x10\x04\x12\n\n\x06NOTICE\x10\x0b\x12\x1e\n\x1aRESULTSET_COLUMN_META_DATA\x10\x0c\x12\x11\n\rRESULTSET_ROW\x10\r\x12\x18\n\x14RESULTSET_FETCH_DONE\x10\x0e\x12\x1d\n\x19RESULTSET_FETCH_SUSPENDED\x10\x0f\x12(\n$RESULTSET_FETCH_DONE_MORE_RESULTSETS\x10\x10\x12\x17\n\x13SQL_STMT_EXECUTE_OK\x10\x11\x12(\n$RESULTSET_FETCH_DONE_MORE_OUT_PARAMS\x10\x12\"\x11\n\x02Ok\x12\x0b\n\x03msg\x18\x01 \x01(\t\"\x88\x01\n\x05\x45rror\x12/\n\x08severity\x18\x01 \x01(\x0e\x32\x16.Mysqlx.Error.Severity:\x05\x45RROR\x12\x0c\n\x04\x63ode\x18\x02 \x02(\r\x12\x11\n\tsql_state\x18\x04 \x02(\t\x12\x0b\n\x03msg\x18\x03 \x02(\t\" \n\x08Severity\x12\t\n\x05\x45RROR\x10\x00\x12\t\n\x05\x46\x41TAL\x10\x01\x42\x1e\n\x1c\x63om.mysql.cj.mysqlx.protobuf')
  ,
  dependencies=[mysqlx_sql_pb2.DESCRIPTOR,mysqlx_resultset_pb2.DESCRIPTOR,mysqlx_crud_pb2.DESCRIPTOR,mysqlx_session_pb2.DESCRIPTOR,mysqlx_connection_pb2.DESCRIPTOR,mysqlx_expect_pb2.DESCRIPTOR,mysqlx_notice_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CLIENTMESSAGES_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Mysqlx.ClientMessages.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CON_CAPABILITIES_GET', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CON_CAPABILITIES_SET', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CON_CLOSE', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESS_AUTHENTICATE_START', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESS_AUTHENTICATE_CONTINUE', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESS_RESET', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESS_CLOSE', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SQL_STMT_EXECUTE', index=7, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRUD_FIND', index=8, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRUD_INSERT', index=9, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRUD_UPDATE', index=10, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRUD_DELETE', index=11, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPECT_OPEN', index=12, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPECT_CLOSE', index=13, number=25,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=194,
  serialized_end=483,
)
_sym_db.RegisterEnumDescriptor(_CLIENTMESSAGES_TYPE)

_SERVERMESSAGES_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Mysqlx.ServerMessages.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONN_CAPABILITIES', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESS_AUTHENTICATE_CONTINUE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESS_AUTHENTICATE_OK', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOTICE', index=5, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULTSET_COLUMN_META_DATA', index=6, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULTSET_ROW', index=7, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULTSET_FETCH_DONE', index=8, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULTSET_FETCH_SUSPENDED', index=9, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULTSET_FETCH_DONE_MORE_RESULTSETS', index=10, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SQL_STMT_EXECUTE_OK', index=11, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESULTSET_FETCH_DONE_MORE_OUT_PARAMS', index=12, number=18,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=505,
  serialized_end=840,
)
_sym_db.RegisterEnumDescriptor(_SERVERMESSAGES_TYPE)

_ERROR_SEVERITY = _descriptor.EnumDescriptor(
  name='Severity',
  full_name='Mysqlx.Error.Severity',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FATAL', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=966,
  serialized_end=998,
)
_sym_db.RegisterEnumDescriptor(_ERROR_SEVERITY)


_CLIENTMESSAGES = _descriptor.Descriptor(
  name='ClientMessages',
  full_name='Mysqlx.ClientMessages',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLIENTMESSAGES_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=175,
  serialized_end=483,
)


_SERVERMESSAGES = _descriptor.Descriptor(
  name='ServerMessages',
  full_name='Mysqlx.ServerMessages',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SERVERMESSAGES_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=486,
  serialized_end=840,
)


_OK = _descriptor.Descriptor(
  name='Ok',
  full_name='Mysqlx.Ok',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='Mysqlx.Ok.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=842,
  serialized_end=859,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='Mysqlx.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='severity', full_name='Mysqlx.Error.severity', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='Mysqlx.Error.code', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sql_state', full_name='Mysqlx.Error.sql_state', index=2,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='Mysqlx.Error.msg', index=3,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ERROR_SEVERITY,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=862,
  serialized_end=998,
)

_CLIENTMESSAGES_TYPE.containing_type = _CLIENTMESSAGES
_SERVERMESSAGES_TYPE.containing_type = _SERVERMESSAGES
_ERROR.fields_by_name['severity'].enum_type = _ERROR_SEVERITY
_ERROR_SEVERITY.containing_type = _ERROR
DESCRIPTOR.message_types_by_name['ClientMessages'] = _CLIENTMESSAGES
DESCRIPTOR.message_types_by_name['ServerMessages'] = _SERVERMESSAGES
DESCRIPTOR.message_types_by_name['Ok'] = _OK
DESCRIPTOR.message_types_by_name['Error'] = _ERROR

ClientMessages = _reflection.GeneratedProtocolMessageType('ClientMessages', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTMESSAGES,
  __module__ = 'mysqlx_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.ClientMessages)
  ))
_sym_db.RegisterMessage(ClientMessages)

ServerMessages = _reflection.GeneratedProtocolMessageType('ServerMessages', (_message.Message,), dict(
  DESCRIPTOR = _SERVERMESSAGES,
  __module__ = 'mysqlx_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.ServerMessages)
  ))
_sym_db.RegisterMessage(ServerMessages)

Ok = _reflection.GeneratedProtocolMessageType('Ok', (_message.Message,), dict(
  DESCRIPTOR = _OK,
  __module__ = 'mysqlx_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Ok)
  ))
_sym_db.RegisterMessage(Ok)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
  DESCRIPTOR = _ERROR,
  __module__ = 'mysqlx_pb2'
  # @@protoc_insertion_point(class_scope:Mysqlx.Error)
  ))
_sym_db.RegisterMessage(Error)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\034com.mysql.cj.mysqlx.protobuf'))
# @@protoc_insertion_point(module_scope)
