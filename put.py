import requests
import temps



BASE = 'http://18.221.104.149/'
        
monitor= temps.tempinit()

response = requests.put(BASE , json=monitor)

print(response.json())
