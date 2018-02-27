import socket

EOL1 = '\n\n'
EOL2 = '\n\r\n'
body = '''<h1>Hello, world!</h1>'''
response_params = [
    'HTTP/1.0 200 OK',
    'Date: Sat, 10 jun 2017 01:01:01 GMT',
    'Content-Type: text/html; charset=utf-8',
    'Content-Length: {}\r\n'.format(len(body)),
    body,
]
response = "\r\n".join(response_params).encode('utf-8')


def handle_connection(conn, addr):
    request = " "
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024).decode('utf-8')
    print(request)
    conn.send(response)
    conn.close()


def main():
    # socket.AF_INET    用于服务器与服务器之间的网络通信
    # socket.SOCK_STREAM    基于TCP的流式socket通信
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口可复用，保证我们每次Ctrl C之后，快速再次重启
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 8080))
    # 可参考：https://stackoverflow.com/questions/2444459/python-sock-listen
    s.listen(1)
    print('http://127.0.0.1:8080')

    try:
        while True:
            c, a = s.accept()
            handle_connection(c, a)
    finally:
        s.close()


if __name__ == '__main__':
    main()
