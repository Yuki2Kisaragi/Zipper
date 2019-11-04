import os
import datetime
import shutil
Input_path = "PATH"
Output_path = "PATH2"


def archive_main():
    os.chdir(Input_path)
    CONTENTS = os.path.isfile(".") or os.path.isdir(".")
    print(CONTENTS)
    if CONTENTS:
        Whole_dir_to_archive()
        Under_directory_remove()
    else:
        print("No exists")


def Whole_dir_to_archive():
    """
    アーカイブファイル名を作成。
    Generate archive file name (full path).
    ex) Zipfile_name = 191104_1307

    shutil.make_archive()
        Directory全体を圧縮ファイルにします
        arg1:Potential arguments. filename ,path
        arg2:Potential arguments. You can select archive format. ex)zip, tar, gztar, bztar , xztar
        arg3:root_dir. Keyword arguments. default= '.'
        arg4:base_dir. Keyword arguments. default= '.' if you don't input base_dir, Whole folder (root_dir) is archived.
    :return: None
    """
    Zipfile_name = Output_path + "\\" + datetime.datetime.now().strftime("%y%m%d_%H%M")
    # print(Zipfile_name)
    shutil.make_archive(Zipfile_name, "zip", root_dir=Input_path)
    print("Archive Complete")


def Under_directory_remove():
    """
    Under the Directory (Input_path) file remove
    :return: None
    """
    shutil.rmtree(".")
    os.mkdir(Input_path)
    print("Remove Complete")


archive_main()
