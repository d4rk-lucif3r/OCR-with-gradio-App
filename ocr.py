import pytesseract
def ocr(image):
    '''
    Args:
        image: PIL Image
    Returns:
        string: text in the image
    '''
    custom_config = r'--oem 1 --psm 3 ' #setting the OCR engine to LSTM and the page segmentation mode to auto
    return pytesseract.image_to_string(image, config=custom_config)
