---
date: 2026-01-01
title: "HiveNet — P2P Decentralized Texting"
tags: ["Swift","SwiftUI","P2P","Networking","Cryptography","VANET","iOS"]
author: "Huzaif"
showreadingtime: false
hideSummary: true
draft: false
---

# HiveNet — Peer-to-Peer Decentralized Communication

> An offline network that does not need internet, connecting devices and relaying messages peer-to-peer using local nodes.

**[Source Code](https://github.com/huz4f/HiveNet)**

---

### Overview

HiveNet is an offline communication network engineered to operate completely without internet access, cellular reception, or centralized servers. It transforms nearby devices into independent local nodes that discover each other, form dynamic mesh topologies, and relay encrypted text messages. Built for off-grid scenarios and high-velocity environments — vehicular ad-hoc networks (VANET), mobile ad-hoc networks (MANET), highway transit, and disaster recovery zones — where traditional connectivity is unavailable.

---

### Architecture & Tech Stack

- **Language**: Swift 5+
- **UI Framework**: SwiftUI with custom honeycomb/hexagonal geometry and radar scanning visuals
- **Ad-Hoc Networking**: Apple MultipeerConnectivity (MPC) — `MCSession`, `MCNearbyServiceBrowser`, `MCNearbyServiceAdvertiser` broadcasting `_vanet-hive._tcp`
- **Location & Kinematics**: CoreLocation for real-time vehicle speed, heading, coordinates. Node-to-node proximity via Haversine formula
- **Cryptography**: CryptoKit + Security Framework — ECDSA P-256 key generation, SHA-256 payload hashing, iOS Keychain storage
- **Concurrency**: Swift Concurrency (`async`/`await`, `@MainActor`) + Combine

---

### Core Systems

#### Velocity-Adaptive Safety Messages (BSM)

Emulates automotive V2V standards with periodic broadcasts containing node profile data (ID, GPS, speed, heading, public key). Broadcast intervals dynamically adjust based on velocity:

| Speed | Interval |
|-------|----------|
| Stationary (< 5 km/h) | Every 10 seconds |
| Urban (5 – 30 km/h) | Every 5 seconds |
| Highway (> 30 km/h) | Every 1 second |

Nodes maintain an active neighbor table with automated stale-peer pruning after 5 seconds of silence.

#### Multi-Hop Relay & Routing

Messages aren't restricted to direct connections — HiveNet supports multi-hop packet forwarding via `RelayEnvelope`:

- **Dynamic Routing Table**: Nodes passively learn routes from transit traffic with 30-second expiry
- **Unicast when known**: Directed delivery via optimal next hop
- **Controlled flood when unknown**: Eliminates loops via duplicate UUID dropping and `visitedIDs` tracking
- **TTL**: Default 7 hops maximum

#### Intelligent Node Scoring

`NodeConnectionManager` automatically manages 5 concurrent MPC slots using composite scoring:

- **Distance** (30%) — prefers nodes within 1 km
- **Signal Strength** (25%)
- **Stability & Freshness** (25%) — connection age and discovery duration
- **Speed Similarity** (20%) — matches vehicles at similar velocities to minimize link breakage

Anti-churn protection enforces 60-second minimum connection lifetime and 15% score improvement threshold before evicting peers.

#### Cryptographic Security

- Every packet digitally signed with **ECDSA P-256**
- Intermediate forwarders cannot tamper with relayed messages — inner packet signed by origin
- **Anti-replay**: Rejects timestamps older than 30 seconds and caches seen packet UUIDs

#### Battery-Aware Discovery

When stationary (< 3 km/h for 10 seconds), the node enters low-power duty cycling — 15 seconds active browsing, 45 seconds asleep.

---

### UI

- **HiveView**: Honeycomb radar visualizer — self node, scanning pulse, connected nodes, neighbor table, learned routes
- **ChatView**: Text messaging with hop count indicators (direct vs relayed), unread counts, connection status
- **SettingsView**: User display name and device type configuration (phone, tablet, emergency, wearable)

