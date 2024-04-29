import os
import time
from client import send_request, get_content

"""
TODO: Finish this with proper testing.
"""

def watch_file(file_path):
    if not os.path.exists(file_path):
        print("File not found:", file_path)
        return

    last_modified = os.path.getmtime(file_path)
    print(f"Watching {file_path} for changes...")

    try:
        while True:
            current_modified = os.path.getmtime(file_path)
            
            if current_modified != last_modified:
                print(f"{file_path} has been updated.")
                try:
                    send_request(get_content(file_path))
                except Exception as e:
                    print("Error:", e)
                last_modified = current_modified
            
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped watching.")

watch_file('example.txt')
