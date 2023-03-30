import numpy as np
import time
import argparse


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
    if cur > pile:
        return (float("inf"),0)
    if mem[cur] != float("inf"):
        return (mem[cur],0)
    if cur == pile:
        return (turns,0)
    else: 
        res =  1 + min(takeDP(pile, turns, cur+9)[0], takeDP(pile, turns,cur+7)[0], takeDP(pile, turns, cur+1)[0])
        if res < mem[cur]:
            # print(f"Min: {res}, Old Table: {mem[cur]}")
            mem[cur] = res 
        return (res, mem)
    
def both(pile):
    start = time.monotonic()
    correct = []
    for i in range(pile):
        correct.append(take(i,0, 0))
    end = time.monotonic()
    print(f"Recursive took {end-start}s")

    start = time.monotonic()
    for i in range(pile):
        if correct[i] != int(takeDP(i, 0, 0)[0]): 
            print(f"Mismatch at {i}.\n\tExpected: {correct[i]}, Got: {takeDP(i, 0, 0)[0]}")
            
    end = time.monotonic()
    print(f"DP took {end-start}s")

def rec(pile):
    start = time.monotonic()
    take(pile, 0, 0)
    end = time.monotonic()
    print(f"Recursive took {end-start}s")

def DP(pile):
    start = time.monotonic()
    mem = np.full(pile+1, float("inf"))
    table = takeDP(pile, 0, 0)[1]
    end = time.monotonic()
    print(f"DP took {end-start}s")
    print(table)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Description of your script')
    parser.add_argument('--type', help='DP, rec, both')
    parser.add_argument('--pile', help='Integer amount')
    args = parser.parse_args()

    if(args.type):
        pile=35
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
        both(50)
