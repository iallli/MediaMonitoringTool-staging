from datetime import datetime
from sqlalchemy import and_

from api.auth.auth_handler import access_token, refresh_token
from api.user_management.model import users, brands
from api.utilities import decrypt_string
from constants import success_msg, user_does_not_exist_msg, user_account_disabled_msg, incorrect_password_msg, \
    user_exist_msg


def user_registration(db, email, password_encrypt):
    """
    :param db:
    :param email:
    :param password_encrypt:
    :return:
    """
    user_exist = get_user_by_email(db=db, email=email)
    print("user_exist", user_exist)
    if user_exist:
        message = user_exist_msg
        status_code = 400
    else:

        user_obj = users(email=email, password=password_encrypt)
        db.add(user_obj)
        db.commit()

        message = success_msg
        status_code = 200

    return message, status_code


def update_last_login(db, email):
    """
    :param db:
    :param email:
    :return:
    """
    db.query(users).filter(users.email == email).update({
        "last_login": datetime.utcnow()
    }, synchronize_session=False)
    db.commit()


def get_user_by_email(db, email):
    """
    :param db:
    :param email:
    :return:
    """
    user_obj = db.query(users).filter(users.email == email).first()

    return user_obj


def get_user_login_details(db, user_obj):
    """
    :param user_obj:
    :return:
    """
    mentions_obj = db.query(brands).filter(brands.user_id == user_obj.id).first()
    if mentions_obj:
        flag = True
    else:
        flag = False
    user_data = dict()
    user_data['id'] = user_obj.id
    user_data['email'] = user_obj.email
    user_data['creation_at'] = user_obj.creation_at.strftime(
        '%Y-%m-%d %H:%M:%S')
    user_data['updated_at'] = user_obj.updated_at.strftime(
        '%Y-%m-%d %H:%M:%S') if user_obj.updated_at else None
    user_data['deleted_at'] = user_obj.deleted_at.strftime(
        '%Y-%m-%d %H:%M:%S') if user_obj.deleted_at else None
    user_data['last_login'] = user_obj.last_login.strftime(
        '%Y-%m-%d %H:%M:%S') if user_obj.last_login else None
    user_data['password'] = user_obj.password
    user_data['access_token'] = access_token(user_id=user_obj.id, user_email=user_obj.email)
    user_data['refresh_token'] = refresh_token(user_id=user_obj.id, user_email=user_obj.email)
    user_data['flag'] = flag

    return user_data


def user_login_email(db, email, password):
    """
    :param db:
    :param email:
    :param password:
    :return:
    """
    user_obj = get_user_by_email(db, email=email)
    if user_obj:
        if user_obj.deleted_at:
            message = user_account_disabled_msg
            status_code = 200
            user_data = []
        else:
            # check_password = password.encode('utf-8')
            # verify_password = bcrypt.checkpw(check_password, user_obj.password)
            # if verify_password:
            decrypt_password = decrypt_string(str(user_obj.password))

            if decrypt_password == password:
                update_last_login(db=db, email=email)
                user_data = get_user_login_details(db=db, user_obj=user_obj)
                message = success_msg
                status_code = 200

            else:
                message = incorrect_password_msg
                status_code = 200
                user_data = []

    else:
        message = user_does_not_exist_msg
        status_code = 200
        user_data = []

    return message, status_code, user_data


def brand_register(db, brand_name, competitor_name, hashtag, email):
    """
    :param db:
    :param brand_name:
    :param competitor_name:
    :param hashtag:
    :return:
    """
    user_obj = db.query(users).filter(users.email == email).first()
    if user_obj:
        brand_obj = brands(brand_name=brand_name, competitor_name=competitor_name, hashtag=hashtag, user_id=user_obj.id)

        db.add(brand_obj)
        db.commit()

        message = success_msg
        status_code = 200
    else:
        message = user_does_not_exist_msg
        status_code = 400
    return message, status_code


def brands_listing(db, account_type, email):
    """
    :param db:
    :param account_type:
    :return:
    """
    brand_listing = []
    user_obj = db.query(users).filter(users.email==email).first()
    brands_listing_obj = db.query(brands).filter(and_(brands.account_type == account_type,
                                                      brands.user_id == user_obj.id)).all()
    if brands_listing_obj:
        for brands_obj in brands_listing_obj:
            brands_listing_dict = dict()
            brands_listing_dict['id'] = brands_obj.id
            brands_listing_dict['brand_name'] = brands_obj.brand_name
            brands_listing_dict['competitor_name'] = brands_obj.competitor_name
            brands_listing_dict['hashtag'] = brands_obj.hashtag
            brands_listing_dict['creation_at'] = brands_obj.creation_at
            brands_listing_dict['updated_at'] = brands_obj.updated_at
            brands_listing_dict['deleted_at'] = brands_obj.deleted_at
            brands_listing_dict['account_type'] = brands_obj.account_type
            brand_listing.append(brands_listing_dict)

    message = success_msg
    status_code = 200

    return message, status_code, brand_listing
