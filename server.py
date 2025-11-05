def handle_request(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    
    if "GET /index.html" in request:
        try:
            with open("index.html", "r") as file:
                html_content = file.read()
            response = f"HTTP/1.1 200 OK\nContent-Type: text/html; charset=UTF-8\n\n{html_content}"
        except FileNotFoundError:
            response = "HTTP/1.1 404 Not Found\n\n<html><body><h1>404 Not Found</h1></body></html>"
    else:
        response = "HTTP/1.1 400 Bad Request\n\n<html><body><h1>400 Bad Request</h1></body></html>"

    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

def create_simple_server(host, port):
    with open(f"/dev/tcp/{host}/{port}", 'r+') as server_socket:
        print(f"Server running at http://{host}:{port}")

        while True:
            client_socket, _ = server_socket.accept()
            handle_request(client_socket)

create_simple_server("127.0.0.1", 8080)
