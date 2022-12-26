import logging
import traceback

from api.user_management.utils import user_registration, user_login_email, brand_register, brands_listing
from constants import exception_msg
from api.utilities import encrypt_sting


def add_company_user(db, email, password):
    """
    :param db:
    :param email:
    :param password:
    :return:
    """
    try:
        password_encrypt = encrypt_sting(string=password)
        message, status_code = user_registration(db=db, email=email, password_encrypt=password_encrypt)

    except Exception as exc:
        db.rollback()
        logging.exception(str(exc))
        traceback.print_exc()
        message = exception_msg
        status_code = 400
    return message, status_code


def company_user_login(db, email, password):
    """
    :param db:
    :param email:
    :param password:
    :return:
    """
    try:

        message, status_code, user_data = user_login_email(db=db, email=email, password=password)

    except Exception as exc:
        logging.exception(str(exc))
        traceback.print_exc()
        user_data = []
        message = exception_msg
        status_code = 400
    return message, status_code, user_data


def add_brand(db, brand_competitor_hashtag_keywords, email):
    """
    This function used for create brand
    :param db:
    :param brand_competitor_hashtag_keywords:
    :return:
    """
    try:
        brand_name, competitor_name, hashtag = brand_competitor_hashtag_keywords.split(', ')
        message, status_code = brand_register(db=db, brand_name=brand_name, competitor_name=competitor_name,
                                              hashtag=hashtag, email=email)

    except Exception as exc:
        logging.exception(str(exc))
        traceback.print_exc()
        message = exception_msg
        status_code = 400
    return message, status_code


def fetch_brands_listing(db, account_type, email):
    """
    This function used for get brands listing
    :param db:
    :param account_type:
    :return:
    """
    try:
        message, status_code, data = brands_listing(db, account_type, email=email)
    except Exception as exc:
        logging.exception(str(exc))
        traceback.print_exc()
        message = exception_msg
        status_code = 400
        data = []
    return message, status_code, data
