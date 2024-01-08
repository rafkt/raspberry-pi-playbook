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


# Below command is to be used to get current list of DNS records under the zone identifier. Zone identifier obtained through the portal
# curl --request GET \
#  --url https://api.cloudflare.com/client/v4/zones/zone_identifier/dns_records \
#  --header 'Content-Type: application/json' \
#  --header 'X-Auth-Email: '
