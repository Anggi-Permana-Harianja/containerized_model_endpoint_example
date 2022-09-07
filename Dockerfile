FROM jupyter/base-notebook
RUN mkdir -p /home/jovyan/work/simple_containerized_model
COPY . /home/jovyan/work/simple_containerized_model
CMD ["/home/jovyan/work/simple_containerized_model/docker_build.sh"]