import cv2
from flask import Flask, render_template, Response
from ultralytics import YOLO

app = Flask(__name__)

# Load your trained YOLOv8 model
model = YOLO("D:/cctv_gait_analyzer/runs/detect/train/weights/best.pt")
print("Model class names:", model.names)  # Debug: Show class labels

# Global alert flag
alert_triggered = False

def gen_frames():
    global alert_triggered
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break

        results = model(frame, conf=0.3)[0]
        alert_triggered = False

        for box, cls, conf in zip(results.boxes.xyxy, results.boxes.cls, results.boxes.conf):
            class_name = model.names[int(cls)]
            confidence = conf.item()
            print(f"Detected class: {class_name}, Confidence: {confidence:.2f}")

            # Optional: skip low-confidence helmet
            if class_name == "helmet" and confidence < 0.6:
                continue

            x1, y1, x2, y2 = map(int, box.tolist())

            # Violations
            if class_name in ["no-helmet", "no-vest"]:
                color = (0, 0, 255)  # Red
                label = f"No {class_name.replace('-', ' ').title()}"
                alert_triggered = True
            # Safe gear
            elif class_name in ["helmet", "vest"]:
                color = (0, 255, 0)  # Green
                label = class_name.title()
            else:
                continue  # Skip unrelated classes

            # Draw bounding box and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        # Optional: Global alert text
        if alert_triggered:
            cv2.putText(frame, "⚠️ No Safety Gear Detected!", (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

        # Encode frame for streaming
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/')
def index():
    return render_template('index.html', alert=alert_triggered)

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
