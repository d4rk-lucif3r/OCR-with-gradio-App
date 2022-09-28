import pytesseract
def ocr(image):
    '''
    Args:
        image: PIL Image
    Returns:
        string: text in the image
    '''
    custom_config = r'--oem 3 --psm 3 ' #setting the OCR engine to Default and the page segmentation mode to auto
    try:
        string = pytesseract.image_to_string(image, config=custom_config)
        print(string)
    except Exception as e:
        print(e)
        string = None
    return string
