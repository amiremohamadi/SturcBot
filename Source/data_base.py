# Database library
# Including some functions to use for managing my database
import redis

r =redis.StrictRedis(host='localhost', port=6379, db=0)

def add_user(chat_id ,username, password):
  user = {"username":username, "password":password}
  return r.hmset(chat_id, user)

def del_user(chat_id):
  r.delete(chat_id)

def get_user(chat_id, what):
  # what : what to get
  if what == 'state':
    return r.hgetall(chat_id)
  else:
    return r.hget(chat_id, what)
