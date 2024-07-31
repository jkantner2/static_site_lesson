import os
import shutil


def copy_static(path):
    if os.path.exists("/Users/james/bootdevLessons/static_site_lesson/public"):
        shutil.rmtree("/Users/james/bootdevLessons/static_site_lesson/public")

    if not os.path.exists(path):
        raise OSError("No such file or directory")
    
    if not os.path.exists("/Users/james/bootdevLessons/static_site_lesson/public"):
        os.mkdir("/Users/james/bootdevLessons/static_site_lesson/public")
    
    copy_files_directories(path)


def copy_files_directories(path):
    dir_contents = os.listdir(path)
    public_base_path = "/Users/james/bootdevLessons/static_site_lesson/public"
    path_list = []
    for item in dir_contents:
        static_path = os.path.join(path, item)
        tmp = static_path.split("static_site_lesson/static")
        public_path = public_base_path + tmp[1]
        if os.path.isdir(static_path):
            if not os.path.exists(public_path):
                os.mkdir(public_path)
            path_list.append(public_path)
            copy_files_directories(static_path)
        if os.path.isfile(static_path):
            path_list.append(static_path)
            shutil.copy(static_path, public_path)


if __name__ == '__main__':
    copy_static()
