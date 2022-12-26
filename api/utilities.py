from cryptography.fernet import Fernet

from environment_variables import default_encryption_key


def encrypt_sting(string, key=None):
    """
    :param string:
    :param key:
    :return:
    """

    if len(string) < 100:

        if not key:
            key = default_encryption_key

        if key:
            enc = Fernet(key)
            encrypted_string = enc.encrypt(string.encode())
            return encrypted_string.decode()

        else:
            return False

    else:
        return string


def decrypt_string(encrypted_string, key=None):
    """
    :param encrypted_string:
    :param key:
    :return:
    """

    if not key:
        key = default_encryption_key

    if key:
        enc = Fernet(key)
        try:
            decrypted_string = enc.decrypt(encrypted_string.encode('utf-8'))
            return decrypted_string.decode()

        except:
            return False
    else:
        return False