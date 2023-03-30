import numpy as np
import time
import argparse

# python sticks.py --type both  --pile 50

mem = np.full(1, float("inf"))
def take(pile, turns, cur):
    if cur > pile:
        return float("inf")    
    if cur == pile:
        return turns
    else: 
        res = 1 + min(take(pile, turns, cur+1), take(pile, turns,cur+7), take(pile, turns, cur+9))
        return res

def takeDP(pile, turns, cur):
    global c
    if cur > pile:
        return (float("inf"),mem)
    if mem[cur] != float("inf"):
        return (mem[cur],mem)
    if cur == pile:
        return (turns,mem)
    else: 
        res =  1 + min(takeDP(pile, turns, cur+9)[0], takeDP(pile, turns,cur+7)[0], takeDP(pile, turns, cur+1)[0])
        if res < mem[cur]:
            mem[cur] = res 
        return (res, mem)
    
def both(pile):
    global mem
    start = time.monotonic()
    rec=[]
    for i in range(pile):
        rec.append(take(i,0, 0))
    end = time.monotonic()
    print(f"Recursive: \t{end-start}s")

    dp=[]
    start = time.monotonic()
    for i in range(pile):
        mem = np.full(i+1, float("inf"))
        dp.append(takeDP(i, 0, 0)[0])
    end = time.monotonic()
    print(f"DP: \t\t{end-start}s")
    print(list(set(rec) - set(dp)))

def rec(pile):
    start = time.monotonic()
    take(pile, 0, 0)
    end = time.monotonic()
    print(f"Recursive took {end-start}s")

def DP(pile):
    global mem
    start = time.monotonic()
    mem = np.full(pile+1, float("inf"))
    res = takeDP(pile, 0, 0)
    end = time.monotonic()
    print(f"DP took {end-start}s")
    print(f"Result: {res[0]}")
    print(f"\nTable: {res[1]}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='''Implemtation of 
    "taking sticks" algorithm using a naive recursive solution and a dynamic programming solution''')
    parser.add_argument('--type', help='DP, rec, both')
    parser.add_argument('--pile', help='Integer amount')
    args = parser.parse_args()

    pile=35
    if(args.type):
        if args.pile:
            pile=int(args.pile)
            mem = np.full(pile+1, float("inf"))
        if args.type=="DP":
            DP(pile)
        if args.type=="rec":
            rec(pile)
        if args.type=="both":
            both(pile)
    else:
        both(pile)
