import psutil
from pypresence import Presence
import time

client_id = "Discord Developerに追加したApplication ID"
RPC = Presence(client_id)
RPC.connect()

try:
    while True:
        running = any(p.name() == "Affinity.exe" for p in psutil.process_iter())

        if running:
            RPC.update(details="Editing...", large_image="Affinity_Logo", large_text="Affinity Logo")
        else:
            RPC.clear()

        time.sleep(15)
except KeyboardInterrupt:
    RPC.close()