from app.yolo_loader import model
from app.prediction import predict_species

from PIL import Image
from pathlib import Path

import tempfile
import os
import cv2

print("NEW YOLO DETECTION FILE LOADED")

ANNOTATED_FOLDER = "uploads/annotated"
os.makedirs(ANNOTATED_FOLDER, exist_ok=True)


def detect_animals(image_path):

    image = Image.open(image_path)

    opencv_image = cv2.imread(str(image_path))

    results = model.predict(
        source=str(image_path),
        conf=0.4,
        verbose=False
    )

    detections = []

    for result in results:

        for box in result.boxes:

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            print(f"Bounding Box: {x1}, {y1}, {x2}, {y2}")

            # Crop detected animal
            crop = image.crop((x1, y1, x2, y2))

            # Save crop temporarily
            with tempfile.NamedTemporaryFile(
                    suffix=".jpg",
                    delete=False) as temp:

                crop.save(temp.name)

                print("Calling MobileNet...")

                prediction = predict_species(temp.name)

                print(prediction)

            label = f"{prediction['species']} {prediction['confidence']:.1f}%"

            # Draw Bounding Box
            cv2.rectangle(
                opencv_image,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            # Draw Label Background
            cv2.rectangle(
                opencv_image,
                (x1, max(0, y1 - 30)),
                (x1 + 220, y1),
                (0, 255, 0),
                -1
            )

            # Draw Species Name
            cv2.putText(
                opencv_image,
                label,
                (x1 + 5, max(20, y1 - 8)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 0),
                2
            )

            detections.append({

                "species": prediction["species"],

                "confidence": prediction["confidence"],

                "boundingBox": [x1, y1, x2, y2]

            })

    output_path = Path(ANNOTATED_FOLDER) / f"annotated_{Path(image_path).name}"

    cv2.imwrite(str(output_path), opencv_image)

    return {

        "animalCount": len(detections),

        "annotatedImage": str(output_path),

        "detections": detections

    }