FROM python:3.8.12


WORKDIR /app

RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list \
    && sed -i 's/security.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list \
    && apt-get update

COPY source/requirements.txt .
COPY fffffffffllllllllll4444444gggggg /etc/fffffffffllllllllll4444444gggggg
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY source .

CMD python3 app.py
