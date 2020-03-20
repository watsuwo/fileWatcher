# -*- coding: utf-8 -*-

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import os
import glob
import time
import fnmatch
import hashlib

TARGET = "/home/wataru/workspace/fileWatcher/logs"
hashes = {}

class ChangeHandler(FileSystemEventHandler):

    def on_created(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        if fnmatch.fnmatch(filename, '*.txt'):
            print("%sが作成された" %filename)

    def on_modified(self, event):
        if event.is_directory:
            pass
        else:
            filepath = event.src_path
            filename = os.path.basename(filepath)
            with open(filepath, 'rb') as f:
                check = hashlib.md5(f.read()).hexdigest()
            if filename not in hashes or (hashes[filename] != check) and fnmatch.fnmatch(filename, '*.txt'):
                hashes[filename] = check
                print("%sが変更された" %filename)

def main():
    while 1:
        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler, TARGET, recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(10)
        except KeyboardInterrupt:
            observer.stop()
            observer.join()

if __name__ == '__main__':
    main()