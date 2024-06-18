```bash
sudo ufw enable 
sudo ufw status   # show status
sudo ufw allow from <clients> to any port nfs  # <clients> can access nfs port 2049
sudo ufw disable
sudo ufw show added  # show added rules
````
