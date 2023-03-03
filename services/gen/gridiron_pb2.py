# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gridiron.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0egridiron.proto\"a\n\x19\x43reateGridironGameRequest\x12\x10\n\x08homeTeam\x18\x01 \x01(\t\x12\x10\n\x08\x61wayTeam\x18\x02 \x01(\t\x12\x0e\n\x06userId\x18\x03 \x01(\t\x12\x10\n\x08leagueId\x18\x04 \x01(\t\",\n\x1a\x43reateGridironGameResponse\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"q\n\x17SetGridironEventRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\x12\x10\n\x08playType\x18\x02 \x01(\t\x12\x0e\n\x06period\x18\x03 \x01(\t\x12\x0f\n\x07teamFor\x18\x04 \x01(\t\x12\x13\n\x0bteamAgainst\x18\x05 \x01(\t\"+\n\x18SetGridironEventResponse\x12\x0f\n\x07\x65ventId\x18\x01 \x01(\t\"W\n\x16SetGridironRushRequest\x12\x0f\n\x07\x65ventId\x18\x01 \x01(\t\x12\x0e\n\x06player\x18\x02 \x01(\t\x12\x0c\n\x04yard\x18\x03 \x01(\x05\x12\x0e\n\x06result\x18\x04 \x01(\t\"*\n\x17SetGridironRushResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"y\n\x17SetGridironThrowRequest\x12\x0f\n\x07\x65ventId\x18\x01 \x01(\t\x12\x16\n\x0eplayerThrowing\x18\x02 \x01(\t\x12\x17\n\x0fplayerReceiving\x18\x03 \x01(\t\x12\x0c\n\x04yard\x18\x04 \x01(\x05\x12\x0e\n\x06result\x18\x05 \x01(\t\"+\n\x18SetGridironThrowResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"W\n\x16SetGridironKickRequest\x12\x0f\n\x07\x65ventId\x18\x01 \x01(\t\x12\x0e\n\x06player\x18\x02 \x01(\t\x12\x0c\n\x04yard\x18\x03 \x01(\x05\x12\x0e\n\x06result\x18\x04 \x01(\t\"*\n\x17SetGridironKickResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"N\n\x19SetGridironGameEndRequest\x12\x0f\n\x07\x65ventId\x18\x01 \x01(\t\x12\x0f\n\x07ptsHome\x18\x02 \x01(\x05\x12\x0f\n\x07ptsAway\x18\x03 \x01(\x05\"-\n\x1aSetGridironGameEndResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"-\n\x1bGetTotalRushingYardsRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"R\n\x1cGetTotalRushingYardsResponse\x12\x18\n\x10homeTeamResponse\x18\x01 \x01(\x02\x12\x18\n\x10\x61wayTeamResponse\x18\x02 \x01(\x02\"-\n\x1bGetTotalPassingYardsRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"R\n\x1cGetTotalPassingYardsResponse\x12\x18\n\x10homeTeamResponse\x18\x01 \x01(\x02\x12\x18\n\x10\x61wayTeamResponse\x18\x02 \x01(\x02\"+\n\x19GetAvgYardsPerPlayRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"P\n\x1aGetAvgYardsPerPlayResponse\x12\x18\n\x10homeTeamResponse\x18\x01 \x01(\x02\x12\x18\n\x10\x61wayTeamResponse\x18\x02 \x01(\x02\"+\n\x19GetTotalTouchdownsRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"P\n\x1aGetTotalTouchdownsResponse\x12\x18\n\x10homeTeamResponse\x18\x01 \x01(\x02\x12\x18\n\x10\x61wayTeamResponse\x18\x02 \x01(\x02\"*\n\x18GetTotalTurnoversRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"O\n\x19GetTotalTurnoversResponse\x12\x18\n\x10homeTeamResponse\x18\x01 \x01(\x02\x12\x18\n\x10\x61wayTeamResponse\x18\x02 \x01(\x02\":\n&GetTopFivePlayersByRushingYardsRequest\x12\x10\n\x08leagueId\x18\x01 \x01(\t\"9\n\'GetTopFivePlayersByRushingYardsResponse\x12\x0e\n\x06result\x18\x01 \x03(\x05\"<\n(GetTopFivePlayersByReceivingYardsRequest\x12\x10\n\x08leagueId\x18\x01 \x01(\t\";\n)GetTopFivePlayersByReceivingYardsResponse\x12\x0e\n\x06result\x18\x01 \x03(\x05\";\n\'GetTopFivePlayersByThrowingYardsRequest\x12\x10\n\x08leagueId\x18\x01 \x01(\t\":\n(GetTopFivePlayersByThrowingYardsResponse\x12\x0e\n\x06result\x18\x01 \x03(\x05\"7\n#GetTopFivePlayersByKicksMadeRequest\x12\x10\n\x08leagueId\x18\x01 \x01(\t\"6\n$GetTopFivePlayersByKicksMadeResponse\x12\x0e\n\x06result\x18\x01 \x03(\x05\"B\n.GetTopFivePlayersByCompletionPercentageRequest\x12\x10\n\x08leagueId\x18\x01 \x01(\t\"A\n/GetTopFivePlayersByCompletionPercentageResponse\x12\x0e\n\x06result\x18\x01 \x03(\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gridiron_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEGRIDIRONGAMEREQUEST._serialized_start=18
  _CREATEGRIDIRONGAMEREQUEST._serialized_end=115
  _CREATEGRIDIRONGAMERESPONSE._serialized_start=117
  _CREATEGRIDIRONGAMERESPONSE._serialized_end=161
  _SETGRIDIRONEVENTREQUEST._serialized_start=163
  _SETGRIDIRONEVENTREQUEST._serialized_end=276
  _SETGRIDIRONEVENTRESPONSE._serialized_start=278
  _SETGRIDIRONEVENTRESPONSE._serialized_end=321
  _SETGRIDIRONRUSHREQUEST._serialized_start=323
  _SETGRIDIRONRUSHREQUEST._serialized_end=410
  _SETGRIDIRONRUSHRESPONSE._serialized_start=412
  _SETGRIDIRONRUSHRESPONSE._serialized_end=454
  _SETGRIDIRONTHROWREQUEST._serialized_start=456
  _SETGRIDIRONTHROWREQUEST._serialized_end=577
  _SETGRIDIRONTHROWRESPONSE._serialized_start=579
  _SETGRIDIRONTHROWRESPONSE._serialized_end=622
  _SETGRIDIRONKICKREQUEST._serialized_start=624
  _SETGRIDIRONKICKREQUEST._serialized_end=711
  _SETGRIDIRONKICKRESPONSE._serialized_start=713
  _SETGRIDIRONKICKRESPONSE._serialized_end=755
  _SETGRIDIRONGAMEENDREQUEST._serialized_start=757
  _SETGRIDIRONGAMEENDREQUEST._serialized_end=835
  _SETGRIDIRONGAMEENDRESPONSE._serialized_start=837
  _SETGRIDIRONGAMEENDRESPONSE._serialized_end=882
  _GETTOTALRUSHINGYARDSREQUEST._serialized_start=884
  _GETTOTALRUSHINGYARDSREQUEST._serialized_end=929
  _GETTOTALRUSHINGYARDSRESPONSE._serialized_start=931
  _GETTOTALRUSHINGYARDSRESPONSE._serialized_end=1013
  _GETTOTALPASSINGYARDSREQUEST._serialized_start=1015
  _GETTOTALPASSINGYARDSREQUEST._serialized_end=1060
  _GETTOTALPASSINGYARDSRESPONSE._serialized_start=1062
  _GETTOTALPASSINGYARDSRESPONSE._serialized_end=1144
  _GETAVGYARDSPERPLAYREQUEST._serialized_start=1146
  _GETAVGYARDSPERPLAYREQUEST._serialized_end=1189
  _GETAVGYARDSPERPLAYRESPONSE._serialized_start=1191
  _GETAVGYARDSPERPLAYRESPONSE._serialized_end=1271
  _GETTOTALTOUCHDOWNSREQUEST._serialized_start=1273
  _GETTOTALTOUCHDOWNSREQUEST._serialized_end=1316
  _GETTOTALTOUCHDOWNSRESPONSE._serialized_start=1318
  _GETTOTALTOUCHDOWNSRESPONSE._serialized_end=1398
  _GETTOTALTURNOVERSREQUEST._serialized_start=1400
  _GETTOTALTURNOVERSREQUEST._serialized_end=1442
  _GETTOTALTURNOVERSRESPONSE._serialized_start=1444
  _GETTOTALTURNOVERSRESPONSE._serialized_end=1523
  _GETTOPFIVEPLAYERSBYRUSHINGYARDSREQUEST._serialized_start=1525
  _GETTOPFIVEPLAYERSBYRUSHINGYARDSREQUEST._serialized_end=1583
  _GETTOPFIVEPLAYERSBYRUSHINGYARDSRESPONSE._serialized_start=1585
  _GETTOPFIVEPLAYERSBYRUSHINGYARDSRESPONSE._serialized_end=1642
  _GETTOPFIVEPLAYERSBYRECEIVINGYARDSREQUEST._serialized_start=1644
  _GETTOPFIVEPLAYERSBYRECEIVINGYARDSREQUEST._serialized_end=1704
  _GETTOPFIVEPLAYERSBYRECEIVINGYARDSRESPONSE._serialized_start=1706
  _GETTOPFIVEPLAYERSBYRECEIVINGYARDSRESPONSE._serialized_end=1765
  _GETTOPFIVEPLAYERSBYTHROWINGYARDSREQUEST._serialized_start=1767
  _GETTOPFIVEPLAYERSBYTHROWINGYARDSREQUEST._serialized_end=1826
  _GETTOPFIVEPLAYERSBYTHROWINGYARDSRESPONSE._serialized_start=1828
  _GETTOPFIVEPLAYERSBYTHROWINGYARDSRESPONSE._serialized_end=1886
  _GETTOPFIVEPLAYERSBYKICKSMADEREQUEST._serialized_start=1888
  _GETTOPFIVEPLAYERSBYKICKSMADEREQUEST._serialized_end=1943
  _GETTOPFIVEPLAYERSBYKICKSMADERESPONSE._serialized_start=1945
  _GETTOPFIVEPLAYERSBYKICKSMADERESPONSE._serialized_end=1999
  _GETTOPFIVEPLAYERSBYCOMPLETIONPERCENTAGEREQUEST._serialized_start=2001
  _GETTOPFIVEPLAYERSBYCOMPLETIONPERCENTAGEREQUEST._serialized_end=2067
  _GETTOPFIVEPLAYERSBYCOMPLETIONPERCENTAGERESPONSE._serialized_start=2069
  _GETTOPFIVEPLAYERSBYCOMPLETIONPERCENTAGERESPONSE._serialized_end=2134
# @@protoc_insertion_point(module_scope)
