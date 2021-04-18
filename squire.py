from telethon.sync import TelegramClient, events
import re, asyncio

api_id = 4078073
api_hash = '79ca6aec3f4f7991899b44b71b826beb'
group = -1001207622861
cw = '@chtwrsbot'


print('Trying to connect telegram')
with TelegramClient("asd", api_id, api_hash) as client:
    print("Connected to telegram")



    @client.on(events.NewMessage(chats=group, incoming=True))
    async def group_handler(event):
        msg=event.raw_text
        if re.search('/g_withdraw',msg):
            await client.send_message(cw, event.raw_text)
        if re.search('Guild Warehouse',msg):
            a=event.raw_text.split('\n')
            a=[i.split() for i in a]
            a=[ [i[0],i[-1]] for i in a[1:]]
            a=[" ".join(i) for i in a]
            a=[a[i:i+9] for i in range(len(a))[::9]]
            a=[" ".join(i) for i in a]
            for i in a:
                await client.send_message(cw, '/g_withdraw ' + i)
                await asyncio.sleep(2.5)


    @client.on(events.NewMessage(chats=cw, incoming=True))
    async def cw_handler(event):
        msg=event.raw_text
        if re.search('Withdrawing',msg) or re.search('Not enough items on guild stock',msg) or re.search('invalid action',msg) or re.search('You are too busy',msg):
            await event.mark_read()
            await client.send_message(group, event.raw_text)


    client.run_until_disconnected()
