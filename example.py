from crypt.crypt import Cipher
from faces import new_tab, old_tab

def read_old_faces_example(cipher: Cipher):
    with open(r'encrypt_data/old_tab_face.txt') as f:
        data = cipher.decrypt(f.read())
        result = old_tab.get_all_ids(data)
        return result


def read_new_faces_example(cipher: Cipher):
    with open(r'encrypt_data/new_tabs_face.txt') as f:
        new_data = cipher.decrypt(f.read())
        result = new_tab.deserialize_tabs(new_data)
        raw_data = new_tab.serialize_to_dict_list(result)
        encrypted_text = cipher.encrypt(raw_data)
        return result, encrypted_text


if __name__ == '__main__':
    read_new_faces_example(Cipher('aaaaaaaaaaaaaaaaa'))
    pass
