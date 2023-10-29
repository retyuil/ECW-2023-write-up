# -*- conding: utf-8 -*-

import socket
import glob
import cv2
import pandas as pd

alphabet = ["a","b","c","d",'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
color = {"0,0,0" : "black", "255,255,255" : "white", "255,0,0" : "red", "0,255,0": "green", "0,0,255" : "blue"}




def braille_to_text(braille_string):
    braille_dict = {
        '⠁': 'a', '⠃': 'b', '⠉': 'c', '⠙': 'd', '⠑': 'e',
        '⠋': 'f', '⠛': 'g', '⠓': 'h', '⠊': 'i', '⠚': 'j',
        '⠅': 'k', '⠇': 'l', '⠍': 'm', '⠝': 'n', '⠕': 'o',
        '⠏': 'p', '⠟': 'q', '⠗': 'r', '⠎': 's', '⠞': 't',
        '⠥': 'u', '⠧': 'v', '⠺': 'w', '⠭': 'x', '⠽': 'y',
        '⠵': 'z', ' ⠀ ': ' ',"x" : " ",":" : ":" ,"," : "," ,
    }
    
    text_string = ""
    braille_string = braille_string.replace(" ⠀","x")
    for char in braille_string:
        if char in braille_dict:
            text_string += braille_dict[char]
    
    return text_string


  


def response1():
  return(b'yes')

def response2():
  return(b'42')

def response3(response):
  before = ("before" in response.decode())
  lettre = response.decode().split(':')
  
  lettre = lettre[-1].replace("\n",'')
  lettre = lettre.replace(" ","")
  if before:
    data = alphabet[alphabet.index(lettre)-1].encode()
  else:
    data = alphabet[alphabet.index(lettre)+1].encode()
  return(data)

def response4(response):
  couleur = response.decode().split(':')
  couleur = couleur[-1].replace("\n",'')
  couleur = couleur.replace(" ","")
  data = color[couleur].encode()
  return(data)

def response5():
  return(rep1+ b","+ rep2+ b"," + rep3+ b"," + rep4)

def response6(response):
  quests = response.decode().split("(s)")
  quests = quests[-1].split("u")
  quests = quests[0].replace(" ","")
  if quests == "1":
    return(rep1)
  if quests == "2":
    return(rep2)
  if quests == "3":
    return(rep3)
  if quests == "1,2":
    return(rep1 +b","+rep2)
  if quests == "2,3":
    return(rep2 +b","+rep3)
  if quests == "1,3":
    return(rep1 +b","+rep3)

  if quests == "1,2,3":
    return(rep1 +b"," + rep2 +b","+rep3)


def response7(response):
  print(response)
  if b"game" in response:
    return(response1())
  if b'life' in response:
    return(response2())
  if b'letter' in response:
    return(response3(response))
  if b'color' in response:
    return(response4(response))
  if b'format' in response:
    return(response6(response))
  if b'commas' in response:
    return(response5())

def response8(response):
  texte = braille_to_text(response.decode().split(".")[-1])
  word = texte.split(":")[-1]
  word = word[1::]
  return(word.encode())

def response9(response):
  response = response[3::]
  file_path = 'image.png' 

  with open(file_path, 'wb') as binary_file:
      binary_file.write(response)

  img = cv2.imread(file_path)
  detect = cv2.QRCodeDetector()
  value, points, straight_qrcode = detect.detectAndDecode(img)
  word = value.split(":")[-1]
  word = word[1::]
  return(word.encode())


def response10(response):
  response = response[4::]
  file_path = 'image2.png' 

  with open(file_path, 'wb') as binary_file:
      binary_file.write(response)

  img = cv2.imread(file_path)
  detect = cv2.QRCodeDetector()
  value, points, straight_qrcode = detect.detectAndDecode(img)
  print(value)
  print(braille_to_text(value))
  value = braille_to_text(value)
  value = value.encode()
  print("value : ",value)
  return(response7(value))


# address and port is arbitrary
def client(host="instances.challenge-ecw.fr", port=39257):
  global rep1
  global rep2
  global rep3
  global rep4

  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))

    response = sock.recv(4096)
    print("[+] Received", (response.decode()))

    response = sock.recv(4096)
    print("[+] Received", (response.decode()))

    data = response1()
    rep1 = data
    sock.send(data + b"\n")
    print("[+] Sending to {}:{}".format(host, port))

    response = sock.recv(4096)
    print("[+] Received", (response.decode()))

    data = response2()
    rep2 = data
    sock.send(data + b"\n")
    print("[+] Sending to {}:{}".format(host, port))

    response = sock.recv(4096)
    print("[+] Received", (response.decode()))

    data = response3(response)
    rep3 = data
    sock.send(data + b"\n")
    print("[+] Sending to {}:{}".format(host, port))
    
    response = sock.recv(4096)
    print("[+] Received", (response.decode()))


    data = response4(response)
    rep4 = data
    sock.send(data + b"\n")
    print("couleur : ",data)
    print("[+] Sending to {}:{}".format(host, port))


    response = sock.recv(4096)
    print("[+] Received", (response.decode()))

    response = sock.recv(4096)
    print("[+] Received", (response.decode()))

    data = response5()
    sock.send(data + b"\n")
    print("[+] Sending to {}:{}".format(host, port))

    response = sock.recv(4096)
    print("[+] Received", (response.decode()))

    data = response6(response)
    sock.send(data + b"\n")
    print("[+] Sending to {}:{}".format(host, port))

    response = sock.recv(4096)
    print("[+] Received", (response.decode()))


    data = response7(response)
    sock.send(data + b"\n")
    print("Sended : ",data)
    print("[+] Sending to {}:{}".format(host, port))

    response = sock.recv(4096)
    print("[+] Received", (response.decode()))

    response = sock.recv(4096)
    print("[+] Received", (response.decode()))

    data = response8(response)
    sock.send(data + b"\n")
    print("Sended : ", data.decode())
    print("[+] Sending to {}:{}".format(host, port))

    response = sock.recv(8192)
    data = response9(response)
    sock.send(data + b"\n")
    print("Sended : ", data.decode())
    print("[+] Sending to {}:{}".format(host, port))

    response = sock.recv(4096)
    print("[+] Received", (response).hex())
    
    data = response10(response)
    sock.send(data + b"\n")
    print("Sended : ", data.decode())
    print("[+] Sending to {}:{}".format(host, port))

    response = sock.recv(4096)
    print("[+] Received", (response).decode())
    response = sock.recv(4096)
    print("[+] Received", (response).decode())

    data = "retyuil2".encode()
    sock.send(data + b"\n")
    print("Sended : ", data.decode())
    print("[+] Sending to {}:{}".format(host, port))

    response = sock.recv(4096)
    print("[+] Received", (response).decode())

    response = sock.recv(4096)
    print("[+] Received", (response).decode())

    response = sock.recv(4096)
    print("[+] Received", (response).decode())

    response = sock.recv(4096)
    print("[+] Received", (response).decode())

    response = sock.recv(4096)
    print("[+] Received", (response).decode())

client()