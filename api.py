import logging
from typing import List
from fastapi import FastAPI, UploadFile
from fastapi.responses import HTMLResponse
from profiler import profile

TMP_FILES_DIR = './tmp_files'
PROFILE_RESULT_DIR = './profile_results'

app = FastAPI()
logger = logging.getLogger(__name__)

@app.get("/", response_class = HTMLResponse)
def index():
    f = open(f'frontend/index.html', "r")
    return f.read()

@app.get("/results/{result_id}", response_class = HTMLResponse)
def read_results(result_id: str):
    f = open(f'{PROFILE_RESULT_DIR}/{result_id}', "r")
    return f.read()

@app.post("/profile/")
def profile_file(files: List[UploadFile]):
    profile_id = profile_file(files[0])
    return {'profile_id': profile_id}

def profile_file(input_file):
    file_path = f'{TMP_FILES_DIR}/{input_file.filename}'

    with open(file_path, 'wb') as f:
        f.write(input_file.file.read())

    result_file = profile(file_path)
    return result_file