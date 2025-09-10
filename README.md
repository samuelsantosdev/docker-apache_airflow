# Hadoop - Airflow - Nifi

### Requirements
Docker version 27.5.1^

### Start the project
```bash
docker compose up -d
```

### Applications

| Application | URL                       | User  | Password                |
|-------------|---------------------------|-------|-------------------------|
| Airflow     | http://127.0.0.1:8080/    | admin | admin                   |
| Nifi        | https://localhost:8443/   | admin | ctsBtRBKHRAx69EqUghvvgEvjnaLjFEB |
| Hadoop RM   | http://localhost:8088     |       |                         |
| NameNode    | http://localhost:9870     |       |                         |
| DataNode 1  | http://localhost:9864     |       |                         |
| DataNode 2  | http://localhost:9865     |       |                         |
| NodeManager1| http://localhost:8042     |       |                         |
| NodeManager2| http://localhost:8043     |       |                         |
| Job History | http://localhost:19888    |       |                         |
