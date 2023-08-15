import asyncio

async def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time left: {seconds} seconds")
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        seconds -= 1
    print("Time's up!")

# Set the duration of the timer in seconds
duration = 10

# Create an event loop
loop = asyncio.get_event_loop()

# Run the timer asynchronously
loop.run_until_complete(countdown_timer(duration))

# Close the event loop
loop.close()
