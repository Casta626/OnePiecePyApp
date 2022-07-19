from configparser import Interpolation
import cv2
import os

input_images_path = "Imagenes"
files_names = os.listdir(input_images_path)

output_images_path = "Imagenes_Galeria"
if not os.path.exists(output_images_path):
    os.mkdir(output_images_path)


for file_name in files_names:
    if file_name.endswith(".jpg"):
    
        image_path = input_images_path + "/" + file_name
        print(image_path)

        image = cv2.imread(image_path)
        if image_path is None:
            continue

        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # image = cv2.resize(image, (640, 480))

        cv2.imwrite(output_images_path + "/" + file_name, image)

    if file_name.endswith(".png"):
    
        image_path = input_images_path + "/" + file_name
        print(image_path)

        image = cv2.imread(image_path)
        if image_path is None:
            continue

        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # image = cv2.resize(image, (640, 480))

        cv2.imwrite(output_images_path + "/" + file_name, image)

    if file_name.endswith(".jpeg"):
    
        image_path = input_images_path + "/" + file_name
        print(image_path)

        image = cv2.imread(image_path)
        if image_path is None:
            continue

        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # image = cv2.resize(image, (640, 480))

        cv2.imwrite(output_images_path + "/" + file_name, image)

'''
        cv2.imshow("Image", image)
        cv2.waitKey(0)
cv2.destroyAllWindows()
'''