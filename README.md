# Containerized simple ML model using FastAPI, Docker
Containerized simple ML model using FastAPI, Docker so could easily deployed

FastAPI basic commands
-----

 - Run the live server with default port
 
   go to `./endpoint/main.py` and then `$ uvicorn main:app --reload` 
   
 - Run with customized port
 
   add these lines of codes in `./endpoint/main.py`
   
   <pre><p>
   if __name__ == '__main__':
            uvicorn.run(app, host='127.0.0.1', port=8000)
    </p></pre>
    
   and then run `python ./endpoint/main.py` instead using command `$ uvicorn main:app --reload`
   
Docker basic commands
--------------------

- installation tutorial
  
  https://docs.docker.com/engine/install/
  
- Pulling an image or a repository from a registry

  `$ docker pull jupyter/base-notebook:latest`
  
- Rename Image

  <pre><p>
  $ sudo docker tag [image ID] [new image name]
  $ docker run tag 6b5af5e76c4d base-notebook #example
  </p></pre>
  
- Running a new container from Image in detach mode

  <pre><p>
  $ docker run -d [image_name]
  $ sudo docker run -d base-notebook:latest #example
  </p></pre>
  
- Rename container

  <pre><p>
  $ docker run --name [new_container_name] [image_name]
  $ sudo docker run --name simple_deployment_container base-notebook #example
  </p></pre>
  
- Running a command in a running container (interactive and pseudo-tty)

  <pre><p>
  $ docker exec [options] [container_id or container_name] [command]
  $ docker exec it simple_deployment_container /bin/bash
  </p></pre>
  
- List containers (not the running containers)

  `$ docker ps`
  
- Stop running container

  `$ docker stop [container_id]`
  
- Kill running container

  <pre><p>
  $ docker kill [container_id] #one container
  $ sudo docker rm $(sudo docker ps -a -q) #kill all containers
  </p></pre>
  
- Delete all container(s) installed

  <pre><p>
  $ docker rm [container_id] #delete one container
  $ sudo docker rm $(sudo docker ps -a -q) #delete all containers
  </p></pre>
  
- Binding port

  <pre><p>
  $ docker run -p[host_port]:[container_port] [image_name]
  $ docker run -p8890:8888 base-notebook
  </p></pre>
  
- List images

  `$ docker images -a`
  
- Remove Image(s)

  <pre><p>
  $ docker rmi [image name] #deleting one Image
  $ sudo docker rmi $(sudo docker images -a -q) #deleting all Images
  </p></pre>
  
Docker compose command
--------

- Installation tutorial

  https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04
  
- Running docker-compose with YAML file

  https://docs.docker.com/engine/reference/commandline/compose_run/

  `$ docker compose-compose -f [yaml_file] up`
  
Docker common concepts
-----------

- Container vs. Image

  Container: is a running environment for Image
  
- Container port vs. Host port

  We can bind port between container and host to prevent mis-allocation of port, for example we can bind port 8000 from container with port 8001 from host so that we can open jupyter-notebook container in host machine using port 8001 instead 8000
  
- Docker compose

  Sometimes we need to have multiple Images(s) and containers running, this could be done by using Docker compose, Docker compose use YAML file format to arrange/list all necessary docker command for each containers so that we only need to build it using one liner code, as for example below:
  
  <pre><p>
  version: 3 #docker compose version
  services:
      mongodb: #container name
          image: mongo #first Image
          ports:
           - 2701:2701
          environments: #see the docker repository for mongodb to see environment for this Image
           - MONGO_INITDB_ROOT_USERNAME=admin
           - MONGO_INITDB_ROOT_PASSWORD=password
      mongo-express: #second contaniner name
          image: mongo-express #second Image
          ports:
           - 8080:8081
          environments:
           - ME_CONFIG_MONGODB_ADMINUSERNAME=admin #see the docker repository for mongo-express to see environment for this Image
           - ME_CONFIG_MONGODB_ADMINPASSWORD=password
  </p></pre>
