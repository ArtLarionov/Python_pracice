def myreceive(sock, msglen):
    msg = ''
    while len(msg) < msglen:
        chunk = sock.recv(msglen - len(msg))
        if chunk == '':
            raise RuntimeError("broken")
        msg = msg + chunk
    return msg
