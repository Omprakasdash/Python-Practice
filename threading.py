#Write a python program to accept a line of text and 
# generate their words in each and every second using thead.

import threading,time
def word(n):
    n=input("Enter the line of statements").split()
    for i in n:
        print(threading.current_thread().name,i)
        time.sleep(1)
wt=threading.Thread(target=word)

wt.start()