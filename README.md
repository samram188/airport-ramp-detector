# ✈️ Airport Ramp Detector

**Real‑time YOLOv8 safety model**  
• Modular dataset → training → inference pipeline  
• Docker & FastAPI micro‑service  
• Experiment tracking with Weights & Biases  
• Reproducible data/model versions via DVC  
• Auto‑built docs site (MkDocs Material)  

## Quick‑start

```bash
git clone https://github.com/yourUser/airport-ramp-detector.git
cd airport-ramp-detector
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
# prepare data
python src/data/prepare_dataset.py --raw_dir data/raw --yolo_dir data/ramp
# train
python src/train.py --data cfg/ramp_aircraft.yaml --model yolov8n.pt --epochs 100
# inference on webcam
python src/inference.py --weights runs/train/exp/weights/best.pt --source 0
```
