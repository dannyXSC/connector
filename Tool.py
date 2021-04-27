import os
import datetime
import time


class Tool():
    def __init__(self):
        pass

    def __getChildren(self, path):
        if not os.path.isdir(path):
            raise Exception(f"--{path}-- is not a folder!")
        try:
            ret = list()
            files = os.listdir(path)
            for file in files:
                file_Path = path+'/'+file
                if os.path.isdir(file_Path) and file[0] != '.':
                    curDict = {}
                    curChildren = self.__getChildren(file_Path)
                    curDict["Type"] = "folder"
                    curDict["Name"] = file
                    curDict["Children"] = curChildren
                    curDict["ModifyTime"] = self.__get_FileModifyTime(
                        file_Path)
                    ret.append(curDict)
                elif not os.path.isdir(file_Path) and file[0] != '.':
                    curDict = {}
                    curDict["Type"] = "file"
                    curDict["Name"] = file
                    curDict["Size"] = self.__get_FileSize(file_Path)
                    curDict["ModifyTime"] = self.__get_FileModifyTime(
                        file_Path)
                    with open(file_Path,'rb') as f:
                        curDict["Data"]=f.read()
                    ret.append(curDict)
            return ret
        except:
            raise Exception("Get children failure!")

    def __get_FileSize(self, path):
        return os.path.getsize(path)

    def __get_FileAccessTime(self, path):
        return os.path.getatime(path)

    def __get_FileModifyTime(self, path):
        return os.path.getmtime(path)

    def __get_FileCreateTime(self, path):
        return os.path.getctime(path)

    def __TimeStamp2Time(self, timestamp):
        if isinstance(timestamp, float):
            raise Exception("Timestamp format error!")
        timeStruct = time.localtime(timestamp)
        return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)

    def getTreeInfo(self, path):
        if not isinstance(path, str):
            raise Exception("Invalid input!")
        if not os.path.exists(path):
            raise Exception(f"Path --{path}-- is not exist!")
        try:
            if os.path.isdir(path):
                curDict = {}
                curDict["Type"] = "folder"
                curDict["Name"] = path[max(
                    path.rfind('/'), path.rfind('\\'))+1:]
                curDict["Children"] = self.__getChildren(path)
                curDict["ModifyTime"] = self.__get_FileModifyTime(path)
                return curDict
            else:
                curDict = {}
                curDict["Type"] = "file"
                curDict["Name"] = path[max(
                    path.rfind('/'), path.rfind('\\'))+1:]
                curDict["Size"] = self.__get_FileSize(path)
                curDict["ModifyTime"] = self.__get_FileModifyTime(path)
                with open(path,'rb') as f:
                    print(1)
                    curDict["Data"]=f.read()
                return curDict
        except:
            raise Exception("Get tree information failure!")

    def load(self, path, info_dict):
        if not isinstance(path, str) or not isinstance(info_dict, dict):
            raise Exception("Invalid input!")
        try:
            if info_dict["Type"] == "folder":
                curPath = path+'/'+info_dict["Name"]
                if not os.path.exists(curPath):
                    os.makedirs(curPath)
                for file in info_dict["Children"]:
                    self.load(curPath, file)
            elif info_dict["Type"] == "file":
                curPath = path+'/'+info_dict["Name"]
                if not os.path.exists(curPath) or self.__get_FileModifyTime(curPath) < info_dict["ModifyTime"]:
                    os.system("touch \"{}\"".format(curPath))
                    with open(curPath, 'wb') as f:
                        f.write(info_dict["Data"])
            else:
                raise Exception("Info_dict invalid!")
        except:
            raise Exception("Load failure!")


if __name__=="__main__":
    tool=Tool()
    info=tool.getTreeInfo(r'D:\Project\connector\test')
    print(info)