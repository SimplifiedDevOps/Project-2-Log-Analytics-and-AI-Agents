import os
from sentence_transformers import SentenceTransformer

# Define model name and save path
MODEL_NAME = 'all-MiniLM-L6-v2'
SAVE_PATH = './saved_model'

def download_and_save_model(model_name, save_path):
    """
    Downloads a pre-trained model from sentence-transformers and saves it locally.

    Parameters:
        model_name (str): Name of the model to download.
        save_path (str): Directory where the model will be saved.
    """
    # Full path for the saved model
    full_model_path = os.path.join(save_path, model_name)

    # Check if the model already exists
    if os.path.exists(full_model_path):
        print(f"Model '{model_name}' already downloaded at {full_model_path}.")
    else:
        # Download and save the model
        print(f"Downloading model '{model_name}'...")
        model = SentenceTransformer(model_name)
        model.save(full_model_path)
        print(f"Model '{model_name}' saved at {full_model_path}.")

if __name__ == "__main__":
   
