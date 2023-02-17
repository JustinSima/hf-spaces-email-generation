""" Functions for loading email generator."""
import transformers


DEFAULT_GENERATOR = 'pszemraj/opt-350m-email-generation'

class EmailGenerator:
    """ Class that loads and wraps a HuggingFace email generation pipeline."""
    def __init__(self, model_tag: str) -> None:
        """ Initialize HuggingFace email generation pipeline.

        Args:
            model_tag (str): Model name.
        """
        self.tag = model_tag
        self.generator = transformers.pipeline(
            'text-generation', model_tag,
            use_fast=True, do_sample=False
        )
        
    def generate(self, prompt: str, max_tokens: int) -> str:
        """ Generate a sample from a given prompt.

        Args:
            prompt (str): Prompting for email generator.
            max_tokens (int): Maximum number of tokens to return.

        Returns:
            str: Generated text.
        """
        output = self.generator(prompt, max_length=max_tokens)
        return output[0]['generated_text']
    
    def __str__(self):
        return f'EmailGenerator({self.tag})'

def set_global_generator(model_tag: str=DEFAULT_GENERATOR):
    """ Set global parameter 'generator' as specified EmailGenerator."""
    global generator
    generator = EmailGenerator(model_tag=model_tag)
        
def generator_exists():
    """ Check if global variable 'generator' has been defined."""
    return 'generator' in globals()

def generate_email(model_tag: str, prompt: str, max_tokens: int):
    """ Check for generator and create prompt.
    Initialize correct generator if incorrect generator or no generator is found.
    """
    if not generator_exists() or generator.tag != model_tag:
        set_global_generator(model_tag=model_tag)
    
    return generator.generate(prompt, max_tokens=max_tokens)
