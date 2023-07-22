import os
import time
import shutil
from c_odf import cleanup_old_files

# 你的 cleanup_old_files 函数应该在这里

def create_test_file(path, days_old):
    with open(path, "w") as f:
        f.write("Test")

    old_time = time.time() - days_old * 86400
    os.utime(path, (old_time, old_time))

def test_cleanup_old_files():
    test_folder = "test_folder"
    os.mkdir(test_folder)

    create_test_file(os.path.join(test_folder, "new_file.txt"), days_old=0)
    create_test_file(os.path.join(test_folder, "old_file.txt"), days_old=31)
    print("已创建完成测试文件")

    cleanup_old_files("E:/code/python/little_project/tidydownload/"+"test_folder", days=30)

    remaining_files = os.listdir(test_folder)
    assert len(remaining_files) == 1
    assert "new_file.txt" in remaining_files

    shutil.rmtree(test_folder)

    print("测试通过")

test_cleanup_old_files()
