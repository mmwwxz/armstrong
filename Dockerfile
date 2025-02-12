FROM python:3.10
ENV PYTHONIOENCODING UTF-8
ENV PYTHONUNBUFFERED 1
ENV TZ=ASIA/Bishkek
WORKDIR /app
ENV PATH="/env/bin:$PATH"

COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app/

RUN python manage.py makemigrations && \
    python manage.py migrate && \
    python manage.py collectstatic --noinput \