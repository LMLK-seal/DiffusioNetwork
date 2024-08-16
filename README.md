<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DiffusioNetwork</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1, h2 {
            color: #2c3e50;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <h1>DiffusioNetwork</h1>

    <p>DiffusioNetwork is a Python application that provides a user-friendly interface for generating images using various Stable Diffusion models. It allows users to input prompts, select different models, and adjust various parameters to create unique images.</p>

    <h2>Features</h2>
    <ul>
        <li>Select from multiple pre-trained Stable Diffusion models</li>
        <li>Input custom prompts for image generation</li>
        <li>Adjust advanced settings such as image dimensions, number of inference steps, and seed</li>
        <li>Option for randomized or fixed seed generation</li>
        <li>Real-time image display</li>
        <li>Save generated images in various formats</li>
    </ul>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.7+</li>
        <li>PyQt5</li>
        <li>Pillow</li>
        <li>NumPy</li>
        <li>diffusers</li>
        <li>torch (with CUDA support for GPU acceleration)</li>
    </ul>

    <h2>Installation</h2>
    <ol>
        <li>Download the <code>DiffusioNetwork.py</code> file from this repository.</li>
        <li>Install the required packages:
            <pre><code>pip install PyQt5 Pillow numpy diffusers torch torchvision torchaudio</code></pre>
            <p>Note: For GPU support, make sure to install the appropriate version of PyTorch for your CUDA version. Visit <a href="https://pytorch.org/">https://pytorch.org/</a> for installation instructions.</p>
        </li>
    </ol>

    <h2>Usage</h2>
    <ol>
        <li>Run the application:
            <pre><code>python DiffusioNetwork.py</code></pre>
        </li>
        <li>Select a Stable Diffusion model from the dropdown menu.</li>
        <li>Enter your prompt in the text box.</li>
        <li>(Optional) Adjust advanced settings:
            <ul>
                <li>Set a specific seed or use randomized generation</li>
                <li>Adjust image width and height</li>
                <li>Set the number of inference steps</li>
            </ul>
        </li>
        <li>Click the "Generate Image" button to create your image.</li>
        <li>Once the image is generated, you can save it using the "Save Image" button.</li>
    </ol>

    <h2>Note on Safety</h2>
    <p>This application disables the safety checker in the Stable Diffusion pipeline. Users should be aware that this may result in the generation of unsafe or inappropriate content. Use responsibly.</p>

    <h2>Contributing</h2>
    <p>Contributions are welcome! Please feel free to submit a Pull Request.</p>

    <h2>License</h2>
    <p><a href="LICENSE">MIT License</a></p>

    <h2>Disclaimer</h2>
    <p>This project is for educational purposes only. Users are responsible for ensuring they have the right to use the selected models and for any content generated using this tool.</p>
</body>
</html>
