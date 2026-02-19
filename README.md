# 🤖 MiRobot

MiRobot is a low-cost modular robotic platform built around a Raspberry Pi 5.  
The project focuses on learning embedded systems, power electronics, robotics architecture, and AI-based perception.

The robot uses a differential drive system, LiPo battery power, current monitoring, and camera-based object recognition.

---

## 🚀 Features

- Differential drive (tank steering)
- 4 DC gear motors (TT motors)
- Dual H-bridge motor control (TB6612FNG)
- 2S LiPo battery powered (7.4V, 5000mAh)
- Real-time voltage and current monitoring (INA219)
- Ultrasonic obstacle detection
- Camera-based object recognition (OpenCV)
- Software-based undervoltage protection
- Modular hardware architecture

---

## 🏗️ Hardware Architecture

### 🔹 Mechanical Structure
- 2 wooden circular plates (~20cm diameter)
- Two-level sandwich structure
- Open-frame design for natural airflow
- Estimated total weight: 1.5–2 kg

---

### 🔹 Traction System
- 4x TT DC gear motors
  - Voltage: 3–12V
  - Gear ratio: 1:48
  - Torque: ~0.8 kg·cm (at 3V)
  - Nominal current: 70mA
  - Peak current: 250mA (at 3V)
- Differential drive configuration
- Independent left and right control

---

### 🔹 Motor Drivers
- 2x TB6612FNG dual H-bridge drivers
  - 2 channels per driver
  - ~1A continuous per channel
  - ~3A peak
  - PWM control supported
  - Internal MOSFETs with integrated flyback protection
  - Motor voltage: 4.5–13.5V
  - Logic voltage: 2.7–5.5V

Noise mitigation:
- 470–1000µF bulk capacitors on motor supply lines
- 100nF ceramic decoupling capacitors
- Motor wiring physically separated from logic wiring

---

### 🔹 Control Unit
- Raspberry Pi 5
  - GPIO control
  - PWM generation
  - I²C communication
  - Obstacle avoidance logic
  - OpenCV-based object recognition

Logic level: 3.3V

---

### 🔹 Sensors

#### INA219 (Current & Voltage Monitoring)
- Bus voltage: 0–26V
- Max current: 3.2A
- I²C interface

Used for:
- Battery voltage monitoring
- Current consumption tracking
- Software undervoltage protection

#### Distance & Vision
- HC-SR04 ultrasonic sensor
- Raspberry Pi Camera Module 3

Ultrasonic → direct distance measurement  
Camera → object recognition & perception

---

## 🔋 Power Architecture

### Battery
- 2S LiPo
- 7.4V nominal
- 8.4V fully charged
- 5000mAh capacity

### Power Distribution

The battery is split into two main branches:

1. **Motor Power Line**
   - Direct connection to motor drivers
   - Includes bulk capacitors
   - Does NOT pass through breadboard

2. **Logic Power Line**
   - 5V buck converter (≥5A recommended)
   - Powers Raspberry Pi and sensors
   - Distributed via breadboard during prototyping

All subsystems share a common ground (GND).

---

## 🛡️ Protection & Safety

- Main fuse (5–7.5A) after battery
- Main power switch
- Bulk and decoupling capacitors
- Software-based undervoltage cutoff (~6.4V recommended for 2S LiPo)
- Motor noise mitigation strategy
- Star-ground wiring recommended

⚠ LiPo batteries are sensitive to over-discharge and must be monitored carefully.

---

## 🧠 Software Architecture

The Raspberry Pi handles:

- Motor control (PWM)
- Sensor data acquisition (I²C + GPIO)
- Obstacle avoidance logic
- Camera processing via OpenCV
- Power monitoring and safety shutdown

Planned improvements:
- Encoder-based speed control
- PID motor regulation
- Real-time motor control via dedicated microcontroller
- SLAM experiments

---

## 📂 Repository Structure

```

MiRobot/
│
├── src/              # Main robot source code
├── tests/            # Test scripts
├── docs/             # Documentation
├── hardware/         # Schematics & hardware notes
├── calibration/      # Calibration data (ignored)
├── logs/             # Runtime logs (ignored)
├── requirements.txt
├── README.md
└── .gitignore

```

---

## 🛠️ Roadmap

- [ ] Basic obstacle avoidance
- [ ] Camera-based object tracking
- [ ] Voltage-based auto shutdown
- [ ] Encoder integration
- [ ] Custom PCB design
- [ ] Dedicated motor controller (ESP32)
- [ ] Autonomous navigation experiments

---

## 🎯 Project Goals

This project aims to:

- Explore embedded systems design
- Understand motor control and power electronics
- Learn robotics architecture principles
- Integrate AI perception into mobile robotics
- Develop a modular and scalable robotic platform

---

## 📜 License

(To be defined)
```

---