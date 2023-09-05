import asyncio

_ = 0
broadcast = None

async def listener():
    while True:
        await asyncio.sleep(0.5)
        if _ != 0:
            broadcast.set_exception(ValueError('the _ is not 0 anymore!'))
        # else:
        #     print('okay', _)

async def executor():
    loop = asyncio.get_event_loop()
    while True:
        x = int(await loop.run_in_executor(None, input, 'execute: '))
        print('=-=-=-1',x)
        global _
        _ = x

async def main():
    global broadcast
    loop = asyncio.get_event_loop()
    loop.create_task(listener())
    loop.create_task(executor())
    while True:
        broadcast = loop.create_future()
        try:
            await broadcast
        except ValueError as e:
            print('got error', e)

asyncio.get_event_loop().run_until_complete(main())