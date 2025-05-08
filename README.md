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

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/bidirectional-sign-translation.git
   cd bidirectional-sign-translation
