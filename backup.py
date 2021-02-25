import pickle
import os
import shutil


def do(_action_):
    global del_actions
    target, mode = _action_
    if os.path.isdir(os.path.join(url_backup_from, target)):  # 文件夹操作
        if mode == "deldir":
            del_actions.append(_action_)
        elif mode == "mkdir":
            os.mkdir(os.path.join(url_backup_to, target))
    else:  # 文件操作
        if mode == "del":
            del_actions.append(_action_)
        elif mode == "update":
            shutil.copy2(os.path.join(url_backup_from, target), os.path.join(url_backup_to, target))
    return del_actions


if __name__ == "__main__":
    url_backup_from: str = input("备份自：")
    url_backup_to: str = input("备份至：")
    if not url_backup_from.endswith('\\'):
        url_backup_from += "\\"
    if not url_backup_to.endswith('\\'):
        url_backup_to += "\\"
    del_actions = []
    with open("action", 'rb') as f:
        actions = pickle.load(f)
    for action in actions:
        print(action)
        del_actions = do(action)
    with open(os.path.join(url_backup_to, ".del_actions"), 'wb') as f:  # 删除动作记录
        pickle.dump(del_actions, f)
    # print(del_actions)
