import uvicorn
from db.db import url


if __name__ == "__main__":
  print(url)
  uvicorn.run("api.my_app:app", host="0.0.0.0", port=8000, reload=True)
  