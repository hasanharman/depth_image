import os
import uuid

from fastapi import FastAPI, File, UploadFile

from predictor import DepthEstimationModel

app = FastAPI()
depth_estimator = DepthEstimationModel()

ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}
TEMP_FOLDER = "api_images"
os.makedirs(TEMP_FOLDER, exist_ok=True)


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        file_ext = os.path.splitext(file.filename)[1]
        if file_ext not in ALLOWED_EXTENSIONS:
            return {"error": "Unsupported file extension."}

        filename_base = str(uuid.uuid4())
        filename = filename_base + file_ext
        destination_path = os.path.join(TEMP_FOLDER, filename)
        output_path = os.path.join(TEMP_FOLDER, "output" + filename_base + ".png")

        with open(destination_path, "wb") as image_data:
            image_data.write(await file.read())

        depth_estimator.calculate_depthmap(destination_path, output_path)
        return {"Ok": "Image processed successfully."}

    except Exception as e:
        return {"error": str(e)}
