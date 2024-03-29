# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: basketball.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x62\x61sketball.proto\"S\n\x1b\x43reateBasketballGameRequest\x12\x10\n\x08homeTeam\x18\x01 \x01(\t\x12\x10\n\x08\x61wayTeam\x18\x02 \x01(\t\x12\x10\n\x08leagueId\x18\x03 \x01(\t\".\n\x1c\x43reateBasketballGameResponse\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"s\n\x19SetBasketballEventRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\x12\x10\n\x08playType\x18\x02 \x01(\t\x12\x0e\n\x06period\x18\x03 \x01(\t\x12\x0f\n\x07teamFor\x18\x04 \x01(\t\x12\x13\n\x0bteamAgainst\x18\x05 \x01(\t\"-\n\x1aSetBasketballEventResponse\x12\x0f\n\x07\x65ventId\x18\x01 \x01(\t\"k\n\x19SetBasketballPointRequest\x12\x0f\n\x07\x65ventId\x18\x01 \x01(\t\x12\x0e\n\x06player\x18\x02 \x01(\t\x12\x0e\n\x06\x61ssist\x18\x03 \x01(\t\x12\x0e\n\x06result\x18\x04 \x01(\t\x12\r\n\x05point\x18\x05 \x01(\t\"-\n\x1aSetBasketballPointResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"<\n\x19SetBasketballStealRequest\x12\x0f\n\x07\x65ventId\x18\x01 \x01(\t\x12\x0e\n\x06player\x18\x02 \x01(\t\"-\n\x1aSetBasketballStealResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"<\n\x19SetBasketballBlockRequest\x12\x0f\n\x07\x65ventId\x18\x01 \x01(\t\x12\x0e\n\x06player\x18\x02 \x01(\t\"-\n\x1aSetBasketballBlockResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"K\n\x18SetBasketballFoulRequest\x12\x0f\n\x07\x65ventId\x18\x01 \x01(\t\x12\x0e\n\x06player\x18\x02 \x01(\t\x12\x0e\n\x06reason\x18\x03 \x01(\t\",\n\x19SetBasketballFoulResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"?\n\x1cSetBasketballTurnoverRequest\x12\x0f\n\x07\x65ventId\x18\x01 \x01(\t\x12\x0e\n\x06player\x18\x02 \x01(\t\"0\n\x1dSetBasketballTurnoverResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\">\n\x1bSetBasketballReboundRequest\x12\x0f\n\x07\x65ventId\x18\x01 \x01(\t\x12\x0e\n\x06player\x18\x02 \x01(\t\"/\n\x1cSetBasketballReboundResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"P\n\x1bSetBasketballGameEndRequest\x12\x0f\n\x07\x65ventId\x18\x01 \x01(\t\x12\x0f\n\x07ptsHome\x18\x02 \x01(\x05\x12\x0f\n\x07ptsAway\x18\x03 \x01(\x05\"/\n\x1cSetBasketballGameEndResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"/\n\x1dGetFieldGoalPercentageRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"N\n\x1eGetFieldGoalPercentageResponse\x12\x13\n\x0bteamForStat\x18\x01 \x01(\x02\x12\x17\n\x0fteamAgainstStat\x18\x02 \x01(\x02\"0\n\x1eGetThreePointPercentageRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"O\n\x1fGetThreePointPercentageResponse\x12\x13\n\x0bteamForStat\x18\x01 \x01(\x02\x12\x17\n\x0fteamAgainstStat\x18\x02 \x01(\x02\"*\n\x18GetFreeThrowsMadeRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"I\n\x19GetFreeThrowsMadeResponse\x12\x13\n\x0bteamForStat\x18\x01 \x01(\x02\x12\x17\n\x0fteamAgainstStat\x18\x02 \x01(\x02\"0\n\x1eGetTotalTurnoversByTeamRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"O\n\x1fGetTotalTurnoversByTeamResponse\x12\x13\n\x0bteamForStat\x18\x01 \x01(\x02\x12\x17\n\x0fteamAgainstStat\x18\x02 \x01(\x02\"-\n\x1bGetTotalStealsByTeamRequest\x12\x0e\n\x06gameId\x18\x01 \x01(\t\"L\n\x1cGetTotalStealsByTeamResponse\x12\x13\n\x0bteamForStat\x18\x01 \x01(\x02\x12\x17\n\x0fteamAgainstStat\x18\x02 \x01(\x02\";\n\'GetTopFivePlayersByPointsPerGameRequest\x12\x10\n\x08leagueId\x18\x01 \x01(\t\"W\n(GetTopFivePlayersByPointsPerGameResponse\x12+\n\x04resp\x18\x01 \x03(\x0b\x32\x1d.BasketballLeagueStatResponse\"=\n)GetTopFivePlayersByReboundsPerGameRequest\x12\x10\n\x08leagueId\x18\x01 \x01(\t\"Y\n*GetTopFivePlayersByReboundsPerGameResponse\x12+\n\x04resp\x18\x01 \x03(\x0b\x32\x1d.BasketballLeagueStatResponse\"<\n(GetTopFivePlayersByAssistsPerGameRequest\x12\x10\n\x08leagueId\x18\x01 \x01(\t\"X\n)GetTopFivePlayersByAssistsPerGameResponse\x12+\n\x04resp\x18\x01 \x03(\x0b\x32\x1d.BasketballLeagueStatResponse\";\n\'GetTopFivePlayersByBlocksPerGameRequest\x12\x10\n\x08leagueId\x18\x01 \x01(\t\"W\n(GetTopFivePlayersByBlocksPerGameResponse\x12+\n\x04resp\x18\x01 \x03(\x0b\x32\x1d.BasketballLeagueStatResponse\";\n\'GetTopFivePlayersByStealsPerGameRequest\x12\x10\n\x08leagueId\x18\x01 \x01(\t\"W\n(GetTopFivePlayersByStealsPerGameResponse\x12+\n\x04resp\x18\x01 \x03(\x0b\x32\x1d.BasketballLeagueStatResponse\"A\n-GetTopFivePlayersByFieldGoalPercentageRequest\x12\x10\n\x08leagueId\x18\x01 \x01(\t\"]\n.GetTopFivePlayersByFieldGoalPercentageResponse\x12+\n\x04resp\x18\x01 \x03(\x0b\x32\x1d.BasketballLeagueStatResponse\";\n\'GetTopFivePlayersBy3ptPercentageRequest\x12\x10\n\x08leagueId\x18\x01 \x01(\t\"W\n(GetTopFivePlayersBy3ptPercentageResponse\x12+\n\x04resp\x18\x01 \x03(\x0b\x32\x1d.BasketballLeagueStatResponse\"A\n-GetTopFivePlayersByFreeThrowPercentageRequest\x12\x10\n\x08leagueId\x18\x01 \x01(\t\"]\n.GetTopFivePlayersByFreeThrowPercentageResponse\x12+\n\x04resp\x18\x01 \x03(\x0b\x32\x1d.BasketballLeagueStatResponse\"@\n\x1c\x42\x61sketballLeagueStatResponse\x12\x12\n\nplayerName\x18\x01 \x01(\t\x12\x0c\n\x04stat\x18\x02 \x01(\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'basketball_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEBASKETBALLGAMEREQUEST._serialized_start=20
  _CREATEBASKETBALLGAMEREQUEST._serialized_end=103
  _CREATEBASKETBALLGAMERESPONSE._serialized_start=105
  _CREATEBASKETBALLGAMERESPONSE._serialized_end=151
  _SETBASKETBALLEVENTREQUEST._serialized_start=153
  _SETBASKETBALLEVENTREQUEST._serialized_end=268
  _SETBASKETBALLEVENTRESPONSE._serialized_start=270
  _SETBASKETBALLEVENTRESPONSE._serialized_end=315
  _SETBASKETBALLPOINTREQUEST._serialized_start=317
  _SETBASKETBALLPOINTREQUEST._serialized_end=424
  _SETBASKETBALLPOINTRESPONSE._serialized_start=426
  _SETBASKETBALLPOINTRESPONSE._serialized_end=471
  _SETBASKETBALLSTEALREQUEST._serialized_start=473
  _SETBASKETBALLSTEALREQUEST._serialized_end=533
  _SETBASKETBALLSTEALRESPONSE._serialized_start=535
  _SETBASKETBALLSTEALRESPONSE._serialized_end=580
  _SETBASKETBALLBLOCKREQUEST._serialized_start=582
  _SETBASKETBALLBLOCKREQUEST._serialized_end=642
  _SETBASKETBALLBLOCKRESPONSE._serialized_start=644
  _SETBASKETBALLBLOCKRESPONSE._serialized_end=689
  _SETBASKETBALLFOULREQUEST._serialized_start=691
  _SETBASKETBALLFOULREQUEST._serialized_end=766
  _SETBASKETBALLFOULRESPONSE._serialized_start=768
  _SETBASKETBALLFOULRESPONSE._serialized_end=812
  _SETBASKETBALLTURNOVERREQUEST._serialized_start=814
  _SETBASKETBALLTURNOVERREQUEST._serialized_end=877
  _SETBASKETBALLTURNOVERRESPONSE._serialized_start=879
  _SETBASKETBALLTURNOVERRESPONSE._serialized_end=927
  _SETBASKETBALLREBOUNDREQUEST._serialized_start=929
  _SETBASKETBALLREBOUNDREQUEST._serialized_end=991
  _SETBASKETBALLREBOUNDRESPONSE._serialized_start=993
  _SETBASKETBALLREBOUNDRESPONSE._serialized_end=1040
  _SETBASKETBALLGAMEENDREQUEST._serialized_start=1042
  _SETBASKETBALLGAMEENDREQUEST._serialized_end=1122
  _SETBASKETBALLGAMEENDRESPONSE._serialized_start=1124
  _SETBASKETBALLGAMEENDRESPONSE._serialized_end=1171
  _GETFIELDGOALPERCENTAGEREQUEST._serialized_start=1173
  _GETFIELDGOALPERCENTAGEREQUEST._serialized_end=1220
  _GETFIELDGOALPERCENTAGERESPONSE._serialized_start=1222
  _GETFIELDGOALPERCENTAGERESPONSE._serialized_end=1300
  _GETTHREEPOINTPERCENTAGEREQUEST._serialized_start=1302
  _GETTHREEPOINTPERCENTAGEREQUEST._serialized_end=1350
  _GETTHREEPOINTPERCENTAGERESPONSE._serialized_start=1352
  _GETTHREEPOINTPERCENTAGERESPONSE._serialized_end=1431
  _GETFREETHROWSMADEREQUEST._serialized_start=1433
  _GETFREETHROWSMADEREQUEST._serialized_end=1475
  _GETFREETHROWSMADERESPONSE._serialized_start=1477
  _GETFREETHROWSMADERESPONSE._serialized_end=1550
  _GETTOTALTURNOVERSBYTEAMREQUEST._serialized_start=1552
  _GETTOTALTURNOVERSBYTEAMREQUEST._serialized_end=1600
  _GETTOTALTURNOVERSBYTEAMRESPONSE._serialized_start=1602
  _GETTOTALTURNOVERSBYTEAMRESPONSE._serialized_end=1681
  _GETTOTALSTEALSBYTEAMREQUEST._serialized_start=1683
  _GETTOTALSTEALSBYTEAMREQUEST._serialized_end=1728
  _GETTOTALSTEALSBYTEAMRESPONSE._serialized_start=1730
  _GETTOTALSTEALSBYTEAMRESPONSE._serialized_end=1806
  _GETTOPFIVEPLAYERSBYPOINTSPERGAMEREQUEST._serialized_start=1808
  _GETTOPFIVEPLAYERSBYPOINTSPERGAMEREQUEST._serialized_end=1867
  _GETTOPFIVEPLAYERSBYPOINTSPERGAMERESPONSE._serialized_start=1869
  _GETTOPFIVEPLAYERSBYPOINTSPERGAMERESPONSE._serialized_end=1956
  _GETTOPFIVEPLAYERSBYREBOUNDSPERGAMEREQUEST._serialized_start=1958
  _GETTOPFIVEPLAYERSBYREBOUNDSPERGAMEREQUEST._serialized_end=2019
  _GETTOPFIVEPLAYERSBYREBOUNDSPERGAMERESPONSE._serialized_start=2021
  _GETTOPFIVEPLAYERSBYREBOUNDSPERGAMERESPONSE._serialized_end=2110
  _GETTOPFIVEPLAYERSBYASSISTSPERGAMEREQUEST._serialized_start=2112
  _GETTOPFIVEPLAYERSBYASSISTSPERGAMEREQUEST._serialized_end=2172
  _GETTOPFIVEPLAYERSBYASSISTSPERGAMERESPONSE._serialized_start=2174
  _GETTOPFIVEPLAYERSBYASSISTSPERGAMERESPONSE._serialized_end=2262
  _GETTOPFIVEPLAYERSBYBLOCKSPERGAMEREQUEST._serialized_start=2264
  _GETTOPFIVEPLAYERSBYBLOCKSPERGAMEREQUEST._serialized_end=2323
  _GETTOPFIVEPLAYERSBYBLOCKSPERGAMERESPONSE._serialized_start=2325
  _GETTOPFIVEPLAYERSBYBLOCKSPERGAMERESPONSE._serialized_end=2412
  _GETTOPFIVEPLAYERSBYSTEALSPERGAMEREQUEST._serialized_start=2414
  _GETTOPFIVEPLAYERSBYSTEALSPERGAMEREQUEST._serialized_end=2473
  _GETTOPFIVEPLAYERSBYSTEALSPERGAMERESPONSE._serialized_start=2475
  _GETTOPFIVEPLAYERSBYSTEALSPERGAMERESPONSE._serialized_end=2562
  _GETTOPFIVEPLAYERSBYFIELDGOALPERCENTAGEREQUEST._serialized_start=2564
  _GETTOPFIVEPLAYERSBYFIELDGOALPERCENTAGEREQUEST._serialized_end=2629
  _GETTOPFIVEPLAYERSBYFIELDGOALPERCENTAGERESPONSE._serialized_start=2631
  _GETTOPFIVEPLAYERSBYFIELDGOALPERCENTAGERESPONSE._serialized_end=2724
  _GETTOPFIVEPLAYERSBY3PTPERCENTAGEREQUEST._serialized_start=2726
  _GETTOPFIVEPLAYERSBY3PTPERCENTAGEREQUEST._serialized_end=2785
  _GETTOPFIVEPLAYERSBY3PTPERCENTAGERESPONSE._serialized_start=2787
  _GETTOPFIVEPLAYERSBY3PTPERCENTAGERESPONSE._serialized_end=2874
  _GETTOPFIVEPLAYERSBYFREETHROWPERCENTAGEREQUEST._serialized_start=2876
  _GETTOPFIVEPLAYERSBYFREETHROWPERCENTAGEREQUEST._serialized_end=2941
  _GETTOPFIVEPLAYERSBYFREETHROWPERCENTAGERESPONSE._serialized_start=2943
  _GETTOPFIVEPLAYERSBYFREETHROWPERCENTAGERESPONSE._serialized_end=3036
  _BASKETBALLLEAGUESTATRESPONSE._serialized_start=3038
  _BASKETBALLLEAGUESTATRESPONSE._serialized_end=3102
# @@protoc_insertion_point(module_scope)
