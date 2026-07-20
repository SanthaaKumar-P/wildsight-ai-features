from app.yolo_loader import model
from app.prediction import predict_species
from app.animal_identifier import identify_animal
from PIL import Image
from pathlib import Path
import tempfile
import os
import cv2


print("NEW YOLO DETECTION FILE LOADED")


ANNOTATED_FOLDER = "uploads/annotated"

os.makedirs(
    ANNOTATED_FOLDER,
    exist_ok=True
)


def detect_animals(image_path):

    image = Image.open(image_path).convert("RGB")

    opencv_image = cv2.imread(
        str(image_path)
    )


    results = model.predict(
        source=str(image_path),
        conf=0.4,
        verbose=False
    )


    detections = []


    for result in results:

        for box in result.boxes:


            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )


            print(
                f"Bounding Box: {x1}, {y1}, {x2}, {y2}"
            )


            # Crop detected animal

            crop = image.crop(
                (
                    x1,
                    y1,
                    x2,
                    y2
                )
            )


            temp_path = None


            try:

                with tempfile.NamedTemporaryFile(
                    suffix=".jpg",
                    delete=False
                ) as temp:

                    temp_path = temp.name


                crop.save(
                    temp_path
                )


                print(
                    "Calling MobileNet..."
                )


                prediction = predict_species(
                    temp_path
                )

                animal_identity = identify_animal(
    temp_path,
    prediction["species"]
)

                print("Animal Identity:")
                print(animal_identity)
                print(
                    prediction
                )


            finally:

                if temp_path and os.path.exists(temp_path):

                    try:

                        os.remove(
                            temp_path
                        )

                    except PermissionError:

                        pass



            confidence = prediction["confidence"]


            label = (
    f"{prediction['species']} "
    f"{confidence:.1f}% "
    f"{animal_identity['animalId']}"
)



            # Draw bounding box

            cv2.rectangle(

                opencv_image,

                (x1, y1),

                (x2, y2),

                (0,255,0),

                2

            )



            # Label background

            cv2.rectangle(

                opencv_image,

                (x1, max(y1-35,0)),

                (x1+250, y1),

                (0,255,0),

                -1

            )



            # Label text

            cv2.putText(

                opencv_image,

                label,

                (x1+5, max(y1-10,20)),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.7,

                (0,0,0),

                2

            )



        


    detections.append({

    "species": prediction["species"],

    "confidence": confidence,

    "boundingBox":[
        x1,
        y1,
        x2,
        y2
    ],

    "animalId":
    animal_identity["animalId"],

    "existingAnimal":
    animal_identity["existingAnimal"],

    "similarity":
    animal_identity["similarity"]

})

            



    # Save annotated image

    output_file = (
        f"annotated_"
        f"{Path(image_path).name}"
    )


    output_path = Path(
        ANNOTATED_FOLDER
    ) / output_file



    cv2.imwrite(

        str(output_path),

        opencv_image

    )



    return {


        "animalCount":
        len(detections),



        "annotatedImage":
        f"http://127.0.0.1:8000/uploads/annotated/{output_file}",



        "detections":
        detections,


        "model":
        "YOLO + MobileNetV2"

    }