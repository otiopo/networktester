import requests, time
beftime = time.time()
response = requests.get("https://speedtest.net")
ping = round(time.time() - beftime) * 12 
print("Ping: " + str(ping))
if ping > 0:
        print("Download: " + str((len(response.content) / ping) / 100))
        print("Upload: " + str((len(response.content) / ping) / 1000))
else:
        print("Download: " + str((len(response.content)) / 100))
        print("Upload: " + str((len(response.content)) / 1000))


