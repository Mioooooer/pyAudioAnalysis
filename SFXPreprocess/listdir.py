import os


def listdir(path):#获取目录下的文件列表
    dirlist = []
    file_list=os.listdir(path)
    # print(file_list)
    global file_count, folder_count
    #遍历文件列表，如果当前文件不是文件夹，则文件数量+1，如果是文件夹，则文件夹数量+1且再调用统计文件个数的方法
    for temp in file_list:
        #path_now = path + "\\" + temp
        path_now = os.path.join(path, temp)
        if os.path.isdir(path_now)==True:
            dirlist.append(path_now)
    return dirlist



print(listdir('../../SFXClassified/'))

