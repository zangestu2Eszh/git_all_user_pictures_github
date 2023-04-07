import requests
i=1
while(i<10000000):
     file=open(f'{i}.png', 'wb')
     file.write(requests.get(f'https://avatars.githubusercontent.com/u/{i}').content)
     file.close()
     i+=1
