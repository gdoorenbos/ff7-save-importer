from ff7_gen_cksum import calc_cksum, _save_filename
from ff7_get_user_id import get_user_id, _ff7_steam_dir
import shutil
import re

_metadata_filename = "metadata.xml"

class FF7SaveUpdater(object):
    def __init__(self):
        user_id = get_user_id()
        self.user_dir = _ff7_steam_dir + "/user_" + user_id
        self.user_metadata = self.user_dir + "/" + _metadata_filename
        self.user_save = self.user_dir + "/" + _save_filename

    def backup_metadata_file(self):
        backup_metadata = _metadata_filename + ".bak"
        shutil.copyfile(self.user_metadata, backup_metadata)

    def update_metadata_file(self):
        updated_metadata = []
        with open(self.user_metadata, "r") as metadata_file:
            sig_replaced = False
            for line in metadata_file:
                if not sig_replaced:
                    if (re.findall(r"^    <signature>\w+</signature>$", line)):
                        line = "    <signature>" + calc_cksum() + "</signature>\n"
                        sig_replaced = True
                updated_metadata.append(line)

        with open(self.user_metadata, "w") as metadata_file:
            metadata_file.write(''.join(updated_metadata))

    def backup_save_file(self):
        backup_save = _save_filename + ".bak"
        shutil.copyfile(self.user_save, backup_save)

    def update_save_file(self):
        shutil.copyfile(_save_filename, self.user_save)

def main():
    save_updater = FF7SaveUpdater()
    save_updater.backup_metadata_file()
    save_updater.update_metadata_file()
    save_updater.backup_save_file()
    save_updater.update_save_file()

if __name__ == '__main__':
    main()