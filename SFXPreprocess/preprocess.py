import os
import shutil


def moveall(src_dir):#e.g: src_dir=E:\pythoncode\copytool\Android
    tempname = ''
    for root , dirs, files in os.walk(src_dir):
        #file =os.path.splitext(files)
        for name in files:
            if name.endswith('.wav'):
                if not compareFilteredName(name[:-4],tempname):
                    tempname = FilterName(name[:-4])
                #targetpath = '../../SFXClassified/'+tempname
                targetpath = os.path.join('../../SFXClassified', tempname)
                for i in range(5):
                    if targetpath.endswith(' '):
                        targetpath = targetpath[:-1]
                    if targetpath.endswith('.'):
                        targetpath = targetpath[:-1]
                if not os.path.exists(targetpath):
                    os.makedirs(targetpath)
                if not os.path.exists(os.path.join(targetpath,name)):
                    shutil.move(os.path.join(root,name),targetpath)
                print(os.path.join(root,name)+' -> '+targetpath)
            #if name[:-4].endswith("idcardimage"):
            '''
                if root==src_dir:
                    if os.path.exists(os.path.join(dest_dir, name)):
                        if not cmp_file(os.path.join(root, name),os.path.join(dest_dir, name)):
                            nums +=1
                            shutil.copy2(os.path.join(root, name), os.path.join(dest_dir, name))
                            print(os.path.join(root, name)+' -> '+os.path.join(dest_dir, name))
                    else:
                        if not os.path.exists(dest_dir):
                            os.makedirs(dest_dir)
                        nums +=1
                        shutil.copy2(os.path.join(root, name), os.path.join(dest_dir, name))
                        print(os.path.join(root, name)+' -> '+os.path.join(dest_dir, name))
            '''
def compareFilteredName(str1, str2):
    newstr1 = ''.join([i for i in str1 if not i.isdigit()])
    newstr2 = ''.join([i for i in str2 if not i.isdigit()])
    return newstr1 == newstr2

def FilterName(str):
    newstr = ''.join([i for i in str if not i.isdigit()])
    return newstr


moveall('G:\SFXRepo')