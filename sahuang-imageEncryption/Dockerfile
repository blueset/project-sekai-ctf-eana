FROM python:3.9-slim-buster
WORKDIR /app
RUN pip3 install flask requests pillow
COPY . .
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8000"]
# docker build --tag project-sekai-ctf-image-encryption .
# docker run -d --publish 36277:8000 --name project-sekai-ctf-image-encryption project-sekai-ctf-image-encryption