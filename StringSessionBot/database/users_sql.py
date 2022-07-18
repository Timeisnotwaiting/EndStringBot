from sqlalchemy import Column, Integer
from StringSessionBot.database import BASE, SESSION


class Users(BASE):
    __tablename__ = "users"
   
    user_id = Column(Integer, primary_key=True)

    def __init__(self, user_id):
        self.user_id = user_id
       

Users.__table__.create(checkfirst=True)


async def num_users():
    ok = SESSION.query(Users).all()
    OK = []
    for lel in ok:
        OK.append(lel.user_id)
    msg = ""
    for hm in ok:
        msg += f"<code>{hm}</code>\n"
    return msg, len(OK)
    
def add(a):
    lel = SESSION.query(Users).get(a)
    if not lel:
        SESSION.add(Users(a))
        SESSION.commit()
    else:
        SESSION.close()
