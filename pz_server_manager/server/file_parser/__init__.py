"""
Filename format: dd-mm-yy_hh-mm-ss_%logname%.txt
Lognames and formats:
    * DebugLog-server: [dd-mm-yy hh:mm:ss.fff] %LEVEL%  : %Type% , $timestamp> $x,$y,$z> %Event text%.
    * chat: [dd-mm-yy hh:mm:ss.fff][%level%] %message%.
    * pvp
    * cmd: [dd-mm-yy hh:mm:ss.fff] $steamid "%username%" %action% @ $x,$y,$z.
    * PerkLog
    * admin: [dd-mm-yy hh:mm:ss.fff] %username% %action%.
    * item: [dd-mm-yy hh:mm:ss.fff] $steamid "%username%" $containertype $valuechange $x,$y,$z $items.
    * ClientActionLog: [dd-mm-yy hh:mm:ss.fff] [$steamid][$action][%username%][$x,$y,$z][$item]
    * map: [dd-mm-yy hh:mm:ss.fff] $steamid "%username%" %action% ($item) at $x,$y,$z.
    * user: [dd-mm-yy hh:mm:ss.fff] %message%.
"""