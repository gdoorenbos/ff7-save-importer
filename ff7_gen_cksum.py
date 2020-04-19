from ff7_get_user_id import get_user_id
import hashlib

_save_filename = 'save00.ff7'

def calc_cksum():
    userid = get_user_id()
    save_contents = open(_save_filename, 'rb').read()
    return hashlib.md5(save_contents + userid.encode('utf-8')).hexdigest()

if __name__ == '__main__':
    print(calc_cksum())