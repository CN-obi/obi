#Python Code Obfuscated by CyberJeevi py-obfuscator
 

import base64, codecs
magic = 'IyBhdXRob3IgOiBAU3locnVsYXJ2XwojIC0qLSBjb2Rpbmc6IHV0Zi04IC0qLQoKaW1wb3J0IG9zCmltcG9ydCBzeXMKaW1wb3J0IGZpbGVpbnB1dAoKTiA9ICdcMDMzWzBtJwpEID0gJ1wwMzNbOTBtJwpXID0gJ1wwMzNbMTszN20nCkIgPSAnXDAzM1sxOzM0bScKUiA9ICdcMDMzWzE7MzFtJwpHID0gJ1wwMzNbMTszMm0nClkgPSAnXDAzM1sxOzMzbScKQyA9ICdcMDMzWzE7MzZtJwoKYXNrID0gRyArICdbJyArIFcgKyAnPycgKyBHICsgJ10gJwpzdWtzZXMgPSBHICsgJ1snICsgVyArICfiiJonICsgRyArICddICcKZXJvciA9IFIgKyAnWycgKyBXICsgJyEnICsgUiArICddJwoKYmFubmVyID0gIiIiCnt9ICAgICAgICAgX25ubm5fe30gICAgICAgIF9fX19fX19fX19fX19fX19fCnt9ICAgICAgICBkR0dHR01NYnt9ICAgICAgfCAgICAgICAgICAgICAgICAgfAp7fSAgICAgICBAcH5xcH5+cU1ie30gICAuX3wge31CYXNoIE91YmZ1c2NhdGUge318Cnt9ICAgICAgIE17fSh7fUB7fSkoe31Ae30pIHt9TXx7fSAgLyAgfF9fX19fX19fX19fX19fX19ffAp7fSAgICAgICBALHt9LS0tLS57fUpNfHt9Xy8'
love = 'Xr30tVPNtVPOXH157sIksKl97sFNtpHgZPvNtVPNtMScDVPNtVPNtVPOkF1WvPvNtVPOxJyNtVPNtVPNtVPNtpHgYLtbtVPOzJyNtVPNtVPNtVPNtVPOGGH1vPvNtVRunGFNtVPNtVPNtVPNtVR1AGH0tVPNtr31Qo2EyMPOvrFO7sGbtr31iLzxXr30tVPOTpH0tVPNtVPNtVPNtVPOAGH1AVPNtVUg9IRptVPNtVPNtr306VUg9DRABK29vnFNmPag9VS9ssPqpVP4tVPNtVPNtVUkpr31xHlOkGHjXr30tsPNtVPOtYvNtVPNtVPO8VTNaVSk7sIckPag9KlxtVPNtVPOpYag9K19sYag9YUjtVPNtVP4aPyksK19sVPNtXKg9GH1AGH1Dr318VPNtYvpXVPNtVPOtYFptVPNtVPNtLP0gWjbvVvVhMz9loJS0XRDfIlkRYSpfEPkKYSxfIlkRYSpfEPkKYRDfIlkRYSpfEPkMYRDfIlkRYSxfEPkUYSpfElkRYRpfIlkUYSxfEPkMYRDfJFkRYSxfEPkMXDbXLzShozIlZvN9VPVvVtbtVPO7sIg7sGS7sI17sFOSozAlnKO0VPNtVPNtr31or30lr31qr30tETIwpayjqNbvVvVhMz9loJS0XRpfIlkUYSpfElkKYRpfIlxXPaOlnJ50VTWuoz5yptcjpzyhqPOvLJ5hMKVlPtcxMJLtMTIepzyjXPx6PvNtVUElrGbXVPNtVPNtVUAwVQ'
god = '0gcmF3X2lucHV0KGFzayArIFcgKyAiU2NyaXB0ICIgKyBHICsgIj4gIiArIFcpCiAgICAgICBmID0gb3BlbihzYywncicpCiAgICAgICBmaWxlZGF0YSA9IGYucmVhZCgpCiAgICAgICBmLmNsb3NlKCkKCiAgICAgICBuZXdkYXRhID0gZmlsZWRhdGEucmVwbGFjZSgiZXZhbCIsImVjaG8iKQoKICAgICAgIG91dCA9IHJhd19pbnB1dChhc2sgKyBXICsgIk91dHB1dCIgKyBHICsgIiA+ICIgKyBXKQogICAgICAgZiA9IG9wZW4ob3V0LCd3JykKICAgICAgIGYud3JpdGUobmV3ZGF0YSkKICAgICAgIGYuY2xvc2UoKQoKICAgICAgIG9zLnN5c3RlbSgidG91Y2ggdGVzLnNoIikKICAgICAgIG9zLnN5c3RlbSgiYmFzaCAiICsgb3V0ICsgIiA+IHRlcy5zaCIpCiAgICAgICBvcy5yZW1vdmUob3V0KQogICAgICAgb3Muc3lzdGVtKCJtdiAtZiB0ZXMuc2ggIiArIG91dCkKICAgICAgIHByaW50IChzdWtzZXMgKyAiRG9uZS4uIikKCiAgIGV4Y2VwdCBLZXlib2FyZEludGVycnVwdDoKICAgICAgIHByaW50IChlcm9yICsgIiBTdG9wcGVkISIpCiAgIGV4Y2VwdCBJT0Vycm9yOgogICAgICAgcHJpbnQgKGVyb3IgK'
destiny = 'lNvVRMcoTHtGz90VRMiqJ5xVFVcPtcxMJLtMJ5epzyjXPx6PvNtVUElrGbXVPNtVPNtVUAwpzyjqPN9VUWuq19coaO1qPuup2ftXlOKVPftVyAwpzyjqPNvVPftElNeVPV+VPVtXlOKXDbtVPNtVPNto3I0pUI0VQ0tpzS3K2yhpUI0XTSmnlNeVSptXlNvG3I0pUI0VPVtXlOUVPftVw4tVvNeVSpcPvNtVPNtVPOipl5mrKA0MJ0bVzWup2tgo2WzqKAwLKEyVPVtXlOmL3WcpUDtXlNvVP1iVPVtXlOiqKEjqKDtXDbtVPNtVPNtpUWcoaDtXUA1n3AyplNeVPWRo25yYv4vXDbtVPOyrTAypUDtF2I5Lz9upzEWoaEypaW1pUD6PvNtVPNtVPOjpzyhqPNbMKWipvNeVPVtH3EipUOyMPRvXDbtVPOyrTAypUDtFH9SpaWipwbXVPNtVPNtVUOlnJ50VPuypz9lVPftVvOTnJkyVR5iqPOTo3IhMPRvXDbXPaEun29eVQ0tpzS3K2yhpUI0XSptXlNvD2uio3AyVvNeVRptXlNvVQ4tVvxXPzyzVUEun29eVQ09VPVkVvOipvO0LJginlN9CFNvZQRvBtbtVPOyozglnKNbXDcyoTyzVUEun29eVQ09VPVlVvOipvO0LJginlN9CFNvZQVvBtbtVPOxMJglnKNbXDcyoUAyBtbtVPOjpzyhqPNbMKWipvNeVPVtI3WiozptnJ5jqKDvXDb='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))