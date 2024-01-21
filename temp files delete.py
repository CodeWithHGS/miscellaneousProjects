import os
import shutil

prefetch="C://Windows//prefetch"
temp2="C://Users//HS//AppData//Local//Temp"
temp="C://Windows//Temp"
def delete_temp_files(path):
    files=os.listdir(path)
    for i in files:
        try:
            if os.path.isdir(path+"//"+i)==True:
                shutil.rmtree(path+"//"+i)
            else:
                os.remove(path+"//"+i)
                print(path+"//"+i)
        except:
            continue
delete_temp_files(prefetch)
delete_temp_files(temp)
delete_temp_files(temp2)

delete_temp_files(prefetch)
delete_temp_files(temp)
delete_temp_files(temp2)

delete_temp_files(prefetch)
delete_temp_files(temp)
delete_temp_files(temp2)
