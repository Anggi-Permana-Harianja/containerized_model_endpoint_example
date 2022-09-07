FROM jupyter/base-notebook
RUN mkdir -p /home/jovyan/work/simple_containerized_model
COPY ./requirements.txt /home/jovyan/work/simple_containerized_model/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /home/jovyan/work/simple_containerized_model/requirements.txt
COPY . /home/jovyan/work/simple_containerized_model
WORKDIR /home/jovyan/work/simple_containerized_model/
CMD ["uvicorn", "endpoint.main:app", "--host", "0.0.0.0", "--port", "80"]