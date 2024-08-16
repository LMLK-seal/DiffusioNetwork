# DiffusioNetwork (100% Private-Offline image generator)

![LLModel Chat Demo](https://github.com/LMLK-seal/DiffusioNetwork/blob/main/Animation.gif?raw=true)

DiffusioNetwork is a Python application that provides a user-friendly interface for generating images using various Stable Diffusion models. It allows users to input prompts, select different models, and adjust various parameters to create unique images.

Important Note: DiffusioNetwork is designed to be 100% offline and private once set up. However, it requires an initial download of the chosen Stable Diffusion model.   After this initial download, the application operates entirely on your local machine, ensuring your prompts and generated images remain private and secure.

## Features

- Select from multiple pre-trained Stable Diffusion models
- Input custom prompts for image generation
- Adjust advanced settings such as image dimensions, number of inference steps, and seed
- Option for randomized or fixed seed generation
- Real-time image display
- Save generated images in various formats

## Requirements

- Python 3.7+
- PyQt5
- Pillow
- NumPy
- diffusers
- torch (with CUDA support for GPU acceleration)

## Installation

1. Download the `DiffusioNetwork.py` file from this repository.

2. Install the required packages:
   ```
   pip install PyQt5 Pillow numpy diffusers torch torchvision torchaudio
   ```

   Note: For GPU support, make sure to install the appropriate version of PyTorch for your CUDA version. Visit https://pytorch.org/ for installation instructions.
   

## Usage

1. Run the application:
   ```
   python DiffusioNetwork.py
   ```

2. Select a Stable Diffusion model from the dropdown menu.

3. Enter your prompt in the text box.

4. (Optional) Adjust advanced settings:
   - Set a specific seed or use randomized generation
   - Adjust image width and height
   - Set the number of inference steps

5. Click the "Generate Image" button to create your image.

6. Once the image is generated, you can save it using the "Save Image" button.

## Note on Safety

This application disables the safety checker in the Stable Diffusion pipeline. Users should be aware that this may result in the generation of unsafe or inappropriate content. Use responsibly.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[MIT License](LICENSE)

## Disclaimer

This project is for educational purposes only. Users are responsible for ensuring they have the right to use the selected models and for any content generated using this tool.
