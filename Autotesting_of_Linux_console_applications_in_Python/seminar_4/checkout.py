import subprocess
from sshcheckers import ssh_checkout


def checkout_positive_ssh(command, expected_output):
    output = ssh_checkout(command)
    return expected_output in output

def checkout_positive(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    if result.returncode == 0 and text in result.stdout:
        return True
    else:
        return False


def checkout_negative(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    if result.returncode != 0 and (text in result.stderr or text in result.stdout):
        return True
    else:
        return False
