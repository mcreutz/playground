import requests

r = requests.get('https://jsonplaceholder.typicode.com/users')

with open("myfile.txt", 'w') as writer:
    writer.write(r.text)
