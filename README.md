# Info
Websockify token plugin for Libvirt domains, token is the Libvirt domain uuid.
This plugin lookups the domain xml using the Libvirt api and gets the vnc port.

# Usage
See the [websockify wiki](https://github.com/novnc/websockify/wiki/Token-based-target-selection)
- Use `pip install websockify-LibvirtDomain` to install the package
- Start websockify with the `--token-plugin websockify_LibvirtDomain.LibvirtDomain` option
- The `--token-source` option in Websockify can be used to specify a Libvirt Uri, without this option specified the uri is `qemu:///system`

# Example Usage
Runs a Websockify deamon for noVNC using this plugin
- Run a server on port 6080: `websockify --web=/usr/share/novnc/ 6080 --token-plugin websockify_LibvirtDomain.LibvirtDomain`
- Run a server on port 6080 with a custom libvirt uri: `websockify --web=/usr/share/novnc/ 6080 --token-plugin websockify_LibvirtDomain.LibvirtDomain --token-source 'LibvirtUri'`
- Use your browser to navigate to the Websockify server with the `token` argument being the domain uuid: `http://some-ip:6080/vnc.html?token=some-uuid`

## Run as a service
- Create a file at `/etc/systemd/system/websockify-libvirtdomain.service` with the contents
```
[Unit]
Description=Websockify LibvirtDomain
After=multi-user.target

[Service]
Type=simple
Restart=always
ExecStart=websockify --web=/usr/share/novnc/ 6080 --token-plugin websockify_LibvirtDomain.LibvirtDomain

[Install]
WantedBy=multi-user.target
```
- Reload systemctl `systemctl daemon-reload`
- Enable the service (run the service on device startup) `systemctl enable websockify-libvirtdomain.service`
- Start the service `systemctl start websockify-libvirtdomain.service`
