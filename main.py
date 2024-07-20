from fastapi import FastAPI

# >uvicorn main:app --reload  # for automate reload after change in code


app = FastAPI()

@app.get("/home")
def get_hello():
    return "Hello Api!!!"




if __name__ == '__main__':

    pass