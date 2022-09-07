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
   
Docker basic commands
--------------------

- installation
  
  https://docs.docker.com/engine/install/
  
- Pulling an image or a repository from a registry

  `$ docker pull jupyter/base-notebook:latest`
  
- Running a command in a new container (with iteractive that takes inside the container) and also detach it

  <pre><p>
  $ docker run --new_container_name test -itd image_name
  $ docker run --simple_deploy_container -itd base_notebook #example
  </p></pre>
  
  
- List containers (not the running containers)

  `$ docker ps`
  
- Delete all containers installed

  <pre><p>
  $ sudo docker kill $(sudo docker ps -q)
  $ sudo docker rm $(sudo docker ps -a -q)
  </p></pre>
  
- List images

  `docker images -a`
  
- Remove Image(s)

  <pre><p>
  $ docker rmi [image name] #deleting one Image
  $ sudo docker rmi $(sudo docker images -a -q) #deleting all Images
  </p></pre>
 
- Rename Image

  <pre><p>
  $ sudo docker tag [image ID] [new image name]
  $ docker run tag 6b5af5e76c4d base-notebook #example
  </p></pre>
  
Docker common concepts
-----------

- Container vs. Image

  Container: is a running environment for Image
