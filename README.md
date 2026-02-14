<div align="center">

# Discord-Richpresence
</div>

完全に自己満。付け加えて好きなソフトにしてね。

## 導入手順

### 1. ファイルのダウンロード
  **Download ZIP** からダウンロードし、好きな場所に配置。

### 2. ライブラリの準備
  コマンドラインより、PythonからWindowsのウィンドウ情報を取得し、Discordへ送信するために以下のライブラリをインストールします。

      pip install pypresence pywin32 psutil

### 3. 自動起動の設定手順
 `Win + R` で**ファイル名で指定して実行**を起動、 **`shell:startup`** と入力し、表示されたスタートアップフォルダに **silent_start.vbsのショートカット** を移動させます。

### 4. 実行
PCを再起動し、動作をテストします。


## 管理方法
### 動作確認
   PC起動後、タスクマネージャーの「詳細」タブに pythonw.exe がいれば成功です。

### 停止方法
   タスクマネージャーから pythonw.exe を右クリックし、「タスクの終了」で停止できます。
