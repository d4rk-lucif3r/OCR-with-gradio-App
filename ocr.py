import easyocr
import logging


def ocr(image):
    '''
    Args:
        image: PIL Image
    Returns:
        string: text in the image
    '''
    custom_config = r'--oem 1 --psm 3 ' #setting the OCR engine to Default and the page segmentation mode to auto
    try:
        reader = easyocr.Reader(['en'], gpu=False, model_storage_directory='.', download_enabled=True)
        string = reader.readtext(image, detail=0)
        print(string)
        logging.info(string)
    except Exception as e:
        print(e)
        logging.error(e)
        string = None
    return string
