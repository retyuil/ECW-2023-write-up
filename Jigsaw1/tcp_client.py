# -*- conding: utf-8 -*-

import socket

alphabet = ["a","b","c","d",'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# address and port is arbitrary
def client(host="instances.challenge-ecw.fr", port=38456):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))

    response = sock.recv(4096)
    print("[+] Received", (response.decode()))

    response = sock.recv(4096)
    print("[+] Received", (response.decode()))

    data = b'yes'
    sock.send(data + b"\n")
    print("[+] Sending to {}:{}".format(host, port))

    response = sock.recv(4096)
    print("[+] Received", (response.decode()))

    data = b'42'
    sock.send(data + b"\n")
    print("[+] Sending to {}:{}".format(host, port))

    response = sock.recv(4096)
    print("[+] Received", (response.decode()))

    lettre = response.decode().split(':')
    before = ("before" in lettre[0])
    lettre = lettre[-1].replace("\n",'')
    lettre = lettre.replace(" ","")
    if before:
      data = alphabet[alphabet.index(lettre)-1].encode()
    else:
      data = alphabet[alphabet.index(lettre)-1].encode()
    sock.send(data + b"\n")
    print("[+] Sending to {}:{}".format(host, port))
    
    response = sock.recv(4096)
    print("[+] Received", (response.decode()))

    data = b'red'
    sock.send(data + b"\n")
    print("[+] Sending to {}:{}".format(host, port))

    response = sock.recv(4096)
    print("[+] Received", (response.decode()))
    
if __name__ == "__main__":
  client()