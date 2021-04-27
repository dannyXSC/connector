import time
import datetime
import os

class Log():
    def __init__(self):
        pass

    def write(self, path, content):
        if not isinstance(content, str):
            raise Exception("Invalid input!")
        try:
            log_path=path+'/log.txt'
            '''
            if not os.path.exists(log_path):
                with open(log_path,'wb') as f:
                    pass 
                '''
            with open(log_path, 'a') as f:
                timeStruct = time.localtime(time.time())
                curTime = time.strftime('[%Y-%m-%d %H:%M:%S]', timeStruct)
                f.write(f"{curTime}\n")
                f.write(content+'\n')
            
        except:
            raise Exception("Write log failure!")
