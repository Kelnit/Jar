from fastapi import FastAPI

app = FastAPI(title="Python Application")

@app.get("/")
async def MainFile():
  """
  Main File Function
  """
  return {"result":"Main Python Application"}