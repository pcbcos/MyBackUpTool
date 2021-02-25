import os
import pickle
def main():
    source_url = input("请输入要建立list的文件夹路径：")
    main_dir = os.walk(source_url)
    dirs_info = []
    files_info = []
    for root, dirs, files in main_dir:
        for dir_ in dirs:
            t = os.path.getctime(os.path.join(root, dir_))
            dirs_info.append((os.path.join(root, dir_), t))
        for file_ in files:
            files_info.append((os.path.join(root, file_),
                               os.path.getmtime(os.path.join(root, file_))))
    with open("info",'wb') as f:
        pickle.dump((dirs_info,files_info),f)
if __name__ == "__main__":
    main()
