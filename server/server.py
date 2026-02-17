import http.server
import socketserver

def start(port=8000):
    """Inicia un servidor web básico en el puerto especificado."""
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"🚀 Server started at http://localhost:{port}")
            print("Press CTRL+C to stop.")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Esto permite ejecutar el archivo directamente también
    start()
