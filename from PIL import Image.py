from PIL import Image

try:
    img = Image.open("Assets/alert_compiler1.png")
    img.show()
except Exception as e:
    print("Error al abrir la imagen:", e)
