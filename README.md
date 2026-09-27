**Sentinel NPU: The On-Device Confidential AI Workspace**



Built for the Snapdragon® AI Lab Build \& Present Challenge - 2026



Sentinel NPU is a secure, completely offline multimodal AI assistant designed for enterprise professionals handling highly sensitive data (legal, medical, HR). By leveraging the localized processing power of the Snapdragon Hexagon NPU on HP PCs, Sentinel provides AI productivity tools without ever sending a single byte of confidential data to the cloud.



**The Problem \& The Solution**

Professionals in strict compliance environments (like India's DPDP Act, HIPAA, or GDPR) are currently excluded from the cloud-based AI revolution due to data privacy risks. 



**Sentinel NPU** solves this by routing three distinct AI models directly through the Snapdragon NPU to run concurrently and entirely offline:

1\. **Real-time Audio Transcription**: Documents client meetings and consultations locally.

2\. **LLM Analysis \& PII Redaction**: Summarizes notes and automatically redacts sensitive information (names, IDs, financials) before export.

3\. **Computer Vision Security**: Actively monitors the laptop's background and instantly blurs the screen if an unauthorized person attempts to shoulder-surf.



**Qualcomm AI Hub Integration**

This project utilizes quantized models optimized for Snapdragon compute platforms, sourced directly from the Qualcomm AI Hub:



Audio: 'Whisper (Base/Small)' – Optimized for NPU offloading for continuous, low-latency dictation.



Text: 'Llama-3-8B-Instruct' – Quantized for local generative tasks and PII extraction.



Vision: 'YOLOv8' – Lightweight facial detection model running on the NPU to monitor webcam feeds with near-zero battery drain.



**Why Snapdragon \& HP PCs?**



Running three separate neural networks (Audio, LLM, Vision) simultaneously on standard CPU/GPU architectures causes severe thermal throttling and battery drain. By optimizing these models via the Qualcomm AI Hub to target the   Snapdragon X Elite/Plus NPU, Sentinel achieves massive concurrent multi-tasking performance while maintaining the all-day battery life and cool thermals expected by HP enterprise users.



**Prerequisites**

&#x20;   **Hardware**:   A Snapdragon-powered HP PC (e.g., HP OmniBook X, HP EliteBook Ultra).

&#x20;   **OS**:   Windows 11 on ARM.

&#x20;   **Software**:   Python 3.10+, ONNX Runtime, and the Qualcomm AI Hub SDK (`qai-hub`).



**Installation** \& **Setup**



1\.   Clone the repository:  

&#x20;  ```bash

&#x20;  git clone \[https://github.com/](https://github.com/)\[your-username]/Sentinel-NPU.git

&#x20;  cd Sentinel-NPU

