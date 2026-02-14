<div align="center">

# Discord-Richpresence
</div>

完全に自己満。付け加えて好きなソフトにしてね。

## 導入手順

### 1. ファイルのダウンロード
  **Download ZIP** からダウンロードし、好きな場所に配置。

### 2. ライブラリの準備
  ダウンロードしたフォルダのコマンドラインより、PythonからWindowsのウィンドウ情報を取得し、Discordへ送信するために以下のライブラリをインストールします。

      pip install pypresence pywin32 psutil

### 2. Discord Developer Portalなどの設定
   #### 2.1 <a href="https://discord.com/developers/applications">Discord Developer Portal</a>にアクセス  
  
   New Application > アクティビティに表示するソフト名を入力 > Create でアプリを作成
    
  
   #### 2.2 アクティビティに表示するソフトアイコンを設定
  
   Rich Presence > Rich Presence Assets > Add Image(s) より1024px × 1024pxの画像をアップロード

   #### 2.3 Application IDをコピペ
   General Information > Application IDをコピー > ダウンロードしたmain.pywの `CLIENT_ID` にペースト
   
   #### 2.4 各種設定
   タスクマネージャー > 詳細 で拡張子付きのソフト名を確認 > `TARGET_PROCESS` にコピー（例：Code.exe）

   `DETAILS` を書き換え、表示する詳細テキストを追加。（例：Coding...）  

   

### 4. 自動起動の設定手順
 `Win + R` で**ファイル名で指定して実行**を起動、 **`shell:startup`** と入力し、表示されたスタートアップフォルダに **silent_start.vbs のショートカット** を移動させます。

### 5. 実行
PCを再起動し、動作をテストします。


## 管理方法
### 動作確認
   PC起動後、タスクマネージャーの「詳細」タブに pythonw.exe がいれば成功です。

### 停止方法
   タスクマネージャーから pythonw.exe を右クリックし、「タスクの終了」で停止できます。
