import subprocess
import sys
import time

processes = []
try:
    print("=== 啟動微服務中 ===")
    
    # 啟動會員微服務 (Port 5001)
    print("啟動 會員微服務 (Port 5001)...")
    p1 = subprocess.Popen([sys.executable, "member_service/app.py"])
    processes.append(p1)
    
    # 啟動購票微服務 (Port 5002)
    print("啟動 購票微服務 (Port 5002)...")
    p2 = subprocess.Popen([sys.executable, "ticket_service/app.py"])
    processes.append(p2)
    
    # 啟動留言微服務 (Port 5003)
    print("啟動 留言微服務 (Port 5003)...")
    p3 = subprocess.Popen([sys.executable, "message_service/app.py"])
    processes.append(p3)
    
    print("\n所有服務已啟動。按下 Ctrl+C 可停止所有服務。\n")
    
    # 持續監控子程序
    while True:
        # 檢查是否有任何服務已自動結束 (例如留言服務 3 次後自動停機)
        for p in processes:
            if p.poll() is not None:
                # 服務已結束，不強制中斷其他服務，讓使用者自行觀察
                pass
        time.sleep(1)

except KeyboardInterrupt:
    print("\n正在停止所有微服務...")
finally:
    for p in processes:
        if p.poll() is None:
            p.terminate()
            p.wait()
    print("所有微服務已停止。")
