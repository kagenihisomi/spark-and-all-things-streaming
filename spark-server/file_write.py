import os
import shutil
import time

def write_to_file_continuously():
    content = "the quick brown fox jumps over the lazy dog"
    script_dir = os.path.dirname(__file__)  # <--- absolute dir the script is in
    for filename in os.listdir(script_dir + "/files"):
        file_path = os.path.join(script_dir + "/files", filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

    rel_path = "files/sample_{}.txt"
    while True:
        timestamp = int(time.time())
        abs_file_path = os.path.join(script_dir, rel_path.format(timestamp))
        with open(abs_file_path, "w") as file:
            file.write(content)
        time.sleep(5)
        
if __name__ == "__main__":
    write_to_file_continuously()
