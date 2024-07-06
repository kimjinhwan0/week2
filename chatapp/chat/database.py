from django.conf import settings

def get_database():
    return settings.MONGODB_DB

def insert_person(user_id, user_pwd):
    db = get_database() # 'Cluster0'이라는 db를 가져옴.
    message_collection = db['auth_user'] # 그 중 'auth_user'라는 표 가져옴.
    message = {
        'user_id': user_id,
        'user_pwd': user_pwd,
    } # message 타입 저장
    result = message_collection.insert_one(message) # insert하기
    return result.inserted_id