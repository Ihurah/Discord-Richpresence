import time
import win32gui
import win32process
import psutil
from pypresence import Presence, DiscordNotFound, InvalidPipe

CLIENT_ID = 'Discord Developer Portalで作成したアプリのApplication ID'
TARGET_PROCESS = 'アクティビティに表示したいソフト（拡張子付き）'
DETAILS = '表示するテキスト'

def get_active_process_name():
    try:
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        if pid == 0:
            return None
        process = psutil.Process(pid)
        return process.name()
    except:
        return None

def main():
    def connect_discord():
        while True:
            try:
                rpc = Presence(CLIENT_ID)
                rpc.connect()
                return rpc
            except (DiscordNotFound, InvalidPipe, FileNotFoundError):
                time.sleep(5)
            except Exception:
                time.sleep(10)

    RPC = connect_discord()
    start_time = None
    is_active_status = False

    while True:
        try:
            active_name = get_active_process_name()

            if active_name and active_name.lower() == TARGET_PROCESS.lower():
                
                if not is_active_status:
                    start_time = time.time()
                    RPC.update(
                        details=DETAILS,
                        start=start_time,
                        large_image="image_key"
                    )
                    is_active_status = True
            
            else:
                if is_active_status:
                    RPC.clear()
                    start_time = None
                    is_active_status = False

            time.sleep(5)

        except (DiscordNotFound, InvalidPipe):
            is_active_status = False
            start_time = None
            RPC = connect_discord()
        
        except Exception:
            time.sleep(5)

if __name__ == '__main__':

    main()
