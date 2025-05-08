# bidirectional-sign-lang

**A deep‑learning pipeline that translates between sign language videos and text in both directions using a CNN‑BiLSTM architecture.**

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Key Features](#key-features)  
3. [Installation](#installation)  
4. [Data Preparation](#data-preparation)  
5. [Model Architecture](#model-architecture)  
6. [Training](#training)  
7. [Evaluation](#evaluation)  
8. [Usage](#usage)  
9. [Project Structure](#project-structure)  
10. [Dependencies](#dependencies)  
11. [Contributing](#contributing)  
12. [License](#license)  

---

## Project Overview

This system performs **bidirectional translation** between sign language and text.  
- **Sign-to-Text (S2T):** Input video of a signer → Extracted visual features → BiLSTM decoder → Output text.  
- **Text-to-Sign (T2S):** Input sentence → Embedding + BiLSTM encoder → CNN-based gesture synthesizer → Output sign video frames.

Application areas include accessibility tools, real-time captioning for deaf communities, and educational aids for learning sign language.

---

## Key Features

- **Bidirectional Translation:** Supports both S2T and T2S flows.  
- **Hybrid CNN + BiLSTM:**  
  - **CNN backbone:** Learns spatial features from video frames.  
  - **BiLSTM layers:** Captures temporal dependencies in both forward and backward directions.  
- **Frame‑level Attention:** Focus on important frames for improved accuracy.  
- **Pretrained Backbone Compatibility:** Swap in ResNet, MobileNet, or custom CNNs.  
- **Modular Training & Inference Scripts:** Separate pipelines for data prep, training, evaluation, and inference.  

---
Model Architecture
Below is the high-level architecture diagram for our CNN + BiLSTM bidirectional translation system:

<p align="center"> <img src="https://i.postimg.cc/5Nxkzx3z/Screenshot-48.png" alt="Architecture Diagram" width="700"/> </p>
Components:

Frame Extraction & Preprocessing

Extract frames from input video

Resize, normalize, and augment

CNN Feature Extractor

Processes each frame to produce spatial feature vectors

BiLSTM Encoder (Text-to-Sign)

Embeds input text tokens

Bi‑directional LSTM captures context

BiLSTM Decoder (Sign-to-Text)

Takes CNN frame features as input

Predicts output text sequence

Attention Mechanism (optional)

Aligns decoder steps with relevant encoder outputs

Gesture Synthesizer (T2S)

Converts decoder outputs back into sign language frames

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/bidirectional-sign-translation.git
   cd bidirectional-sign-translation
