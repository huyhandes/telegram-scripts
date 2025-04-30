import asyncio
from datetime import datetime, timedelta

from telethon import TelegramClient

# Replace with your own values

client = TelegramClient("session", APP_ID, APP_HASH)
APP_ID = # put your value here
APP_HASH = # put your value here
GROUP_ID = # put your value here 
CHANNEL_ID = # put your value here
LIMIT = 1000


async def crawl_messages():
    messages = []
    async with client:
        entity = await client.get_entity(GROUP_ID)
        offset_date = datetime.now() - timedelta(days=7)
        messages = await client.get_messages(
            entity=entity,
            offset_id=0,
            offset_date=offset_date,
            reply_to=CHANNEL_ID,
            limit=LIMIT,
        )

    return [message.message for message in messages]


async def main():
    await client.start()
    # topics = await client(
    #     GetForumTopicsRequest(channel=GROUP_NAME, offset_date=datetime.now())
    # )
    # for topic in topics.topics:
    messages = await crawl_messages()
    # Store messages in database (implementation needed)
    # store_messages(topic.id, messages)
    print(messages)


if __name__ == "__main__":
    asyncio.run(main())
