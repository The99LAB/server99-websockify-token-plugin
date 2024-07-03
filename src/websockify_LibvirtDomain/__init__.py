from xml.etree import ElementTree as ET
import requests

class Server99Token(object):
    def __init__(self, src):
        # src is the address of the server99 backend
        # For development, it should be http://localhost:5000
        if src is None:
            src = "http://localhost:80"
        self.src = src

    def lookup(self, token):
        # The token is the UUID of the domain and the jwt token
        # Token format DOMAIN_UUID:JWT_TOKEN
        domain_uuid, jwt_token = token.split(":")

        # Get the vnc_port from the server99 backend
        # The server99 backend will check if the user has access to the domain
        # If the user has access, it will return the vnc_port
        backend_response = requests.get(f"{self.src}/api/vm-manager/{domain_uuid}/vnc_port", headers={"Authorization": f"Bearer {jwt_token}"})
        if backend_response.status_code != 200:
            raise Exception("Unauthorized access to the domain")
        else:
            vnc_port = backend_response.text
            return ("localhost", vnc_port)
