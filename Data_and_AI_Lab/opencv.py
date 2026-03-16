import cv2
import numpy as np

# Load multiple pre-trained Haar Cascade classifiers for better detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
upper_body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')
full_body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# Try to open camera
cap = cv2.VideoCapture(0)

# Set camera properties for better quality
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

if not cap.isOpened():
    print("Error: Cannot access camera.")
else:
    print("Camera turned on! Controls: 'Esc'=Exit, 'r'=Recalibrate, 'd'=Debug mode, 'h'=Help")
    
    # Detection parameters (can be adjusted)
    detection_params = {
        'scaleFactor': 1.05,      # Smaller steps for better detection
        'minNeighbors': 3,        # Lower threshold for more detections
        'minSize': (50, 50),      # Minimum detection size
        'maxSize': (300, 300)     # Maximum detection size
    }
    
    frame_count = 0
    detection_history = []
    debug_mode = False  # Toggle to show rejected detections

    while cap.isOpened():
        # Read a frame
        ret, frame = cap.read()
        if not ret:
            break
        
        frame_count += 1
        
        # Skip frames for better performance (process every 2nd frame)
        if frame_count % 2 != 0:
            continue

        # Image preprocessing for better detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Apply histogram equalization for better contrast
        gray = cv2.equalizeHist(gray)
        
        # Apply Gaussian blur to reduce noise
        gray = cv2.GaussianBlur(gray, (5, 5), 0)

        human_detected = False
        detection_count = 0
        detection_info = []

        # Detect faces with stricter parameters
        faces = face_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.1,  # Slightly larger steps to reduce false positives
            minNeighbors=6,   # Higher threshold for more reliable detection
            minSize=(60, 60), # Larger minimum size to avoid small false positives
            maxSize=(300, 300),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        # Filter faces with validation checks
        valid_faces = []
        rejected_faces = []
        for (x, y, w, h) in faces:
            # Check aspect ratio (faces are roughly square to slightly rectangular)
            aspect_ratio = w / h
            if 0.7 <= aspect_ratio <= 1.4:  # Face aspect ratio validation
                # Check if detection is in upper portion of frame (faces are usually higher)
                if y < frame.shape[0] * 0.7:  # Face should be in upper 70% of frame
                    # Additional validation: check for reasonable size
                    if 60 <= w <= 300 and 60 <= h <= 300:
                        valid_faces.append((x, y, w, h))
                    else:
                        rejected_faces.append((x, y, w, h, "Size"))
                else:
                    rejected_faces.append((x, y, w, h, "Position"))
            else:
                rejected_faces.append((x, y, w, h, "Aspect"))
        
        # Show rejected faces in debug mode
        if debug_mode:
            for (x, y, w, h, reason) in rejected_faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)  # Red for rejected
                cv2.putText(frame, f'Rejected: {reason}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        
        # Draw only validated faces
        for (x, y, w, h) in valid_faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            human_detected = True
            detection_count += 1
            detection_info.append('Face')

        # Detect upper bodies with validation
        upper_bodies = upper_body_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.1, 
            minNeighbors=5,  # Higher threshold for upper body
            minSize=(100, 100),  # Larger minimum size
            maxSize=(400, 400)
        )
        
        # Filter upper bodies to avoid overlap with faces
        valid_upper_bodies = []
        for (x, y, w, h) in upper_bodies:
            # Check if this detection overlaps significantly with any valid face
            overlaps_with_face = False
            for (fx, fy, fw, fh) in valid_faces:
                # Calculate overlap
                overlap_x = max(0, min(x + w, fx + fw) - max(x, fx))
                overlap_y = max(0, min(y + h, fy + fh) - max(y, fy))
                overlap_area = overlap_x * overlap_y
                detection_area = w * h
                
                if overlap_area > detection_area * 0.3:  # 30% overlap threshold
                    overlaps_with_face = True
                    break
            
            # Only add if it doesn't significantly overlap with a face
            if not overlaps_with_face:
                valid_upper_bodies.append((x, y, w, h))
        
        for (x, y, w, h) in valid_upper_bodies:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, 'Upper Body', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            human_detected = True
            detection_count += 1
            detection_info.append('Upper Body')

        # Detect full bodies with stricter parameters
        full_bodies = full_body_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.15,  # Larger steps for full body
            minNeighbors=6,    # Higher threshold
            minSize=(120, 200), # Taller minimum size for full body
            maxSize=(500, 500)
        )
        
        # Filter full bodies
        valid_full_bodies = []
        for (x, y, w, h) in full_bodies:
            # Check aspect ratio for full body (should be taller than wide)
            aspect_ratio = h / w
            if 1.5 <= aspect_ratio <= 3.0:  # Full body should be taller
                valid_full_bodies.append((x, y, w, h))
        
        for (x, y, w, h) in valid_full_bodies:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, 'Full Body', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            human_detected = True
            detection_count += 1
            detection_info.append('Full Body')

        # Update detection history for stability
        detection_history.append(human_detected)
        if len(detection_history) > 10:
            detection_history.pop(0)
        
        # Use majority voting for stable detection
        stable_detection = sum(detection_history) > len(detection_history) // 2

        # Display detection status
        status_color = (0, 255, 0) if stable_detection else (0, 0, 255)
        status_text = f"Human Detected: {detection_count} parts" if stable_detection else "No Human Detected"
        cv2.putText(frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, status_color, 2)
        
        # Display detection parameters for debugging
        cv2.putText(frame, f"Scale: {detection_params['scaleFactor']}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, f"Neighbors: {detection_params['minNeighbors']}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Print detailed detection info
        if stable_detection and detection_info:
            print(f"Human Detected! Parts: {', '.join(set(detection_info))}")

        # Display the frame with detection
        cv2.imshow("Enhanced Human Detection", frame)

        # Handle key presses
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # Esc key
            break
        elif key == ord('r'):  # Recalibrate
            print("Recalibrating detection parameters...")
            # Reset to stricter parameters to reduce false positives
            detection_params['scaleFactor'] = 1.1
            detection_params['minNeighbors'] = 6
            print(f"Recalibrated to stricter parameters: scaleFactor={detection_params['scaleFactor']}, minNeighbors={detection_params['minNeighbors']}")
        elif key == ord('d'):  # Toggle debug mode
            debug_mode = not debug_mode
            print(f"Debug mode: {'ON' if debug_mode else 'OFF'}")
        elif key == ord('h'):  # Help
            print("Controls: 'Esc'=Exit, 'r'=Recalibrate, 'd'=Debug mode, 'h'=Help")

    cap.release()
    cv2.destroyAllWindows()