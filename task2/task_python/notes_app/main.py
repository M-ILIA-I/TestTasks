import uvicorn
from database.db import url
from database.db import engine

if __name__ == "__main__":
  uvicorn.run("api.my_app:app", host="0.0.0.0", port=8000, reload=True)
  