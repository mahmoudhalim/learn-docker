# Docker Labs

<!--toc:start-->

- [Docker Labs](#docker-labs)
  - [Lab 01](#lab-01)
    - [Problem 01](#lab-01-problem-01)
    - [Problem 02](#lab-01-problem-02)
    - [Problem 03](#lab-01-problem-03)
    - [Problem 04](#lab-01-problem-04)
    - [Problem 05](#lab-01-problem-05)
  - [Lab 02](#lab-02)
    - [Problem 01](#lab-02-problem-01)
    - [Problem 02](#lab-02-problem-02)
    <!--toc:end-->

## Lab 01

<a id="lab-01"></a>
<a id="lab-01-problem-01"></a>

### Problem 01

- run hello world container  
  ![1-1](assets/1-1.png)

- check container status  
  ![1-2](assets/1-stat.png)

- start container  
  ![1-3](assets/1-3.png)

- delete the container and the image  
  ![1-4](assets/1-4.png)

<a id="lab-01-problem-02"></a>

### Problem 02

- run ubuntu container  
  ![2-1](assets/2-1.png)

- echo docker and create hello docker file  
  ![2-2](assets/2-2.png)

- removing the container will delete all its files including hello-docker  
  ![2-3](assets/2026-03-06-10-14-33.png)

<a id="lab-01-problem-03"></a>

### Problem 03

- deploy mysql

![mysql](assets/2026-03-06-10-33-08.png)

<a id="lab-01-problem-04"></a>

### Problem 04

- run nginx  
  ![4-1](assets/4-1.png)

- add html static

  ![4-2](assets/2026-03-06-10-30-24.png)

- now nginx serve my app  
  ![4-3](assets/4-3.png)

- commit the container to create a new image from it and push the new image to dockerhub  
  ![4-4](assets/4-4.png)

<a id="lab-01-problem-05"></a>

### Problem 05

- Single stage

```Dockerfile
FROM python:3.10.20
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt
COPY hello.py .
EXPOSE 5000
CMD ["python", "hello.py"]
```

- multistage

```Dockerfile
FROM python:3.10.20 AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.10.20-slim
WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY hello.py .

ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000
CMD ["python", "hello.py"]
```

- build both containers and run them
  ![single](assets/2026-03-06-15-47-25.png)
  ![multi](assets/multi.png)

- notice the size difference
  ![diff](assets/2026-03-06-15-47-06.png)

- rename the image and push it
  ![5-3](assets/5-3.png)

## Lab 02

<a id="lab-02"></a>
<a id="lab-02-problem-01"></a>

### Problem 01

- create 2 volumes
  ![vol](assets/vol.png)

- create nginx container
  ![nginx](assets/nginx.png)

- edit html content
  ![html](assets/2026-03-06-15-21-13.png)

- remove the container

  ![rm](assets/2026-03-06-15-22-46.png)

- create another two nginx containers and test if the html files persist
  ![persist](assets/2026-03-06-15-25-44.png)

<a id="lab-02-problem-02"></a>

### Problem 02

- create nginx container with binding volume
  ![bind](assets/2026-03-06-15-33-18.png)

- removing the container and creating a new one will not remove the files
  ![new](assets/2026-03-06-15-35-45.png)

## Lab 03

### Problem 03

- create nginx container on network 1
  ![net](assets/2026-03-08-22-13-08.png)
- create flask app on network 1 and network 2
  ![flask](assets/2026-03-08-22-14-34.png)
- run mariadb in network 2
  ![mariadb](assets/2026-03-08-22-18-14.png)
- since nginx and flask app in the same network the can ping each other using container name
  ![ping](assets/2026-03-08-22-20-26.png)

