import gradio as gr
from ocr import ocr

#Here we are going to use Gradio Blocks
demo = gr.Blocks()

with demo:

    gr.Markdown("# OCR Demo")

    with gr.Tabs():
        with gr.TabItem("Examples"):  # Example Tab where we will have 2 images
            with gr.Row():
                rad = gr.components.Radio(
                    ['Example 1', 'Example 2'], label='Select Video and wait till it appears!')
                img1 = gr.components.Image()
                web_bt1 = gr.Button('Submit')

        with gr.TabItem("Upload"):  # Upload Tab where we can upload any image
            with gr.Row():
                img2 = gr.components.Image(source='upload')
            web_bt2 = gr.Button('Submit')

    def action(choice):
        '''function for radio component'''
        if choice == 'Example 1':
            return 'test-images/receipt-1.jpeg'
        elif choice == 'Example 2':
            return 'test-images/receipt-2.jpeg'

    rad.change(action, rad, img1)

    op = gr.components.Textbox(label='Output')

    def fn(img):
        string = ocr(img)
        return string

    web_bt2.click(fn, inputs=[img2], outputs=op)
    web_bt1.click(fn, inputs=[img1], outputs=op)

try:
    demo.launch(inline=False, server_name="0.0.0.0",
                server_port=8080, max_threads=100)
except Exception as e:
    print(e)
    pass
