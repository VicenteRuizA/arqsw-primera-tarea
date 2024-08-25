MAX_COUNTERS = 10
counters = [0]*MAX_COUNTERS
async def add_counter(counter, amount):
    if(counter > 0 and counter < MAX_COUNTERS):
        counters[counter]+=amount
        return counters[counter]
    return None
