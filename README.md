# MiDaS Webcam Depth Estimation

This project demonstrates **real-time monocular depth estimation** using a regular webcam and a pre-trained MiDaS model (DPT_Large), all without the need for a depth sensor. It provides a lightweight way to apply deep learning-based depth prediction on live video feeds.

![Demo](demo_midas-webcam-depth-estimation.gif)

---

## Project Purpose

Estimating depth from a single RGB camera feed can be incredibly useful in robotics, augmented reality, assistive tech, and more. By using **MiDaS**, a state-of-the-art model from Intel ISL, this project shows how accurate depth information can be extracted from regular webcams in real-time.

I built this to:
- Understand the application of depth estimation in real-world scenarios
- Build a base for future 3D vision projects
- Possibly integrate this with object detection (YOLO) and measurement pipelines

---

## Tech Stack

- **Python 3.10+**
- **Torch** + **TorchVision**
- **OpenCV**
- **MiDaS** (via `timm` pretrained weights)

---

## How It Works

1. The webcam feed is captured using OpenCV.
2. The frame is resized and normalized to fit the MiDaS model’s expected input.
3. The depth is predicted using the `DPT_Large` MiDaS model.
4. The depth map is post-processed and displayed live.

---

## Folder Structure

```text

midas-webcam-depth-estimation/
├── cam_check.py
├── realtime_midas_depth.py
├── demo_midas-webcam-depth-estimation.gif
├── LICENSE
├── .gitignore
├── README.md
└── requirements.txt

```

---

## Installation

1. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶Run the Demo

To start real-time depth estimation:

```bash
python realtime_midas_depth.py
```

To test webcam availability:

```bash
python cam_check.py
```

---

## requirements.txt

```text
torch
torchvision
opencv-python
timm

```

---

## My Effort and What’s Next

This project is a culmination of my efforts to understand monocular depth estimation with a real-time feed. It required digging into:

- Model input/output formatting
- GPU acceleration with Torch
- Managing large virtual environments (and GitHub integration issues)

### Next Steps:
- Add side-by-side depth + RGB output to a video
- Overlay YOLOv9 bounding boxes with depth
- Publish as a Streamlit or Flask web app
- Quantify distance in centimeters using MiDaS + camera calibration

---

## License

MIT

---

## Author

Made by William Jo
