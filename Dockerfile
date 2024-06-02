FROM ubuntu:24.04

WORKDIR /app/eralchemy2

ENV PATH="/root/.local/bin:${PATH}"

RUN apt-get update && apt-get install -y python3 python3-pip pipx graphviz libgraphviz-dev && pipx install eralchemy2

CMD ["eralchemy2"]
