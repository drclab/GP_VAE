import os
import gradio as gr
from toolbox import format_io, find_free_port

def text_length(text):
    return len(text)

iface = gr.Interface(fn=text_length, inputs='text', outputs='text')

iface.launch()
