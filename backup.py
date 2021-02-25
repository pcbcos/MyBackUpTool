import pickle
import os
import shutil
def do(action):
    global del_actions
    target,mode=action
    if os.path.isdir(target):   #文件夹操作
        if mode=="deldir":
            del_actions.append(action)
        elif mode=="mkdir":
            os.mkdir(target.replace(url_backup_from,url_backup_to))
    else:                      #文件操作
        if mode=="del":
            del_actions.append(action)
        elif mode=="update":
            shutil.copy2(target,target.replace(url_backup_from,url_backup_to))
    return del_actions
if __name__=="__main__":
    url_backup_from=input("备份自：")
    url_backup_to=input("备份至：")
    del_actions=[]
    with open("action",'rb') as f:
        actions=pickle.load(f)
    for action in actions:
        print(action)
        del_actions=do(action)
    with open(os.path.join(url_backup_to,".del_actions"),'wb') as f:   #删除动作记录
        pickle.dump(del_actions,f)
    #print(del_actions)