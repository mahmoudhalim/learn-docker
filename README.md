# Docker Lab-01

## Problem 01

- run hello world container
  ![1-1](assets/1-1.png)

- check container status
  ![1-2](assets/1-stat.png)

- start container
  ![1-3](assets/1-3.png)

- delete the container and the image
  ![1-4](assets/1-4.png)

## Problem 02

- run ubuntu container
  ![2-1](assets/2-1.png)

- echo docker and create hello docker file
  ![2-2](assets/2-2.png)

- removing the container will delete all its files including hello-docker
  ![2-3](assets/2026-03-06-10-14-33.png)

## Problem 03

- deploy mysql

![mysql](assets/2026-03-06-10-33-08.png)

## Problem 04

- run nginx
  ![4-1](assets/4-1.png)

- add html static

![4-2](assets/2026-03-06-10-30-24.png)

- now nginx serve my app
  ![4-3](assets/4-3.png)

- commit the container to create a new image from it and push the new image to dockerhub
  ![4-4](assets/4-4.png)

## Problem 05

```Docker
FROM python:3.10.20-alpine3.22

COPY hello.py .

CMD ["python", "hello.py"]
```

- build the container and run
  ![5-2](assets/5-2.png)

- rename the image and push it
  ![5-3](assets/5-3.png)
