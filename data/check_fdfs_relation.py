import os
import sys

sys.path.append("/devops/script/base/")
sys.path.append("/devops/script/comm/")

import base_util
FDFS_CONF_PATH = '/home/faier/etc/fdfs/'
FDFS_SHELL_PATH = '/home/faier/bin/'
FDFS_DAT_PATH = '/dat/fdfs/'


def check(storage_path):
    check_fdfs_alive_cmd = "ps -ef | grep fdfs_storaged | grep -E storage-?%s.conf | grep -v grep | wc -l" % storage_path
    suc, res = base_util.linuxShell(check_fdfs_alive_cmd)
    if suc and int(res) == 1:
        return True

    print(check_fdfs_alive_cmd + " " + str(suc) + " " + res)
    return False

def main():
    for file in os.listdir(FDFS_CONF_PATH):
        if file.startswith("storage") and file != "storage-template.conf" and file != "storage_ids.conf.sample" and file != "storage.conf.sample":
            if file.startswith("storage-"):
                storage_path = file[8:-5]
            else:
                storage_path = file[7:-5]
            if not check(storage_path):
               print(file)

    for file in os.listdir(FDFS_SHELL_PATH):
        if file.startswith("fastdfs-storage") and file != "fastdfs-storage-template.sh" and file != "fastdfs-storage.sh.template":
            if file.startswith("fastdfs-storage-"):
                storage_path = file[16:-3]
            else:
                storage_path = file[15:-3]

            if not check(storage_path):
                print(file)

    for file in os.listdir(FDFS_DAT_PATH):
        if not check(file):
            print(file)

if __name__ == '__main__':
    main()