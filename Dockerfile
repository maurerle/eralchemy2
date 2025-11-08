FROM python:3.12.4-slim

RUN apt update && apt install --no-install-recommends -y build-essential gcc graphviz libgraphviz-dev libpq-dev \
&& pip3 install mysql-connector-python psycopg2 sqlalchemy pygraphviz eralchemy2 \
&& apt-get purge -y build-essential libgraphviz-dev gcc \
&& apt-get autoremove -y \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

CMD ["eralchemy2", "-h"]
