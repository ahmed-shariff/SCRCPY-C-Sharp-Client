import cv2
import socket
from multiprocessing import Process
from tqdm import tqdm

def main():
    s_input = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_input.bind(('127.0.0.1', 27183))
    s_input.listen(1)
    conn, addr = s_input.accept()

    print(conn, addr)
    print(conn.recv(64).decode('utf-8'))
    print(int.from_bytes(conn.recv(2), "big"))
    print(int.from_bytes(conn.recv(2), "big"))

    s_output = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_output.bind(('127.0.0.1', 27184))
    s_output.listen(1)
    p = Process(target=client)
    p.start()
    out_conn, addr = s_output.accept()

    print("\n", out_conn, addr)
    while True:
        out_conn.send(conn.recv(1))
    p.join()
    

def client():
    cap = cv2.VideoCapture("tcp://127.0.0.1:27184")
    print(cap)

    for _ in tqdm(range(1000)):
        r, img = cap.read()
        if not r:
            continue
        cv2.imshow("", img)
        cv2.waitKey(20)
    

if __name__ == "__main__":
    main()
    # client()
