import pytest
from sshcheckers import ssh_checkout

folder_out = "/home/user/tst/badarx"
folder_ext = "/home/user/tst/ext"

host = "your_host"
user = "your_user"
passwd = "your_password"
port = 22


def test_step1():
    # test1
    cmd = "cd {}; 7z e badarx.7z -o{} -y".format(folder_out, folder_ext)
    text = "ERROR"
    assert ssh_checkout(host, user, passwd, cmd, text, port), "Test4 Fail"


def test_step2():
    # test2
    cmd = "cd {}; 7z t badarx.7z".format(folder_out)
    text = "ERROR"
    assert ssh_checkout(host, user, passwd, cmd, text, port), "Test5 Fail"


if __name__ == '__main__':
    pytest.main()