# INDUSTRIAL-AI-BASED-ASSEMBLY-PROCESS-MANAGEMENT

## Overview

Industrial AI Based Assembly Process Management is a computer vision-based quality monitoring system developed to assist manual assembly operations in manufacturing environments. The system uses an overhead USB camera and an AprilTag attached to the operator's glove to continuously track hand movements and verify that assembly tasks are performed in the correct predefined sequence.

The application allows users to calibrate assembly points corresponding to different fastening locations and monitors the technician's workflow in real time. Each assembly point must be completed in the specified order, providing immediate visual guidance throughout the process. Once a fastening point is completed, it is marked as finished and excluded from further validation.

To improve quality assurance, the system includes an intelligent NG (No Good) detection mechanism. If the operator remains at an incorrect assembly point for more than two seconds, the system displays an NG notification indicating the expected and current positions. Temporary movements across incorrect locations do not trigger false alarms, making the system suitable for practical industrial environments.

This project demonstrates the integration of Computer Vision, Artificial Intelligence, and Industrial Automation to reduce human errors, improve assembly accuracy, and support Industry 4.0 smart manufacturing practices.

## Features

- Real-time AprilTag detection using OpenCV and Pupil AprilTags
- Overhead camera-based hand tracking
- Interactive calibration of assembly positions
- Sequential assembly verification (P1 → P2 → P3 → P4 → P5 → P6)
- Real-time operator guidance
- Intelligent NG detection for incorrect assembly sequence
- Automatic cancellation of false NG alerts
- Assembly completion time monitoring
- Modular and configurable project architecture

## Technologies Used

- Python
- OpenCV
- Pupil AprilTags
- NumPy
- JSON
- Computer Vision
- Artificial Intelligence
- Industrial Automation

## Installation

```bash
git clone https://github.com/your-username/Industrial_AI_Based_Assembly_Process_Management.git

cd Industrial_AI_Based_Assembly_Process_Management

pip install -r requirements.txt

python main.py
```

## Future Enhancements

- PLC integration
- Industrial HMI dashboard
- Assembly data logging
- Database integration
- Multi-camera support
- Operator performance analytics

## Author

**Hemanth M B**  
B.Tech Computer Science and Engineering (Artificial Intelligence and Machine Learning)  
SRM Institute of Science and Technology
