# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: locadoraCarro.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'locadoraCarro.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13locadoraCarro.proto\x12\rlocadoraCarro\"I\n\x0e\x42ookCarRequest\x12\x11\n\tcar_model\x18\x01 \x01(\t\x12\x12\n\nstart_date\x18\x02 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x03 \x01(\t\"J\n\x0f\x42ookCarResponse\x12\x0e\n\x06sucess\x18\x01 \x01(\x08\x12\x0f\n\x02id\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x0f\n\x07message\x18\x03 \x01(\tB\x05\n\x03_id\"\"\n\x14\x43\x61ncelBookCarRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"8\n\x15\x43\x61ncelBookCarResponse\x12\x0e\n\x06sucess\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xb5\x01\n\rLocadoraCarro\x12H\n\x07\x42ookCar\x12\x1d.locadoraCarro.BookCarRequest\x1a\x1e.locadoraCarro.BookCarResponse\x12Z\n\rCancelBookCar\x12#.locadoraCarro.CancelBookCarRequest\x1a$.locadoraCarro.CancelBookCarResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'locadoraCarro_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_BOOKCARREQUEST']._serialized_start=38
  _globals['_BOOKCARREQUEST']._serialized_end=111
  _globals['_BOOKCARRESPONSE']._serialized_start=113
  _globals['_BOOKCARRESPONSE']._serialized_end=187
  _globals['_CANCELBOOKCARREQUEST']._serialized_start=189
  _globals['_CANCELBOOKCARREQUEST']._serialized_end=223
  _globals['_CANCELBOOKCARRESPONSE']._serialized_start=225
  _globals['_CANCELBOOKCARRESPONSE']._serialized_end=281
  _globals['_LOCADORACARRO']._serialized_start=284
  _globals['_LOCADORACARRO']._serialized_end=465
# @@protoc_insertion_point(module_scope)
