from fastapi import FastAPI, Request, Response
from header_injection import HeaderInjection

app = FastAPI()
HeaderInjection(app)

