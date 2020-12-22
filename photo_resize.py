import cv2

input_image = input("Enter image path: ")
img = cv2.imread(input_image)
if img is None:
	print("No image found.")
	exit()
print(f"Input image's width and height: {img.shape[1], img.shape[0]}")
desired_width = input("Enter desired width in pixel: ")
desired_height = input("Enter desired height in pixel: ")
img2 = cv2.resize(img,(int(desired_width), int(desired_height)))
cv2.imshow("output (Press ESC to exit program)", img2)
if cv2.waitKey(0) == 27:
    exit()
