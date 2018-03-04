import time
import telepot
from telepot.loop import MessageLoop
from data_base import *
from panel import *

# Define bot with a token code
TOKEN = 'blah-blahblah'
TelegramBot = telepot.Bot(TOKEN)
# -----------------------------------------------------

def login(text, chat_id):
  # Extract username and password from message text
  # Username is first argumant and password is the second
  username = ' '.join(text.split()[1:2])
  password = ' '.join(text.split()[2:3])
  # First check if you enter your user and pass after /login or not
  if username.strip() and password.strip():
    # Then check if your data save on database
    if add_user(chat_id, username, password):
      TelegramBot.sendMessage(chat_id, 'با موفقیت انجام شد 🙂\nحالا میتونی ازم استفاده کنی!')

  else:
    TelegramBot.sendMessage(chat_id, 'اینجوری از دستور login استفاده کن:\n\n/login username password')


def show(chat_id):
  if get_user(chat_id, 'state'):

    msg_content = panel(get_session(get_user(chat_id, 'username'), get_user(chat_id, 'password')))
    TelegramBot.sendMessage(chat_id, msg_content[1].replace('خوش آمدید', 'اینم از وضعیت حضور غیابت '))
    TelegramBot.sendMessage(chat_id, msg_content[0])
  else:
    TelegramBot.sendMessage(chat_id, 'هنوز وارد نشدی که!\nاز /login برای وارد شدن استفاده کن')


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    msg_content = msg.get('text')
    # Check the message you entered
    if '/login' in msg_content:
      login(msg_content, chat_id)
    elif msg_content == '/show':
      show(chat_id)
    elif msg_content == '/start':
      TelegramBot.sendMessage(chat_id, 'چه کمکی میتونم بهت بکنم؟')
    else:
      TelegramBot.sendMessage(chat_id, 'چیزی که وارد کردی رو نمیفهمم!')


def main():
  # Loop message listen to users messages
  MessageLoop(TelegramBot, {'chat': on_chat_message}).run_as_thread()
  print('...دارم گوش میدم')

  while 1:
      time.sleep(10)


if __name__ == '__main__':
  main()
