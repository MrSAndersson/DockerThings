FROM python

RUN pip install Flask

WORKDIR /app
ENV FLASK_APP app.py

COPY . .

ENTRYPOINT [ "flask", "run" , "--host=0.0.0.0" ]