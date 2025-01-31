from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Allow all origins (you can replace '*' with specific domains if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ['http://localhost:8081']
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
async def root():
    return {"message": "Hello Airbills Agent"}