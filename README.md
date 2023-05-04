# network-firewall
A network firewall for our class project

ON PROXY

To generate a self-signed certificate, perform the following steps on the proxy:

openssl genpkey -algorithm RSA -out private.key

openssl req -new -key private.key -out certificate.csr

openssl x509 -req -days 365 -in certificate.csr -signkey private.key -out certificate.crt

Based on where the certificate and private key are on the proxy, modify their paths in main.py 

Proxy port can be modified in main.py. Default is port 8080.

ON CLIENT

The certificate generated in the above step needs to be added to the trusted certificate folder on the client machine. If the client is using Ubuntu, the following steps should be taken:

sudo apt-get install ca-certificates

sudo cp certificate.crt /usr/local/share/ca-certificates/

sudo update-ca-certificates

To avoid bad certificate error, add proxy domain resolution on DNS or on the client device even if the proxy settings are configured with proxy IP and not proxy domain.

sudo nano /etc/hosts 

proxy_IP_address	domain_entered_while_creating_the_certificate

If testing proxy by using wget, make sure to do the following step as wget does not use system proxy settings

Modify https proxy in /etc/wgetrc to https://proxy_IP_address:proxy_port
