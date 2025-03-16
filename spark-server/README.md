# Spark Server

This repository contains a Docker-based setup for a Spark cluster, designed for local development

## Getting Started

### Build and Run

```bash
docker-compose up -d
```

## Architecture

```mermaid
flowchart TD
    subgraph "Local Environment"
        jupyter["Jupyter Notebook"]
    end
    
    subgraph "Docker Network"
        connect["Spark Connect Server<br>(UI Port: 4040)"]
        master["Spark Master<br>(UI Port: 8080)"]
        worker1["Spark Worker 1<br>(Internal:8081)"]
        worker2["Spark Worker 2<br>(Internal:8082)"]
        worker3["Spark Worker 3<br>(Internal:8083)"]
    end
    
    jupyter -->|Submit jobs| connect
    connect -->|Coordinate| master
    master -->|Assign tasks| worker1
    master -->|Assign tasks| worker2
    master -->|Assign tasks| worker3
    
    classDef exposed fill:#c9e6ff,stroke:#0073bb,stroke-width:2px
    class jupyter,master,connect exposed
```

The Spark cluster consists of the following components:

- **Jupyter Notebook** - Interactive development environment with PySpark support
- **Spark Connect** - Provides a server for remote Spark clients
- **Spark Master** - Coordinates resource allocation and job scheduling
- **Spark Workers** - Execute the actual computation tasks


You can access these components through your browser:
- **Spark Master UI**: http://localhost:8080
- **Spark Connect UI**: http://localhost:4040

The locally running Jupyter notebook connects to the containerized Spark cluster through the Spark Connect server for job submission and execution.