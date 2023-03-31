To use Gradio, you can follow these steps:

1. Install Gradio via pip or conda. The recommended way is to install it via pip using the following command: 

   ```
   pip install gradio
   ```

2. Import gradio module in your Python script by adding the following code:

   ```
   import gradio as gr
   ```

3. Define a function that takes inputs and returns outputs. For example, consider a function that takes a text input and returns its length:

   ```
   def text_length(text):
       return len(text)
   ```

4. Create an interface for the function using gradio's `Interface` class:

   ```
   iface = gr.Interface(fn=text_length, inputs="text", outputs="text")
   ```

5. Run the interface using the `launch` method:

   ```
   iface.launch()
   ```

   This will start a local web server and launch the Gradio interface in your browser.

That's it! You can now use Gradio to build and test your machine learning models or any other Python code that can be turned into a function.