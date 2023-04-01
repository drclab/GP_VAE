import os
import gradio as gr

def text_length(text):
    return len(text)

iface = gr.Interface(fn=text_length, inputs='text', outputs='text')

iface.launch()
