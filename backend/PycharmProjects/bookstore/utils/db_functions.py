from utils.pure_db import execute, fetch


async def db_check_token_user(user):
    # query = """select * from users where username = :username and
    #                                      password = :password"""
    # values = {"username": user.username, "password": user.password}
    # result = await fetch(query, True, values)
    query = """select * from users where username = :username"""
    values = {"username": user.username}
    result = await fetch(query, False, values)
    if None is result:
        return None
    else:
        return result


async def db_check_jwt_username(username: str):
    query = """select * from users where username = :username"""
    values = {"username": username}

    result = await fetch(query, True, values)
    if None is result:
        return False
    else:
        return True


async def db_insert_personel(user):
    query = """insert into personel(username, password, mail, role)
            values(:name, :password, :mail, :role)"""
    values = dict(user)
    await execute(query, False, values)


async def db_check_personel(username, password):
    query = """select * from personel where username = :username
                                        and password = :password"""
    values = {"username": username, "password": password}
    result = await fetch(query, True, values)
    if None is result:
        return False
    else:
        return True


async def db_check_fake(isbn):
    query = """select * from book where isbn = :isbn"""
    values = {"isbn": isbn}
    result = await fetch(query, True, values)
    return result


async def db_get_book_with_isbn(isbn):
    query = """select * from book where isbn = :isbn"""
    values = {"isbn": isbn}
    result = await fetch(query, True, values)
    return result


async def db_get_author(input_val):
    query = """select * from authors where name = :name"""
    values = {"name": input_val}
    author = await fetch(query, True, values)
    return author


async def db_get_author_from_id(input_val):
    query = """select * from authors where id=:id"""
    values = {"id": input_val}
    result = await fetch(query, True, values)
    return result


async def db_patch_author_name(id, name):
    query = """update authors set name=:name where id=:id"""
    values = {"id": id, "name": name}
    await execute(query, False, values)

