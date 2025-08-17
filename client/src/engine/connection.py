from client.src.engine.settings import *

def try_connect() -> socket.socket | None:
    """
    try and connect to the server and returns if the client connected successfully or not

    :return: socket.socket / None for the clients connection to the server
    """

    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    conn.settimeout(5)  # after 5 seconds time out connection return False

    try:
        print("trying to connect")
        conn.connect((SERVER_ADDRESS, SERVER_PORT))
        print("Connected successfully")
        return conn
    except ConnectionRefusedError as e:
        print(f"server not running / refused to connect")
    except socket.timeout:
        print("Connection timed out.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

def disconnect(conn:socket.socket) -> None:
    """

    :param conn: the clients connection to the server
    :return: None
    """
    if conn is not None:
        conn.close()