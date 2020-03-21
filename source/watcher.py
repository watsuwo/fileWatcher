# -*- coding: utf-8 -*-

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from email.mime.text import MIMEText

import smtplib
import os
import glob
import time
import fnmatch
import hashlib
import change_getter
import mailer

TARGET = "/home/wataru/workspace/fileWatcher/logs"
ERROR_MESSAGE = "NG"
hash_value = {}

class ChangeHandler(FileSystemEventHandler):

    def on_created(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        if fnmatch.fnmatch(filename, '*.txt'):
            print("%s is created" %filename)

    def on_modified(self, event):
        if event.is_directory:
            pass
        else:
            filepath = event.src_path
            filename = os.path.basename(filepath)
            
            with open(filepath, 'rb') as f:
                check = hashlib.md5(f.read()).hexdigest()

            if filename not in hash_value or (hash_value[filename] != check) and fnmatch.fnmatch(filename, '*.txt'):
                hash_value[filename] = check
                getter = change_getter.Getter(filepath)
                changes = getter.get_change()

                if ERROR_MESSAGE in changes:
                    mailer.send_mail()
                else:
                    pass
            else:
                pass

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