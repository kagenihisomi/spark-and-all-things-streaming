# Spark and all things streaming
This is a set of notes and examples for working with spark and all things streaming for my own reference. I've tried to connect to as many different streaming systems as possible to understand how they work and how to use them. And also decouple them as much as possible to understand how they work in isolation.
It's for figuring out all things
- Docker
- Kafka
- Spark
- QuestDB
- Locust

## Docker 
I've tried to use docker-compose to create a stack for each of the streaming systems I've tried to use to make it as easy as possible to get started.

To start all services run:
```bash
./stonks up
```

To stop all services run:
```bash
./stonks up
```


## Kafka / Conduktor
- [Kafka](kafka-stack-docker-compose/README.md)

I wanted to use the Conduktor docker-compose stack to test out some of the features of Kafka.

## Spark
I wanted to use the spark docker-compose stack to test out some of the features of Spark. Such as
- Spark Connect
- Spark Strucutured Streaming 
- Spark ODBC

## QuestDB
I wanted to use the QuestDB docker-compose stack to test out some of the features of QuestDB. Especially an interaction between Spark and QuestDB, and how you could "stream" data from Spark to QuestDB.


