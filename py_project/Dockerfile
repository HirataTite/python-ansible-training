FROM alpine:3.4

# We copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt /app/requirements.txt

WORKDIR /app

# RUN pip install -r requirements.txt
RUN apk --no-cache add python python3 \
                       python-dev python3-dev \
                       py-pip \
                       && pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]