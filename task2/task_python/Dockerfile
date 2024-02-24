FROM python

ENV HOME=/home/app/web

RUN addgroup --system app && adduser --system app --ingroup app

WORKDIR $HOME

COPY . $HOME

EXPOSE 8000

RUN pip install --no-cache-dir -r requirments.txt

CMD ["source", "venv/bin/activate"]

CMD ["python3", "./notes_app/main.py"]