from waitress import serve
from app import app  # Import your Flask/Django WSGI app

if __name__ == '__main__':
    # Documentation: https://docs.pylonsproject.org/projects/waitress/en/stable/
    print("Starting Waitress server on 0.0.0.0:8000...")
    serve(
        app,
        host='0.0.0.0',
        port=8000,
        threads=4,          # Analogous to Gunicorn workers (though threaded)
        channel_timeout=20, # Cleanup inactive connections
        cleanup_interval=30
    )