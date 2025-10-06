# WNBA Stats Chatbot

Practice project: WNBA stats chatbot running on AWS.

## Project Flow Diagram

::: mermaid
graph TD
  subgraph Data_Ingestion["Data Ingestion"]
    A1[🌐 REST API Request] --> A2[💾 Save to AWS S3]
  end

  subgraph Data_Processing["Data Processing"]
    B1[🐍 Python Script on EC2 VM] --> B2[⚙️ Calculate Advanced Stats]
  end

  subgraph Chatbot_Interaction["Chatbot Interaction"]
    C1[🤖 Feed Stats to Chatbot AWS Lex?] --> C2[👤 User Q&A with Chatbot]
  end

  A2 --> B1
  B2 --> C1

  %% Styling
  classDef ingestion fill:#d0f0fd,stroke:#007acc,stroke-width:2px,color:#003366,font-weight:bold;
  classDef processing fill:#d0f7d9,stroke:#28a745,stroke-width:2px,color:#155724,font-weight:bold;
  classDef chatbot fill:#fddede,stroke:#dc3545,stroke-width:2px,color:#721c24,font-weight:bold;

  class Data_Ingestion ingestion;
  class Data_Processing processing;
  class Chatbot_Interaction chatbot;
:::

## Data Tables

### Players

* Player details
* Player game logs

### Teams

* Team details
* Team game logs

### Games

* Boxscores
* Player rotations
* Play-By-Play data
* Shot chart data

::: mermaid

---
title: Data Flow
---
graph TD

API[(WNBA Stats API)]
PL[Player List]
PGL[Player Game Log]
TL[Team List]
TGL[Team Game Log]
S3[(AWS S3)]
USR((End User))
LEX[AWS Lex]
PIDL(player_ids)
TIDL(team_ids)

API -- request --> PL
API -- request --> TL

PIDL --> PGL
API -- request --> PGL
API --> TGL
PL -- player_id --> PIDL
TL -- team_id --> TIDL
S3 <--> LEX <--> USR


:::
