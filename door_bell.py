import socket

mode = input("Enter mode (send / receive): ").lower()

PORT = 5000

if mode == "receive":
    s = socket.socket()
    s.bind(("", PORT))
    s.listen(1)
    print("Waiting for doorbell...")

    conn, addr = s.accept()
    msg = conn.recv(1024).decode()
    if msg == "RING":
        print("🔔 Ding Dong!")

    conn.close()

elif mode == "send":
    ip = input("Enter receiver IP: ")
    s = socket.socket()
    s.connect((ip, PORT))
    s.send(b"RING")
    print("Signal sent")

    s.close()

else:
    print("Invalid mode")
