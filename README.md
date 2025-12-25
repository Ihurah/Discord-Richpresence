<div align="center">

# Discord-Richpresence
</div>

完全に自己満。加えて好きなソフトにしてね。

## 導入手順

### 1. ファイルのダウンロード
  **Download ZIP** からダウンロードし、好きな場所に配置。

### 2. batファイルの作成
  PC起動時に自動的に実行されるようにするため、 **`autostart.bat`** （ファイル名は何でも良い）を作成。  

      @echo off  
      start "" "C:\Users\***\AppData\Local\Programs\Python\Python310\pythonw.exe" "C:\Users\***\..." > 
      exit  
 `C:\Users\***\AppData\Local\Programs\Python\Python310\pythonw.exe` はPythonの実行ファイルのパスを貼り付け、  

 `C:\Users\***\...` にはmain.pywのパスを貼り付けます。

### 3. batファイルの配置
 `Win + R` で**ファイル名で指定して実行**を起動、 **`shell:startup`** と入力し、表示されたスタートアップフォルダに **`autostart.bat`** を移動させます。

### 4. 実行
PCを再起動し、動作をテストします。
