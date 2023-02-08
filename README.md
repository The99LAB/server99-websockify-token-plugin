# Info
Websockify token plugin for Libvirt domains, token is the Libvirt domain uuid.
This plugin lookups the domain xml using the Libvirt api and gets the vnc port.

# Usage
See the [websockify wiki](https://github.com/novnc/websockify/wiki/Token-based-target-selection)
- The `--token-source` option in Websockify can be used to specify a Libvirt Uri, without this option specified the uri is `qemu:///system`

# Example Usage
Runs a Websockify deamon for noVNC using this plugin
- Run a server on port 6080: `websockify --web=/usr/share/novnc/ 6080 --token-plugin websockify_LibvirtDomain.LibvirtDomain`
- Run a server on port 6080 with a custom libvirt uri: `websockify --web=/usr/share/novnc/ 6080 --token-plugin websockify_LibvirtDomain.LibvirtDomain --token-source 'LibvirtUri'`
- Use your browser to navigate to the Websockify server with the `token` argument being the domain uuid: `http://some-ip:6080/vnc.html?token=some-uuid`
