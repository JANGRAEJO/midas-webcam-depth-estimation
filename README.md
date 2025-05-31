# MiDaS Webcam Depth Estimation

This project demonstrates **real-time monocular depth estimation** using the MiDaS model and a regular webcam feed. No depth sensor is required.

![Demo GIF](demo_midas-webcam-depth-estimation.gif)

## 🔍 Motivation
Depth estimation is a crucial building block for AR/VR, robotics, and computer vision. By leveraging state-of-the-art pretrained models like MiDaS, we can approximate scene depth in real-time using just a regular webcam. This project was created to:

- Experiment with MiDaS in a live setting
- Test integration with live webcam inputs
- Prepare for further fusion with object detection (YOLO) and distance conversion tools

## 🧠 Model
This project uses the [MiDaS v3.1 Small](https://github.com/isl-org/MiDaS) model from the `torch.hub` repository.

## 📦 Tech Stack
- Python 3.10+
- PyTorch
- OpenCV
- timm (for model loading)
- Conda environment (not virtualenv)

## 🗂️ Folder Structure
```
├── cam_check.py                    # Simple webcam test script
├── realtime_midas_depth.py        # Main depth estimation logic
├── demo_midas-webcam-depth-estimation.gif  # Demo output for README
├── LICENSE
├── .gitignore
├── README.md                      # This file
├── requirements.txt
```

## ▶️ How to Run
### 1. Clone the Repository
```bash
git clone https://github.com/JANGRAEJO/midas-webcam-depth-estimation.git
cd midas-webcam-depth-estimation
```

### 2. Create and Activate Conda Environment
```bash
conda create -n midas-depth python=3.10 -y
conda activate midas-depth
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Webcam Depth Estimation
```bash
python realtime_midas_depth.py
```

## 🧪 File Descriptions
### `cam_check.py`
Runs a quick test to make sure the webcam is functioning correctly using OpenCV.

### `realtime_midas_depth.py`
Main script that loads MiDaS, grabs webcam frames, preprocesses them, and shows the depth estimation output in real-time.

## 🧱 Requirements
Check `requirements.txt` for all required packages.

```txt
torch>=2.0.0
torchvision
opencv-python
timm
```

## 📌 Limitations
- Output is relative depth, not absolute distances.
- FPS may vary depending on hardware (MiDaS is heavy on CPU/GPU).

## 🔮 Next Steps
- Integrate with YOLOv9 for object detection + distance annotation
- Calibrate real-world scaling using known markers or camera parameters
- Build web app or GUI using Streamlit or Flask

## 🙋 Author
**Jangrae Jo**  
MS in ECE, UMass Amherst  
Open to research and collaboration in computer vision and depth sensing.

## 🪪 License
MIT License – see [LICENSE](LICENSE) file.

---
> If this project helps you, please ⭐ the repo and follow for more updates!
