# =====================================================
# LAPTOP RECEIVER FOR REAL-TIME ICU DATA
# =====================================================

import socket

# =====================================================
# SERVER CONFIGURATION
# =====================================================

HOST = '0.0.0.0'
PORT = 5000

# =====================================================
# CREATE SERVER SOCKET
# =====================================================

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen(1)

print("\nWaiting for mobile connection...\n")

# =====================================================
# ACCEPT CONNECTION
# =====================================================

conn, addr = server.accept()

print(f"Connected to Mobile: {addr}\n")

# =====================================================
# RECEIVE DATA
# =====================================================

buffer = ""

while True:

    try:

        data = conn.recv(1024)

        # connection closed
        if not data:
            break

        # decode bytes to string
        buffer += data.decode()

        # process complete lines
        while "\n" in buffer:

            line, buffer = buffer.split("\n", 1)

            print("Received ->", line)

    except Exception as e:

        print("\nError:")
        print(e)

        break

# =====================================================
# CLOSE CONNECTION
# =====================================================

conn.close()

server.close()

print("\nConnection Closed")