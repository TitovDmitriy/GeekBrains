import random
import string
import subprocess
import pytest
from checkout import checkout_positive

folder_in = "/home/user/tst/file"
folder_out = "/home/user/tst/out"
folder_ext = "/home/user/tst/ext"
folder_badarx = "/home/user/tst/badarx"


@pytest.fixture()
def make_folders():
    return checkout_positive("mkdir {} {} {} {}".format(folder_in, folder_out, folder_ext, folder_badarx), "")


@pytest.fixture()
def clear_folders():
    return checkout_positive("rm -rf {}/* {}/* {}/* {}/*".format(folder_in, folder_out, folder_ext, folder_badarx), "")


@pytest.fixture()
def make_files():
    list_off_files = []
    for i in range(5):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout_positive(
                "cd {}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(folder_in, filename),
                ""):
            list_off_files.append(filename)
    return list_off_files


@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not checkout_positive("cd {}; mkdir {}".format(folder_in, subfoldername), ""):
        return None, None
    if not checkout_positive(
            "cd {}/{}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(folder_in, subfoldername,
                                                                                      testfilename), ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename
