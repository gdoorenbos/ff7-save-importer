import os
import re

_ff7_steam_dir = "~/Documents/Square Enix/Final Fantasy VII Steam"

def get_user_id():
    user_regex = r'^user_(\d+)$'
    steam_dir_children = os.listdir(os.path.expanduser(_ff7_steam_dir))
    [[user_id]] = [re.findall(user_regex, child) for child in steam_dir_children if re.findall(user_regex, child)]
    return user_id

def main():
    user_id = get_user_id()
    print(user_id)

if __name__ == '__main__':
    main()