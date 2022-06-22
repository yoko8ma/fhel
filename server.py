USE_REAL_SERVER: bool = True

print(f"[Client] launching server (could be launched sparately)...")
if(USE_REAL_SERVER):
  import subprocess, os
  from pathlib import Path
  dir = Path(os.path.realpath("__file__")).parent
  process = subprocess.Popen(
    ["python", str(dir / "Demo_5bis_CS_Server.py")],
    stderr=subprocess.STDOUT,
  )
  import time
  time.sleep(6)  # Wait for server initialization
else:
  print(f"[Server] mock stated...")
print("[Client] server initialized...")
