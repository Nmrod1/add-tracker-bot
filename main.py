from telethon import TelegramClient, events
from collections import defaultdict
import os
from threading import Thread

api_id = 12406538
api_hash = '6c82bc80720a5fb3a672b881149f1bb6'
bot_token = '7572315849:AAEra3cOWrF1Rk3Nh8BuZoVmEqzB1ZfB0tE'

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

referrals = defaultdict(int)

@client.on(events.ChatAction)
async def handler(event):
    if event.user_added:
        adder_id = event.action_message.from_id.user_id
        added_ids = [user.id for user in event.users]
        referrals[adder_id] += len(added_ids)

        sender = await event.get_sender()
        await event.reply(f"{sender.first_name} أضاف {len(added_ids)} عضو.\n📊 مجموع إضافاته: {referrals[adder_id]}")

@client.on(events.NewMessage(pattern='/score'))
async def score_handler(event):
    user_id = event.sender_id
    count = referrals.get(user_id, 0)
    await event.reply(f"📈 عدد الأشخاص اللي أضفتهم: {count}")
    from threading import Thread
from flask import Flask

app = Flask('')

@app.route('/')
def home():
    return "I'm alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

t = Thread(target=run)
t.start()
client.start()
client.run_until_disconnected()
