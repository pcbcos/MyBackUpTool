# 自制增量备份工具

0   make_blank.py
    生成一份空的文件info，用于第一次增量备份（全量备份）
1   Infogen_sep.py
    输入备份源路径,生成一份包含所用文件夹和文件路径、时间信息的info,可用于每次备份完毕之后创建新的info
2   Info_Compare.py
    输入备份源路径，输入旧的info文件路径，自动生成（但不保存）新的info并与旧的info相比，生成action并给出需拷贝的文件的大小
3   backup.py
    输入备份源路径，输入备份文件存放的路径，自动执行操作，并留下.del_actions
4   recover.py (还没写)

使用顺序
0-->2-->3-->1-->(2-->check-->3-->check-->1)*N-->4
