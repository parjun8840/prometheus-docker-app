FROM alpine:3.7
MAINTAINER "Arjun Pandey"
LABEL description="This could be used for Blue/Green deployment. \
Just pass the environment vairable SERVICE_NAME as Blue/Green."
RUN apk update && apk add python3 bash jq ca-certificates curl net-tools
RUN pip3 install --upgrade pip
RUN python3 --version && pip3 --version
RUN pip3 install -q requests==2.21.0  prometheus-client
RUN mkdir /code
ADD ./service.py /code
ADD ./entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod u+x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["python3","/code/service.py"]
