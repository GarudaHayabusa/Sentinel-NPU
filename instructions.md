# Model Download Instructions

Due to GitHub's file size limits, the optimized AI models are not included directly in this repository. To run Sentinel NPU locally on a Snapdragon-powered PC, you must pull the quantized models from the Qualcomm AI Hub.

**Prerequisites:**
Ensure you have the SDK installed and your API token configured:
`pip install qai-hub`

**Download Commands:**
Navigate to the root of this project in your terminal and run the following commands to pull the models targeted for the Snapdragon X Elite NPU:

```bash
# 1. Download Audio Model (Whisper Base)
qai-hub download --model whisper-base --target snapdragon-x-elite --out models/

# 2. Download Text Model (Llama 3 8B Instruct)
qai-hub download --model llama-v3-8b-instruct --target snapdragon-x-elite --out models/

# 3. Download Vision Model (YOLOv8)
qai-hub download --model yolov8 --target snapdragon-x-elite --out models/