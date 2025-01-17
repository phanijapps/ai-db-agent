import os
from smolagents import LiteLLMModel, TransformersModel

class ModelType:
    OPENAI = "openai"
    OLLAMA = "ollama"
    TRANSFORMERS = "transformers"

MODEL_FACTORY = {
    ModelType.OPENAI: lambda model_id: LiteLLMModel(model_id),
    ModelType.OLLAMA: lambda model_id: LiteLLMModel(
        model_id=model_id,
        api_base= os.getenv("OLLAMA_BASE_URL")
    ),
    ModelType.TRANSFORMERS: lambda model_id: TransformersModel(model_id=model_id)
}

def get_model(model_type, model_id):
    """Returns the appropriate model instance based on the given type and model ID."""
    print(f"{model_type} - {model_id}")
    model_creator = MODEL_FACTORY.get(model_type)
    print(model_creator)
    if not model_creator:
        raise ValueError(f"Unsupported model type: {model_type}")
    return model_creator(model_id)

# Example usage:
# model = get_model(ModelType.OPENAI, "gpt-4o")
# model = get_model(ModelType.OLLAMA, "ollama_chat/llama3.2")
# model = get_model(ModelType.TRANSFORMERS, "meta-llama/Llama-3.2-3B-Instruct")