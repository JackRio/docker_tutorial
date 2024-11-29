# Docker Commands  

## First check your docker installation

`docker run hello-world`

- docker build -t ml_model -f Dockerfile .
- docker build -t ml_model -f Dockerfile . --no-cache
- docker run ml_model
- docker run -d ml_model
- docker run -d -p 8881:8001 ml_model
- docker run -d -v /home/sanyog/docker/machine_learning/model_weights:/app/model_weights -p 8881:8001 ml_model
- docker exec -it <container-id> sh

# Additional Commands
- docker logs <container_id>
- docker stop <container_id>


# Docker base/slim/alpine

## Admin Commands
- sudo systemctl start docker