import json
import os
import requests

import gradio as gr

# Load test cases
testcases = os.listdir("testcases")

# Load test case contents with proper file handling
testcase_contents = {}
for name in testcases:
    with open(f"testcases/{name}", "r", encoding="utf-8") as f:
        testcase_contents[name] = json.load(f)

def send_request(json_body:dict) -> dict:
    # Display the content of the selected testcase immediately
    content = json.dumps(json_body)

    # Send a request to the FastAPI server
    url = f"http://localhost:80/v1/generate"
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(url, headers=headers, data=content)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        # handle error and return early
        return {"error": str(e)}

    # Return the original content and the response from the server
    return response.json()

def example_case(testcase_name):
    content = testcase_contents[testcase_name]
    return content, send_request(content)

def input_case(title, content):
    # Display the content of the selected testcase immediately
    return send_request({"title": title, "content": content})

with gr.Blocks() as testing_iface:
    gr.Markdown("To test GPT worker.")
    with gr.Tab("Input Examples"):
        testcase_dropdown = gr.Dropdown(choices=testcases, label="Test Cases")
        with gr.Row():
            testcase_content = gr.JSON(label="Test Case Content")
            server_response = gr.JSON(label="Server Response")
        run_example_button = gr.Button("Generate")
    with gr.Tab("Input Text"):
        title_input = gr.Textbox(label="Title")
        content_input = gr.TextArea(label="Content")
        run_text_button = gr.Button("Generate")
        text_response = gr.JSON(label="Server Response")

    run_example_button.click(fn=example_case, inputs=[testcase_dropdown], outputs=[testcase_content, server_response])
    run_text_button.click(fn=input_case, inputs=[title_input, content_input], outputs=[text_response])


if __name__ == "__main__":
    testing_iface.launch(share=True, server_name="0.0.0.0")
