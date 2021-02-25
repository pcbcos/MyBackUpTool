import os


def get_info(source_url):
    main_dir = os.walk(source_url)
    dirs_info = []
    files_info = []
    for root, dirs, files in main_dir:
        root_ = root.replace(source_url, "")
        for dir_ in dirs:
            t = os.path.getctime(os.path.join(root, dir_))
            dirs_info.append((os.path.join(root_, dir_), t))
        for file_ in files:
            files_info.append((os.path.join(root_, file_),
                               os.path.getmtime(os.path.join(root, file_))))
    return dirs_info, files_info
