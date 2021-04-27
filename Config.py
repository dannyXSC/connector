import time
import datetime
import os

class Config():
    def __init__(self):
        pass

    def write(self, path, config):
        if not isinstance(config, dict):
            raise Exception("Invalid input!")
        try:
            config_path=path+'/config.txt'
            if not os.path.exists(config_path):
                with open(config_path,'w') as _:
                    pass
            with open(config_path, 'a') as f:
                f.write(f"{config['Name']} {config['Ip']} {config['Port']} {config['Path']}\n")
        except:
            raise Exception("Write config failure!")

    def read(self,path):
        try:
            config_path=path+'/config.txt'
            if not os.path.exists(config_path):
                return None
            else:
                ret=list()
                with open(config_path,'r') as f:
                    lines=f.readlines()
                    for line in lines:
                        line=line.split()
                        ret.append({'Name':line[0],'Ip':line[1],'Port':int(line[2]),'Path':line[3]})
                return ret
        except:
            raise Exception("Read config failure!")

if __name__=='__main__':
    cfg=Config()
    path=r'D:\Project\connector\test\repetory'
    info={'Name':'123','Ip':'321','Port':456,'Path':'654'}
    cfg.write(path,info)
    info=cfg.read(path)
    print(info)