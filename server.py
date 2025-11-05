import socket
import os

def handle_request(client_socket, file_path):
    request = client_socket.recv(1024).decode('utf-8')
    
    if "GET" in request:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                html_content = file.read()
            response = f"""HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8

{html_content}
"""
        else:
            response = """HTTP/1.1 404 Not Found
Content-Type: text/html; charset=UTF-8

<html><body><h1>404 Not Found</h1></body></html>
"""
        client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

def create_http_server(host, port, file_path):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    
    print(f"Server running at http://{host}:{port}")
    
    while True:
        client_socket, client_address = server_socket.accept()
        handle_request(client_socket, file_path)

create_http_server("127.0.0.1", 8080, "index.html")
