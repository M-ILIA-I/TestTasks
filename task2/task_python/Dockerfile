FROM python

COPY . .

EXPOSE 8000

RUN pip install --no-cache-dir -r requirments.txt

CMD ["source", "venv/bin/activate"]

CMD ["python3", "./notes_app/main.py"]