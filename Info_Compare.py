from Infogen import get_info
import pickle
import os
def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize/float(1024 * 1024 * 1024)
    return round(fsize, 8)

def load_and_get_info(source_url): #从文件中读取旧的info信息，从url中获取新的信息
    with open(info_url,"rb") as f:
        old_dirs_info , old_files_info = pickle.load(f)
    dirs_info , files_info = get_info(source_url)
    return [(old_dirs_info,old_files_info),
            (dirs_info,files_info)]

def info_Compare(info_list): #得到差集
    old_dirs_info , old_files_info = info_list[0]
    dirs_info ,     files_info     = info_list[1]
    same_dirs= list(set(old_dirs_info).intersection(set(dirs_info)))
    same_files=list(set(old_files_info).intersection(set(files_info)))
    diff_old_dirs =[i for i in old_dirs_info if i not in same_dirs]
    diff_new_dirs =[i for i in dirs_info if i not in same_dirs]
    diff_old_files=[i for i in old_files_info if i not in same_files]
    diff_new_files=[i for i in files_info if i not in same_files]
    return [diff_old_dirs,    #旧的文件夹与公共部分的不同
            diff_new_dirs,    #新的文件夹与公共部分的不同
            diff_old_files,   #旧的文件与公共部分的不同
            diff_new_files]   #新的文件与公共部分的不同

def prepare_action(diff_info):
    diff_old_dirs,diff_new_dirs,diff_old_files,diff_new_files=diff_info
    action=[]
    copysize=0
    for dir_ in diff_old_dirs: #文件夹删除
        dir_path,_=dir_
        if not ( dir_ in diff_new_dirs):
            action.append((dir_path,"deldir"))

    for dir_ in diff_new_dirs: #文件夹新建
        dir_path,_=dir_
        if not ( dir_ in diff_old_dirs):
            action.append((dir_path,"mkdir"))

    for file_ in diff_old_files:
        file_path,_=file_
        action.append((file_path,'del'))

    for file_ in diff_new_files:
        file_path,_=file_
        action.append((file_path,"update"))
        copysize+=get_FileSize(file_path)
    return [action,copysize]

if __name__ == "__main__":
    source_url = input("请输入源目录路径：")
    info_url = input("请输入旧的info的路径:")
    old_and_new_info=load_and_get_info(source_url) #旧的和新的信息
    diff_info=info_Compare(old_and_new_info)
    action=prepare_action(diff_info)[0]
    copysize=prepare_action(diff_info)[1]
    with open("action",'wb') as f:
        pickle.dump(action,f)
    print(action)
    print("文件大小：%.3f GB"%(copysize))