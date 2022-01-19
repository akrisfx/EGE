from subprocess import call, run
def f(ch):
    if ch&1:
        return ch + 1
    else:
        return(ch * 2)


arr = [i for i in range(10)]
print(arr)

arr = list(map(lambda x: x*2, arr))
print(arr)
print(f'{bin(10)} to {bin(10 << 2)}')
print((8 >> 1), (10 << 2) >> 2)



run(["notify-send", "This is title!", "This is message body!"],)