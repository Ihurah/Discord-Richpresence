Set WshShell = CreateObject("WScript.Shell")
' 第2引数の 0 は「ウィンドウを非表示にする」という命令です
WshShell.Run "cmd /c start.bat", 0, False
