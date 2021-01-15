import requests

url = 'https://admin.googleapis.com/admin/directory/v1/users'

body = '{
"primaryEmail": "liz@example.com",
"name": {
 "givenName": "Elizabeth",
 "familyName": "Smith"
},
"suspended": false,
"password": "new user password",
"hashFunction": "SHA-1",
"changePasswordAtNextLogin": false,
"ipWhitelisted": false,
"ims": [
 {
  "type": "work",
  "protocol": "gtalk",
  "im": "liz_im@talk.example.com",
  "primary": true
 }
],
"emails": [
 {
  "address": "liz@example.com",
  "type": "home",
  "customType": "",
  "primary": true
 }
],
"addresses": [
 {
  "type": "work",
  "customType": "",
  "streetAddress": "1600 Amphitheatre Parkway",
  "locality": "Mountain View",
  "region": "CA",
  "postalCode": "94043"
 }
],
"externalIds": [
 {
  "value": "12345",
  "type": "custom",
  "customType": "employee"
 }
],
"relations": [
 {
  "value": "Mom",
  "type": "mother",
  "customType": ""
 },
 {
  "value": "manager",
  "type": "referred_by",
  "customType": ""
 }
],
"organizations": [
 {
  "name": "Google Inc.",
  "title": "SWE",
  "primary": true,
  "type": "work",
  "description": "Software engineer"
 }
],
"phones": [
 {
  "value": "+1 nnn nnn nnnn",
  "type": "work"
 }
],
"orgUnitPath": "/corp/engineering",
"includeInGlobalAddressList": true
}'

x = requests.post(url, body,)

if (x.status = 200 ):
	print('all good')

url1 = 'https://admin.googleapis.com/admin/directory/v1/users/liz@example.com'

y = requests.delete(url1)

