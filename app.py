import gradio as gr

from email_generator import generate_email, DEFAULT_GENERATOR


AVAILABLE_MODELS = [
    'pszemraj/opt-350m-email-generation',
    'pszemraj/opt-350m-email-generation',
    'postbot/gpt2-medium-emailgen',
    'sagorsarker/emailgenerator'
]

with gr.Blocks() as app:
    # -- Description.
    gr.Markdown('# Email Generation')
    gr.Markdown("""
        Start an email and let AI do the rest, courtesy of the HuggingFace community!
        AI is supposed to help automate the boring stuff,
        and there's nothing more boring to me than writing generic emails.
        Use this demo to interact with various HuggingFace models for automatic email generation.
        
        Select a model from the dropdown list to use a specific pretrained model,
        or leave it unchanged to default to [pszemraj/opt-350m-email-generation](https://huggingface.co/pszemraj/opt-350m-email-generation).
        
        Then you just have to begin your email and click 'Generate Email' to complete it automatically!
        """
    )
    gr.Image('emails/images/bored.jpg', label='Credit: https://unsplash.com/@thomascpark')

    # -- Model parameters.
    with gr.Row():
        model_tag = gr.Dropdown(
            choices=AVAILABLE_MODELS,
            label='Choose a HuggingFace model',
            value=DEFAULT_GENERATOR
        )
        max_tokens = gr.Slider(10, 200, value=64, label='Max Tokens')
    
    # -- Prompt.
    with gr.Row():
        with gr.Column():
            prompt = gr.Textbox(
                lines=4,
                label='',
                placeholder='Begin your email here...'
            )
            generate_button = gr.Button('Generate Email', variant='primary')

    # -- Output.
    with gr.Row():
        output = gr.Textbox(lines=8, label='Output', interactive=False)

    # -- Button actions.
    generate_button.click(fn=generate_email, inputs=[model_tag, prompt, max_tokens], outputs=output)

app.launch()
