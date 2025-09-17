from fastapi import APIRouter, File, UploadFile

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    # Save file locally or forward to API
    contents = await file.read()
    with open(f"uploaded_{file.filename}", "wb") as f:
        f.write(contents)
    return {"msg": "File uploaded"}