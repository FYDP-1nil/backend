# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamer.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0estreamer.proto\x12\x08streamer\"&\n\x16ObtainTwitchKeyRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\"&\n\x17ObtainTwitchKeyResponse\x12\x0b\n\x03key\x18\x01 \x01(\t\"\'\n\x17ObtainYoutubeKeyRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\"\'\n\x18ObtainYoutubeKeyResponse\x12\x0b\n\x03key\x18\x01 \x01(\t2\xbd\x01\n\x08Streamer\x12V\n\x0fObtainTwitchKey\x12 .streamer.ObtainTwitchKeyRequest\x1a!.streamer.ObtainTwitchKeyResponse\x12Y\n\x10ObtainYoutubeKey\x12!.streamer.ObtainYoutubeKeyRequest\x1a\".streamer.ObtainYoutubeKeyResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'streamer_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _OBTAINTWITCHKEYREQUEST._serialized_start=28
  _OBTAINTWITCHKEYREQUEST._serialized_end=66
  _OBTAINTWITCHKEYRESPONSE._serialized_start=68
  _OBTAINTWITCHKEYRESPONSE._serialized_end=106
  _OBTAINYOUTUBEKEYREQUEST._serialized_start=108
  _OBTAINYOUTUBEKEYREQUEST._serialized_end=147
  _OBTAINYOUTUBEKEYRESPONSE._serialized_start=149
  _OBTAINYOUTUBEKEYRESPONSE._serialized_end=188
  _STREAMER._serialized_start=191
  _STREAMER._serialized_end=380
# @@protoc_insertion_point(module_scope)
