import subprocess 


def check_output(command, text, mode='default'):
    try:
        output = subprocess.check_output(command, shell=True).decode()
        output_words = re.findall(r'\w+', output.lower())
        if mode == 'default':
            if text in output:
                return True
            else:
                return False
        elif mode == 'word':
            text_words = text.split()
            for word in text_words:
                word = word.lower()
                if word not in output_words:
                    return False
            return True
    except subprocess.CalledProcessError:
        return False