# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stats.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bstats.proto\x12\x05stats\"G\n\x11\x43reateGameRequest\x12\x10\n\x08homeTeam\x18\x01 \x01(\t\x12\x10\n\x08\x61wayTeam\x18\x02 \x01(\t\x12\x0e\n\x06userId\x18\x03 \x01(\t\"$\n\x12\x43reateGameResponse\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"!\n\x0fGetShotsRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"R\n\x10GetShotsResponse\x12\x1c\n\x07teamFor\x18\x01 \x03(\x0b\x32\x0b.stats.Shot\x12 \n\x0bteamAgainst\x18\x02 \x03(\x0b\x32\x0b.stats.Shot\"!\n\x0fGetFoulsRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"R\n\x10GetFoulsResponse\x12\x1c\n\x07teamFor\x18\x01 \x03(\x0b\x32\x0b.stats.Foul\x12 \n\x0bteamAgainst\x18\x02 \x03(\x0b\x32\x0b.stats.Foul\"$\n\x12GetOffsidesRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"[\n\x13GetOffsidesResponse\x12\x1f\n\x07teamFor\x18\x01 \x03(\x0b\x32\x0e.stats.Offside\x12#\n\x0bteamAgainst\x18\x02 \x03(\x0b\x32\x0e.stats.Offside\"h\n\x0eSetShotRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\x12\x0f\n\x07teamFor\x18\x02 \x01(\t\x12\x13\n\x0bteamAgainst\x18\x03 \x01(\t\x12 \n\x0bshotDetails\x18\x04 \x01(\x0b\x32\x0b.stats.Shot\"\"\n\x0fSetShotResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"h\n\x0eSetFoulRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\x12\x0f\n\x07teamFor\x18\x02 \x01(\t\x12\x13\n\x0bteamAgainst\x18\x03 \x01(\t\x12 \n\x0b\x66oulDetails\x18\x04 \x01(\x0b\x32\x0b.stats.Foul\"\"\n\x0fSetFoulResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"q\n\x11SetOffsideRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\x12\x0f\n\x07teamFor\x18\x02 \x01(\t\x12\x13\n\x0bteamAgainst\x18\x03 \x01(\t\x12&\n\x0eoffsideDetails\x18\x04 \x01(\x0b\x32\x0e.stats.Offside\"%\n\x12SetOffsideResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"C\n\x0fSetEventRequest\x12\x11\n\teventType\x18\x01 \x01(\t\x12\x0e\n\x06gameId\x18\x02 \x01(\t\x12\r\n\x05\x65vent\x18\x03 \x01(\t\"#\n\x10SetEventResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"U\n\x04\x46oul\x12\x10\n\x08isYellow\x18\x01 \x01(\x08\x12\r\n\x05isRed\x18\x02 \x01(\x08\x12\x0e\n\x06player\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\x12\x0c\n\x04time\x18\x05 \x01(\x05\"X\n\x04Shot\x12\x0e\n\x06isGoal\x18\x01 \x01(\x08\x12\x12\n\nisOnTarget\x18\x02 \x01(\x08\x12\x0e\n\x06scorer\x18\x03 \x01(\t\x12\x0e\n\x06\x61ssist\x18\x04 \x01(\t\x12\x0c\n\x04time\x18\x05 \x01(\x05\"\x17\n\x07Offside\x12\x0c\n\x04time\x18\x01 \x01(\x05\x32\xfe\x03\n\x05Stats\x12\x41\n\nCreateGame\x12\x18.stats.CreateGameRequest\x1a\x19.stats.CreateGameResponse\x12;\n\x08GetShots\x12\x16.stats.GetShotsRequest\x1a\x17.stats.GetShotsResponse\x12;\n\x08GetFouls\x12\x16.stats.GetFoulsRequest\x1a\x17.stats.GetFoulsResponse\x12\x44\n\x0bGetOffsides\x12\x19.stats.GetOffsidesRequest\x1a\x1a.stats.GetOffsidesResponse\x12\x38\n\x07SetShot\x12\x15.stats.SetShotRequest\x1a\x16.stats.SetShotResponse\x12\x38\n\x07SetFoul\x12\x15.stats.SetFoulRequest\x1a\x16.stats.SetFoulResponse\x12\x41\n\nSetOffside\x12\x18.stats.SetOffsideRequest\x1a\x19.stats.SetOffsideResponse\x12;\n\x08SetEvent\x12\x16.stats.SetEventRequest\x1a\x17.stats.SetEventResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stats_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEGAMEREQUEST._serialized_start=22
  _CREATEGAMEREQUEST._serialized_end=93
  _CREATEGAMERESPONSE._serialized_start=95
  _CREATEGAMERESPONSE._serialized_end=131
  _GETSHOTSREQUEST._serialized_start=133
  _GETSHOTSREQUEST._serialized_end=166
  _GETSHOTSRESPONSE._serialized_start=168
  _GETSHOTSRESPONSE._serialized_end=250
  _GETFOULSREQUEST._serialized_start=252
  _GETFOULSREQUEST._serialized_end=285
  _GETFOULSRESPONSE._serialized_start=287
  _GETFOULSRESPONSE._serialized_end=369
  _GETOFFSIDESREQUEST._serialized_start=371
  _GETOFFSIDESREQUEST._serialized_end=407
  _GETOFFSIDESRESPONSE._serialized_start=409
  _GETOFFSIDESRESPONSE._serialized_end=500
  _SETSHOTREQUEST._serialized_start=502
  _SETSHOTREQUEST._serialized_end=606
  _SETSHOTRESPONSE._serialized_start=608
  _SETSHOTRESPONSE._serialized_end=642
  _SETFOULREQUEST._serialized_start=644
  _SETFOULREQUEST._serialized_end=748
  _SETFOULRESPONSE._serialized_start=750
  _SETFOULRESPONSE._serialized_end=784
  _SETOFFSIDEREQUEST._serialized_start=786
  _SETOFFSIDEREQUEST._serialized_end=899
  _SETOFFSIDERESPONSE._serialized_start=901
  _SETOFFSIDERESPONSE._serialized_end=938
  _SETEVENTREQUEST._serialized_start=940
  _SETEVENTREQUEST._serialized_end=1007
  _SETEVENTRESPONSE._serialized_start=1009
  _SETEVENTRESPONSE._serialized_end=1044
  _FOUL._serialized_start=1046
  _FOUL._serialized_end=1131
  _SHOT._serialized_start=1133
  _SHOT._serialized_end=1221
  _OFFSIDE._serialized_start=1223
  _OFFSIDE._serialized_end=1246
  _STATS._serialized_start=1249
  _STATS._serialized_end=1759
# @@protoc_insertion_point(module_scope)
