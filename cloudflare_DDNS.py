import http.client
import json


connWTFisMyIp = http.client.HTTPSConnection("wtfismyip.com");
connWTFisMyIp.request("GET", "/text")
resHostIp = connWTFisMyIp.getresponse()
dataHostIp = resHostIp.read()
dataHostIpDecoded = dataHostIp.decode("utf-8")
print("Host IP:")
print(dataHostIpDecoded)



newIp = dataHostIpDecoded
# Ansible managed block
# End of block

conn = http.client.HTTPSConnection("api.cloudflare.com")

#payload = "{\n  \"content\": \"xxx.xxx.xxx.xxx\",\n  \"name\": \"domain.com\",\n  \"type\": \"A\"}"

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
# more info at https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-list-dns-records?schema_url=https%3A%2F%2Fraw.githubusercontent.com%2Fcloudflare%2Fapi-schemas%2Fmain%2Fopenapi.yaml
# and at https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-patch-dns-record
#

