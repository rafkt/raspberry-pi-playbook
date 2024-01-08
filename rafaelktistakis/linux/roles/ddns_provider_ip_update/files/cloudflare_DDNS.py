import http.client
import json

# BEGIN ANSIBLE MANAGED BLOCK

# END ANSIBLE MANAGED BLOCK

connWTFisMyIp = http.client.HTTPSConnection("wtfismyip.com");
connWTFisMyIp.request("GET", "/text")
resHostIp = connWTFisMyIp.getresponse()
dataHostIp = resHostIp.read()
dataHostIpDecoded = dataHostIp.decode("utf-8")
print("Host IP:")
print(dataHostIpDecoded)

newIp = dataHostIpDecoded

conn = http.client.HTTPSConnection("api.cloudflare.com")

payload = {
    "content": newIp,
    "name": domainName,
    "type": domainType
    }

headers = {
    'Content-Type': "application/json",
    'X-Auth-Email': authEmail,
    'Authorization': "Bearer " + bearerToken 
    }

payloadStr = json.dumps(payload, separators=(",", ":"))
print("Request Payload: " + payloadStr)

conn.request("PATCH", "/client/v4/zones/" + zoneId +"/dns_records/" + recordId, payloadStr, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
