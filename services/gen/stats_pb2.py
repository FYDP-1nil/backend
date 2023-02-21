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


from . import basketball_pb2 as basketball__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bstats.proto\x12\x05stats\x1a\x10\x62\x61sketball.proto\"G\n\x11\x43reateGameRequest\x12\x10\n\x08homeTeam\x18\x01 \x01(\t\x12\x10\n\x08\x61wayTeam\x18\x02 \x01(\t\x12\x0e\n\x06userId\x18\x03 \x01(\t\"$\n\x12\x43reateGameResponse\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"!\n\x0fGetShotsRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"R\n\x10GetShotsResponse\x12\x1c\n\x07teamFor\x18\x01 \x03(\x0b\x32\x0b.stats.Shot\x12 \n\x0bteamAgainst\x18\x02 \x03(\x0b\x32\x0b.stats.Shot\"!\n\x0fGetFoulsRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"R\n\x10GetFoulsResponse\x12\x1c\n\x07teamFor\x18\x01 \x03(\x0b\x32\x0b.stats.Foul\x12 \n\x0bteamAgainst\x18\x02 \x03(\x0b\x32\x0b.stats.Foul\"$\n\x12GetOffsidesRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"[\n\x13GetOffsidesResponse\x12\x1f\n\x07teamFor\x18\x01 \x03(\x0b\x32\x0e.stats.Offside\x12#\n\x0bteamAgainst\x18\x02 \x03(\x0b\x32\x0e.stats.Offside\"h\n\x0eSetShotRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\x12\x0f\n\x07teamFor\x18\x02 \x01(\t\x12\x13\n\x0bteamAgainst\x18\x03 \x01(\t\x12 \n\x0bshotDetails\x18\x04 \x01(\x0b\x32\x0b.stats.Shot\"\"\n\x0fSetShotResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"h\n\x0eSetFoulRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\x12\x0f\n\x07teamFor\x18\x02 \x01(\t\x12\x13\n\x0bteamAgainst\x18\x03 \x01(\t\x12 \n\x0b\x66oulDetails\x18\x04 \x01(\x0b\x32\x0b.stats.Foul\"\"\n\x0fSetFoulResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"q\n\x11SetOffsideRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\x12\x0f\n\x07teamFor\x18\x02 \x01(\t\x12\x13\n\x0bteamAgainst\x18\x03 \x01(\t\x12&\n\x0eoffsideDetails\x18\x04 \x01(\x0b\x32\x0e.stats.Offside\"%\n\x12SetOffsideResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"C\n\x0fSetEventRequest\x12\x11\n\teventType\x18\x01 \x01(\t\x12\x0e\n\x06gameId\x18\x02 \x01(\t\x12\r\n\x05\x65vent\x18\x03 \x01(\t\"#\n\x10SetEventResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"U\n\x04\x46oul\x12\x10\n\x08isYellow\x18\x01 \x01(\x08\x12\r\n\x05isRed\x18\x02 \x01(\x08\x12\x0e\n\x06player\x18\x03 \x01(\t\x12\x0e\n\x06reason\x18\x04 \x01(\t\x12\x0c\n\x04time\x18\x05 \x01(\x05\"X\n\x04Shot\x12\x0e\n\x06isGoal\x18\x01 \x01(\x08\x12\x12\n\nisOnTarget\x18\x02 \x01(\x08\x12\x0e\n\x06scorer\x18\x03 \x01(\t\x12\x0e\n\x06\x61ssist\x18\x04 \x01(\t\x12\x0c\n\x04time\x18\x05 \x01(\x05\"\x17\n\x07Offside\x12\x0c\n\x04time\x18\x01 \x01(\x05\x32\x95\r\n\x05Stats\x12;\n\x08GetShots\x12\x16.stats.GetShotsRequest\x1a\x17.stats.GetShotsResponse\x12;\n\x08GetFouls\x12\x16.stats.GetFoulsRequest\x1a\x17.stats.GetFoulsResponse\x12\x44\n\x0bGetOffsides\x12\x19.stats.GetOffsidesRequest\x1a\x1a.stats.GetOffsidesResponse\x12\x41\n\nCreateGame\x12\x18.stats.CreateGameRequest\x1a\x19.stats.CreateGameResponse\x12\x38\n\x07SetShot\x12\x15.stats.SetShotRequest\x1a\x16.stats.SetShotResponse\x12\x38\n\x07SetFoul\x12\x15.stats.SetFoulRequest\x1a\x16.stats.SetFoulResponse\x12\x41\n\nSetOffside\x12\x18.stats.SetOffsideRequest\x1a\x19.stats.SetOffsideResponse\x12;\n\x08SetEvent\x12\x16.stats.SetEventRequest\x1a\x17.stats.SetEventResponse\x12S\n\x14\x43reateBasketballGame\x12\x1c.CreateBasketballGameRequest\x1a\x1d.CreateBasketballGameResponse\x12M\n\x12SetBasketballEvent\x12\x1a.SetBasketballEventRequest\x1a\x1b.SetBasketballEventResponse\x12M\n\x12SetBasketballPoint\x12\x1a.SetBasketballPointRequest\x1a\x1b.SetBasketballPointResponse\x12M\n\x12SetBasketballSteal\x12\x1a.SetBasketballStealRequest\x1a\x1b.SetBasketballStealResponse\x12M\n\x12SetBasketballBlock\x12\x1a.SetBasketballBlockRequest\x1a\x1b.SetBasketballBlockResponse\x12J\n\x11SetBasketballFoul\x12\x19.SetBasketballFoulRequest\x1a\x1a.SetBasketballFoulResponse\x12V\n\x15SetBasketballTurnover\x12\x1d.SetBasketballTurnoverRequest\x1a\x1e.SetBasketballTurnoverResponse\x12S\n\x14SetBasketballGameEnd\x12\x1c.SetBasketballGameEndRequest\x1a\x1d.SetBasketballGameEndResponse\x12S\n\x14SetBasketballRebound\x12\x1c.SetBasketballReboundRequest\x1a\x1d.SetBasketballReboundResponse\x12Y\n\x16GetFieldGoalPercentage\x12\x1e.GetFieldGoalPercentageRequest\x1a\x1f.GetFieldGoalPercentageResponse\x12\\\n\x17GetThreePointPercentage\x12\x1f.GetThreePointPercentageRequest\x1a .GetThreePointPercentageResponse\x12J\n\x11GetFreeThrowsMade\x12\x19.GetFreeThrowsMadeRequest\x1a\x1a.GetFreeThrowsMadeResponse\x12\\\n\x17GetTotalTurnoversByTeam\x12\x1f.GetTotalTurnoversByTeamRequest\x1a .GetTotalTurnoversByTeamResponse\x12S\n\x14GetTotalStealsByTeam\x12\x1c.GetTotalStealsByTeamRequest\x1a\x1d.GetTotalStealsByTeamResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stats_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEGAMEREQUEST._serialized_start=40
  _CREATEGAMEREQUEST._serialized_end=111
  _CREATEGAMERESPONSE._serialized_start=113
  _CREATEGAMERESPONSE._serialized_end=149
  _GETSHOTSREQUEST._serialized_start=151
  _GETSHOTSREQUEST._serialized_end=184
  _GETSHOTSRESPONSE._serialized_start=186
  _GETSHOTSRESPONSE._serialized_end=268
  _GETFOULSREQUEST._serialized_start=270
  _GETFOULSREQUEST._serialized_end=303
  _GETFOULSRESPONSE._serialized_start=305
  _GETFOULSRESPONSE._serialized_end=387
  _GETOFFSIDESREQUEST._serialized_start=389
  _GETOFFSIDESREQUEST._serialized_end=425
  _GETOFFSIDESRESPONSE._serialized_start=427
  _GETOFFSIDESRESPONSE._serialized_end=518
  _SETSHOTREQUEST._serialized_start=520
  _SETSHOTREQUEST._serialized_end=624
  _SETSHOTRESPONSE._serialized_start=626
  _SETSHOTRESPONSE._serialized_end=660
  _SETFOULREQUEST._serialized_start=662
  _SETFOULREQUEST._serialized_end=766
  _SETFOULRESPONSE._serialized_start=768
  _SETFOULRESPONSE._serialized_end=802
  _SETOFFSIDEREQUEST._serialized_start=804
  _SETOFFSIDEREQUEST._serialized_end=917
  _SETOFFSIDERESPONSE._serialized_start=919
  _SETOFFSIDERESPONSE._serialized_end=956
  _SETEVENTREQUEST._serialized_start=958
  _SETEVENTREQUEST._serialized_end=1025
  _SETEVENTRESPONSE._serialized_start=1027
  _SETEVENTRESPONSE._serialized_end=1062
  _FOUL._serialized_start=1064
  _FOUL._serialized_end=1149
  _SHOT._serialized_start=1151
  _SHOT._serialized_end=1239
  _OFFSIDE._serialized_start=1241
  _OFFSIDE._serialized_end=1264
  _STATS._serialized_start=1267
  _STATS._serialized_end=2952
# @@protoc_insertion_point(module_scope)
