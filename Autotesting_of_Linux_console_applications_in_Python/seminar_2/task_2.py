"""
Установить пакет для расчёта crc32
sudo apt install libarchive-zip-perl
• Доработать проект, добавив тест команды расчёта хеша (h). 
Проверить, что хеш совпадает с рассчитанным командой crc32
"""

import subprocess
from checker import check_output
from checkout import checkout_positive

folder_in = "/home/user/tst/file"
folder_out = "/home/user/tst/out"
folder_ext = "/home/user/tst/ext"


def crc32(filename:str) -> str:
    output = subprocess.check_output("crc32 {}".format(filename), shell=True)
    return output.strip().decode('utf-8')


def test_step1(make_folders, clear_folders, make_files):
    res1 = checkout_positive("cd {}; 7z a {}/arx1.7z".format(folder_in, folder_out), "Everything is Ok"), "Test1 Fail"
    res2 = checkout_positive("ls {}".format(folder_out), "arx.7z"), "Test1 Fail"
    assert res1 and res2, "Test Fail"


def test_step2(clear_folders, make_files):
    res = []
    res.append(checkout_positive("cd {}; 7z a {}/arx1.7z".format(folder_in, folder_out), "Everything is Ok"))
    res.append(checkout_positive("cd {}; 7z e arx1.7z -o{} -y".format(folder_out, folder_ext), "Everything is Ok"))
    for item in make_files:
        res.append(checkout_positive("ls {}".format(folder_ext), ""))
    assert all(res)


def test_step3():
    assert checkout_positive("cd {}; 7z t {}/arx1.7z".format(folder_in, folder_out), "Everything is Ok"), "Test1 Fail"


def test_step4(make_folders, clear_folders, make_files):
    assert checkout_positive("cd {}; 7z u {}/arx1.7z".format(folder_in, folder_out), "Everything is Ok"), "Test1 Fail"


# Д/з:
def test_step5(make_folders, clear_folders, make_files):
    res = []
    res.append(checkout_positive("cd {}; 7z l arx1.7z".format(folder_out), ""))
    for item in make_files:
        file_in_crc32 = crc32("{}/{}".format(folder_in, item))
        file_out_crc32 = crc32("{}/{}".format(folder_out, item))
        res.append(check_output("{}: {} = {}".format(folder_out, file_in_crc32, file_out_crc32)))
    assert all(res), "Test Fail"


# Д/з:
def test_step6(make_folders, clear_folders, make_files):
    res = []
    res.append(checkout_positive("cd {}; 7z x arx1.7z -o{} -y".format(folder_out, folder_ext), "Everything is Ok"))
    for item in make_files:
        file_in_crc32 = crc32("{}/{}".format(folder_in, item))
        file_ext_crc32 = crc32("{}/{}".format(folder_ext, item))
        res.append(check_output("{}: {} = {}".format(folder_ext, file_in_crc32, file_ext_crc32)))
    assert all(res), "Test Fail"

if __name__ == "__main__":
    test_step1()
    test_step2()
    test_step3()
    test_step4()
    test_step5()
    test_step6()
    print("Все тесты успешно пройдены!")
