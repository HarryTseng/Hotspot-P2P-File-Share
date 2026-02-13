# Hotspot-P2P-File-Share
Cross-platform peer-to-peer file transfer over mobile hotspot 

(Designed for Mac ↔ Android without cloud or third-party services)

## Motivation
AirDrop works only inside Apple ecosystem, it is not available on Android.

In real life, a common scenario is that:

Laptop connects to phone hotspot for internet
- Devices are already in the same LAN
- But still cannot share files easily

Most solutions require:
- cloud upload/download
- account login
- external internet

Solutions above are not designed for such particular scenario.

## Goal

Provide a lightweight local-network file transfer protocol that works when:
- Android provides hotspot
- Mac joins the hotspot
- No internet access required
- No cloud/relay server
- No third-party service