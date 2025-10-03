# WNBA Stats Chatbot

Practice project: WNBA stats chatbot running on AWS.

::: mermaid

---
title: Data Flow

---
graph TD;
    A[(WNBA Stats\nAPI)]-->B(AWS VM);
    B-->D(Chatbot);
    C[(AWS\nStorage)]-->B;
    D-->E(User)
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
