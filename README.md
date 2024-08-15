# 🖼️ Image Compressor

## Table of Contents 📚
- [Description](#description)
- [Features](#features-)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Learnings and Skills](#learnings-and-skills)

## Description 📝

This project compresses images to reduce their file size while maintaining an acceptable level of quality. It's perfect for optimizing images for the web or saving storage space.
It is built using Python and the <code>PIL</code> library.<br>

## Features 📄

▫️ **Image Compression**: Efficiently reduces file size of images while retaining quality.<br>
▫️ **Multiple Formats Support**: Handles various image formats including JPEG and PNG.<br>
▫️ **Cross-platform**: Works on Windows, macOS, and Linux.<br>

## Requirements 🖥️

▫️ Python 3.x<br>
▫️ Pillow library<br>
▫️ Tkinter (usually included with Python)<br>

## Installation 🚀

Install the required library to import PIL<br>

    pip install pillow 

## Usage 🔍

 1. Run the script:<br>

        python main.py
    
2. A file dialog will appear. Select the image you want to compress.<br>
3. Another file dialog will appear to save the compressed image. Enter the desired file name and save it.<br>

## Configuration 🔧

The compression script is currently configured to use the <code>LANCZOS</code> filter for resizing, which provides high-quality results.<br>

## Project Structure 📁

      image-compressor/
       ├── main.py              # Main script for image compression
       └── README.md            # Project documentation

## Learnings and Skills 📘

▫️ **Python Programming**: Utilized Python for scripting and automation.<br>
▫️ **Image Processing**: Gained experience with the Pillow library for handling and manipulating images.<br>
▫️ **Graphical User Interface (GUI)**: Used <code>tkinter</code> for file dialogs to enhance user interaction.<br>

