# # 获取一个大的文件夹，进入到其中的每个小文件夹中
# root="/Users/xiongjiangkai/Downloads/algorithm_zuo"
# import os
# import shutil
# import re

# #依次进入到每个子文件夹中
# def enter_dir():
#     for root1,dirs,files in os.walk(root):
#         for dir in dirs:
#             os.chdir(root1+"/"+dir)
#             # 进入到一个文件夹中，按照文件名的原本顺序，将文件名改为1,2,3,4,5,6,7,8,9,10
#             # 1.获取文件名
#             file_names=os.listdir()
#             # 2.对文件名进行排序
#             file_names.sort(key=lambda x:x.split(".")[0])
#             # 只对后缀是.pptx的文件进行改名
#             for i in range(len(file_names)):
#                 if file_names[i].split(".")[1]=="pptx":
#                     # 3.将文件名改为1,2,3,4,5,6,7,8,9,10
#                     os.rename(file_names[i],str(i+1)+".pptx")

# enter_dir()
# import subprocess
# # AppleScript 文件的路径
# applescript_file_path = "/Users/xiongjiangkai/xjk_coding/a.applescript"

# # 使用 osascript 运行 AppleScript 文件
# subprocess.run(["osascript", applescript_file_path], capture_output=True, text=True)


import subprocess
import time
#给定最大的文件夹
root="/Users/xiongjiangkai/Downloads/algorithm_zuo"
# 要执行的 AppleScript 文件路径
applescript_file_path = "/Users/xiongjiangkai/xjk_coding/a.applescript"
#给定一个文件夹，进入到其中的每个子文件夹中，在每个子文件夹中将所有.pptx后缀的文件发给在applescript_file_path中
import os
for root1,dirs,files in os.walk(root):
    for dir in dirs:
        os.chdir(root1+"/"+dir)
        # 1.获取文件名
        file_names=os.listdir()
        file_names=[i for i in file_names if i.split(".")[1]=="pptx"]
        file_names.sort(key=lambda x:int(x.split(".")[0]))
        file_paths=[os.getcwd()+"/"+file_name for file_name in file_names if file_name.split(".")[1]=="pptx"]
        # 使用 subprocess 执行 AppleScript 文件，一次性传递所有文件路径
        process = subprocess.Popen(["osascript", applescript_file_path] + file_paths, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        
        # # 使用 subprocess 执行 AppleScript 文件，传递文件路径参数
        # for file_path in file_paths:
        #     # 必须要等待这个subprocess执行完成才能执行下一个,否则会出现bug
        #     # process = subprocess.run(["osascript", applescript_file_path, file_path], capture_output=True, text=True)
        #     process = subprocess.Popen(["osascript", applescript_file_path, file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        #     process.wait()






