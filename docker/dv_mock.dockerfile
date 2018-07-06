FROM alpine:3.6
RUN apk update; apk add python3 py-virtualenv curl
RUN mkdir -p /opt/dv-mock
COPY ./mocks /opt/dv-mock
WORKDIR /opt/dv-mock
RUN pip install -r requirements.txt
EXPOSE 8080
HEALTHCHECK CMD curl --fail http://localhost:8080/ || exit 1
CMD ["/opt/dv-mock/dev_dv.sh"]
