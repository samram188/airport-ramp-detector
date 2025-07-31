from ultralytics import YOLO
from pathlib import Path
import numpy as np, cv2, random

def test_dummy(tmp_path):
    weights = Path("weights/best.pt")
    if not weights.exists():
        return
    model = YOLO(weights)
    img = tmp_path / "dummy.jpg"
    cv2.imwrite(str(img), np.ones((512, 512, 3), dtype=np.uint8) * random.randint(0, 255))
    out = model.predict(img, conf=0.01)
    assert out and out[0].boxes is not None
