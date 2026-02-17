import http.server
import socketserver
import socket

def get_local_ip():
    """Detecta la IP local de la computadora en la red."""
    try:
        # Crea un socket temporal para conectar con un DNS externo (no envía datos)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def start(port=8000):
    """Inicia el servidor e imprime cómo acceder desde otros dispositivos."""
    Handler = http.server.SimpleHTTPRequestHandler
    local_ip = get_local_ip()
    
    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"Server is running!")
            print(f"Local access:  http://localhost:{port}")
            print(f"Network access: http://{local_ip}:{port}")
            print("-" * 40)
            print("Note: Make sure your devices are on the same Wi-Fi network.")
            print("Press CTRL+C to stop.")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    start()
