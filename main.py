import asyncio

user_input = ""
counter = 0

async def get_input():
    global user_input
    while True:
        if user_input == "":
            user_input = await get_input_async("")
        await asyncio.sleep(.001) # short break to allow the taskSwapper to kick in

# Coroutine to get input asynchronously
async def get_input_async(str):
    return await asyncio.to_thread(input, str)

async def handle_input():
    global user_input
    cntr = 0
    while user_input != "":
        cntr += 1
        print (f"\n                    handle input: {user_input}")
        user_input = ""
        await asyncio.sleep(3)
        print (f"                    ready ({cntr})")

# Coroutine to get input asynchronously
async def learn():
    global counter
    counter += 1
    print(f"\n                                                             learning cycle {counter}")
    await asyncio.sleep(2)

async def taskSwapper():
    while True:
        await handle_input()
        await learn()

async def main():
    # Two tasks sharing processing time, only one of them is running,
    # If it pauses, the other task takes over (and vice versa)
    print(f"user input          input result                             learning")
    print(f"===============================================================================")
    await asyncio.gather(get_input(), taskSwapper())

# Start the asyncio event loop
asyncio.run(main())
