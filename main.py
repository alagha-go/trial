from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def Trial ():
	return ("Hello World")
