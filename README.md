# Info
Websockify token plugin for Server99
The format of the websockify token is DOMAIN_UUID:JWT_TOKEN
This plugin sends a request to the Server99 API to validate the authentication token and get the vnc port of the domain.

# Usage
See the [websockify wiki](https://github.com/novnc/websockify/wiki/Token-based-target-selection)
- Use `pip install /path/to/server99_websockify_token_plugin-X.X.tar.gz` to install the package
- Start websockify with the `--token-plugin server99-websockify-token-plugin.Server99Token` option
- The `--token-source` option is used to specify the Server99 API address
- The `--token-source` option is optional and defaults to `http://localhost:80`

# Example Usage
Runs a Websockify deamon for noVNC using this plugin
- Run a server on port 6080: `websockify --web=/usr/share/novnc/ 6080 --token-plugin server99-websockify-token-plugin.Server99Token`
- Run a server on port 6080 with a custom uri: `websockify --web=/usr/share/novnc/ 6080 --token-plugin server99-websockify-token-plugin.Server99Token --token-source http://127.0.0.1:8000`
- Use your browser to navigate to the Websockify server with the `token` argument: `http://127.0.0.1:6080/vnc.html?token=domain_uuid:jwt_token`

## Run as a service
- Create a file at `/etc/systemd/system/websockify-server99.service` with the contents
```
[Unit]
Description=Websockify Server99 Service
After=multi-user.target

[Service]
Type=simple
Restart=always
ExecStart=websockify --web=/usr/share/novnc/ 6080 --token-plugin server99-websockify-token-plugin.Server99Token

[Install]
WantedBy=multi-user.target
```
- Reload systemctl `systemctl daemon-reload`
- Enable the service (run the service on device startup) `systemctl enable websockify-server99.service`
- Start the service `systemctl start websockify-server99.service`
