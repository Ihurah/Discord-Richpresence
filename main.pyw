import sys
import traceback
print("main_resolve.pyw started", flush=True)
import psutil
from pypresence import Presence
import time


client_id = "Application ID"
RPC = Presence(client_id)
RPC.connect()

try:
    while True:
        running = any(p.name() == ".exe" for p in psutil.process_iter())

        if running:
            RPC.update(details="statusを入力", large_image="Discord Developer PortalでRich Presence AssetsにAddしたimage", large_text="任意のテキスト")
        else:
            RPC.clear()  

        time.sleep(15)
except KeyboardInterrupt:
    RPC.close()
except Exception:
    print("[ERROR]", file=sys.stderr)
    traceback.print_exc()
