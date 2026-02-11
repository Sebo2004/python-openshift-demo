FROM registry.access.redhat.com/ubi9/ubi-minimal

RUN microdnf install -y python3 python3-pip && \
    microdnf clean all

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app.py .

USER 1001

EXPOSE 8080

CMD ["python3", "app.py"]
