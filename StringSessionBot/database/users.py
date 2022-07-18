from . import db

usersdb = db.users

async def add(a: int):
    ok = usersdb.find_one({"a": a})
    if ok:
        return
    await usersdb.insert_one({"a": a})

async def users():
    users = usersdb.find({"a": {"$gt": 0}})
    if not users:
        return []
    users_list = []
    for user in await users.to_list(length=1000000000):
        users_list.append(user)
    return users_list
