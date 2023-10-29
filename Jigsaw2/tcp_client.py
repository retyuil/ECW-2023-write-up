# -*- conding: utf-8 -*-

import socket

alphabet = ["a","b","c","d",'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
color = {"0,0,0" : "black", "255,255,255" : "white", "255,0,0" : "red", "0,255,0": "green", "0,0,255" : "blue"}


def response1():
  return(b'yes')

def response2():
  return(b'42')

def response3(response):
  lettre = response.decode().split(':')
  before = ("before" in lettre[0])
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
  if quests == "1,2,3":
    return(rep1 +b","+b","+rep3)


def response7(response):
  print(response)
  if b"game" in response:
    return(response1())
  if b'life' in response:
    return(response2())
  if b'Easy' in response:
    return(response3(response))
  if b'color' in response:
    return(response4(response))



# address and port is arbitrary
def client(host="instances.challenge-ecw.fr", port=38475):
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

    data = rep1+ b","+ rep2+ b"," + rep3+ b"," + rep4
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
    print("[+] Sending to {}:{}".format(host, port))

    response = sock.recv(4096)
    print("[+] Received", (response.decode()))

    response = sock.recv(4096)
    print("[+] Received", (response.decode()))

client()