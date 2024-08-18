import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QFileDialog, QTextEdit, QMessageBox, QSlider, QComboBox,
                             QLineEdit, QCheckBox, QGroupBox, QScrollArea)
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QImage
from PyQt5.QtCore import Qt, QRect
from PIL import Image, ImageDraw
import numpy as np
from diffusers import StableDiffusionPipeline, StableDiffusionInpaintPipeline
import torch
import random

class FluxInplant(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('DiffusioNetwork')
        self.setGeometry(100, 100, 800, 600)

        # Main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # Model Selection
        self.model_label = QLabel('Select a model:')
        self.model_combo = QComboBox()
        self.model_combo.addItems([
            'CompVis/stable-diffusion-v1-4',
            'runwayml/stable-diffusion-v1-5',
            'stabilityai/sdxl-turbo',
            'stabilityai/stable-diffusion-x4-upscaler',
            'stabilityai/stable-diffusion-2-1',
            'CompVis/ldm-text2im-large-256',
            'prompthero/openjourney-v4',
            'dreamlike-art/dreamlike-diffusion-1.0',
            'stabilityai/stable-diffusion-2-base',
            'EnD-Diffusers/Virtual_Diffusion_3d_version_one_PDXL'
            
        ])

        # Prompt and Output
        self.prompt_label = QLabel('Enter your prompt:')
        self.prompt_entry = QTextEdit()
        self.prompt_entry.setFixedHeight(60)

        self.result_label = QLabel('')

        # Image Display
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("background-color: #f0f0f0; border: 1px solid #d0d0d0;")

        # Process Button
        self.process_button = QPushButton('Generate Image')
        self.process_button.clicked.connect(self.process_image)
        self.process_button.setStyleSheet("background-color: #f44336; color: white; padding: 10px;")

        # Save Button
        self.save_button = QPushButton('Save Image')
        self.save_button.clicked.connect(self.save_image)
        self.save_button.setStyleSheet("background-color: #008CBA; color: white; padding: 10px;")
        self.save_button.setEnabled(False)  # Disable save button initially

        # Advanced Settings
        advanced_group = QGroupBox("Advanced Settings")
        advanced_layout = QVBoxLayout()

        self.seed_label = QLabel("Seed:")
        self.seed_entry = QLineEdit("0")
        advanced_layout.addWidget(self.seed_label)
        advanced_layout.addWidget(self.seed_entry)

        self.randomized_checkbox = QCheckBox("Randomized")
        self.randomized_checkbox.setChecked(True)
        advanced_layout.addWidget(self.randomized_checkbox)

        self.width_label = QLabel("Width:")
        self.width_entry = QLineEdit("512")
        advanced_layout.addWidget(self.width_label)
        advanced_layout.addWidget(self.width_entry)

        self.height_label = QLabel("Height:")
        self.height_entry = QLineEdit("512")
        advanced_layout.addWidget(self.height_label)
        advanced_layout.addWidget(self.height_entry)

        self.steps_label = QLabel("Number of Inference Steps:")
        self.steps_entry = QLineEdit("20")
        advanced_layout.addWidget(self.steps_label)
        advanced_layout.addWidget(self.steps_entry)

        advanced_group.setLayout(advanced_layout)

        # Create a scroll area to contain the main layout
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)  # Allow the scroll area to resize its content
        scroll_area_widget = QWidget()  # Widget for scroll area content
        scroll_area_layout = QVBoxLayout()  # Layout for scroll area content
        scroll_area_layout.addWidget(self.model_label)
        scroll_area_layout.addWidget(self.model_combo)
        scroll_area_layout.addWidget(self.prompt_label)
        scroll_area_layout.addWidget(self.prompt_entry)
        scroll_area_layout.addWidget(self.process_button)
        scroll_area_layout.addWidget(self.save_button)
        scroll_area_layout.addWidget(self.result_label)
        scroll_area_layout.addWidget(self.image_label)
        scroll_area_layout.addWidget(advanced_group)
        scroll_area_layout.addStretch()
        scroll_area_widget.setLayout(scroll_area_layout)
        scroll_area.setWidget(scroll_area_widget)

        # Layout
        main_layout.addWidget(scroll_area)  # Add the scroll area to the main layout

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def process_image(self):
        prompt = self.prompt_entry.toPlainText().strip()
        if not prompt:
            QMessageBox.warning(self, "Error", "Please provide a prompt.")
            return

        model_name = self.model_combo.currentText()
        seed = int(self.seed_entry.text())
        randomized = self.randomized_checkbox.isChecked()
        width = int(self.width_entry.text())
        height = int(self.height_entry.text())
        steps = int(self.steps_entry.text())

        try:
            # Load the Stable Diffusion model with safety checker disabled
            model = StableDiffusionPipeline.from_pretrained(
                model_name,
                torch_dtype=torch.float16,
                safety_checker=None,  # Disable safety checker
                requires_safety_checker=False  # Disable safety checker requirement
            )
            model = model.to("cuda")

            # Generate image
            generator = torch.Generator(device="cuda")
            if not randomized:  # Only set seed if not randomized
                generator.manual_seed(seed)

            image = model(
                prompt=prompt,
                guidance_scale=7.5,
                num_inference_steps=steps,
                height=height,
                width=width,
                generator=generator
            ).images[0]

            # Display image
            self.display_image(image)

            self.result_label.setText("Image generated successfully.")
            self.save_button.setEnabled(True)  # Enable save button after processing
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to process image: {e}")

    def display_image(self, image):
        # Convert PIL Image to QImage
        img = image.convert("RGBA")
        data = img.tobytes("raw", "RGBA")
        qimage = QImage(data, img.width, img.height, QImage.Format_RGBA8888)

        pixmap = QPixmap.fromImage(qimage)
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(pixmap.width(), pixmap.height())

    def save_image(self):
        if self.image_label.pixmap() is None:
            QMessageBox.warning(self, "Error", "No image generated yet.")
            return

        filepath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "JPEG (*.jpg *.jpeg);;PNG (*.png);;GIF (*.gif);;All files (*.*)")
        if filepath:
            self.image_label.pixmap().save(filepath)
            QMessageBox.information(self, "Success", "Image saved successfully.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FluxInplant()
    ex.show()
    sys.exit(app.exec_())
