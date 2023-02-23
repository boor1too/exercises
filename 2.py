import re

def replace_email_domains(text):
    pattern_mailru = r'(?<=\b[\w.-]+@)mail\.ru\b'
    replaced_text = re.sub(pattern_mailru, 'gmail.com', text)

    pattern_yahoo = r'(?<=\b[\w.-]+@)yahoo\.com\b'
    replaced_text = re.sub(pattern_yahoo, 'outlook.com', replaced_text)

    pattern_bkru = r'(?<=\b[\w.-]+@)bk\.ru\b'
    replaced_text = re.sub(pattern_bkru, 'kbtu.kz', replaced_text)

    return replaced_text

text = "My email is john.doe@mail.ru and my friend's email is jane.smith@yahoo.com, Also here is another: another@bk.ru"
replaced_text = replace_email_domains(text)
print(replaced_text)