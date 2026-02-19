# MiRobot components

This document describes the hardware architecture of MiRobot and how all subsystems are connected together.

---

## 1. Inventory

In the latest version of MiRobot (![Release](https://img.shields.io/github/v/release/Michele-Vitali/Robot)) the system is composed of the following subsystems.

---

## 1.1 Mechanical Structure

The chassis is designed to be lightweight, modular and low-cost.

Configuration:
- **2 thin wooden discs** (~20cm diameter).
- Two-level sandwich structure to separate power electronics and logic.
- Open-frame design for natural airflow and improved thermal dissipation.

Estimated total robot weight: 1.5–2 kg.

---

## 1.2 Traction System

The robot uses a differential drive configuration (tank steering).

### Motors (TT DC Gear Motors)

Specifications:
- Voltage range: 3–12V
- Gear ratio: 1:48
- Torque: ~0.8 kg·cm (at 3V)
- Nominal current: 70mA
- Peak current: 250mA (at 3V)

We use **4 motors total**:
- 2 on the left side
- 2 on the right side

Each motor is independently driven through a dedicated H-bridge channel.

---

## 1.3 Motor Drivers

We use **2 TB6612FNG dual H-bridge drivers**.

Specifications:
- 2 channels (A and B)
- 1 motor per channel
- ~1A continuous current per channel
- ~3A peak current
- PWM speed control
- Internal MOSFETs with integrated flyback protection
- Motor supply voltage: 4.5V–13.5V
- Logic voltage: 2.7V–5.5V

### Electrical Noise Mitigation

To reduce motor-induced electrical noise:

- 470–1000µF electrolytic capacitors are placed near each driver’s motor supply input.
- 100nF ceramic capacitors are used for high-frequency decoupling.
- Motor power wiring is kept physically separated from logic wiring.

---

## 1.4 Control Unit

The robot is controlled by a **Raspberry Pi 5**.

It handles:
- GPIO control
- PWM generation
- I²C communication
- Obstacle avoidance logic
- OpenCV-based object recognition

Logic voltage: 3.3V.

Voltage compatibility must always be verified before connecting peripherals.

Additional decoupling capacitors (470µF + 100nF) are placed near the 5V rail to improve voltage stability.

---

## 1.5 Sensors

### 1.5.1 Current & Voltage Monitoring

An INA219 current sensor is used to monitor:

- Battery voltage
- Current consumption
- Estimated power usage

Specifications:
- Bus voltage: 0–26V
- Max current: 3.2A
- Logic: 3–5V
- I²C interface

The system software implements:

- Undervoltage detection (cutoff recommended at ~6.4V for 2S LiPo)
- Consumption monitoring
- Safety shutdown logic (future implementation)

---

### 1.5.2 Distance & Object Recognition

Sensors used:

- HC-SR04 ultrasonic sensor
- Raspberry Pi Camera Module 3

The ultrasonic sensor provides real-time distance measurements.

The camera is used for object recognition and can assist obstacle detection.

---

## 1.6 Power Supply Architecture

### Battery

- Type: 2S LiPo
- Nominal voltage: 7.4V
- Fully charged: 8.4V
- Capacity: 5000mAh

---

### Power Distribution

The battery output is split into two branches:

1. **Motor Power Line**
   - Directly connected to motor drivers.
   - Does NOT pass through breadboard.
   - Includes bulk capacitors for stabilization.

2. **Logic Power Line**
   - Connected to a 5V buck converter (recommended ≥5A output).
   - Powers Raspberry Pi and low-power sensors.
   - Distributed via breadboard during prototyping.

All subsystems share a common ground (GND).

---

### Protection Components

To increase reliability and safety:

- Main fuse (5–7.5A) directly after battery.
- Main power switch.
- Bulk electrolytic capacitors (470–1000µF).
- 100nF decoupling capacitors.
- Software-based undervoltage cutoff via INA219.

---

## 1.7 Grounding & Wiring Strategy

- Star-ground configuration preferred.
- Motor current paths kept separate from logic signal paths.
- Short power cables to reduce voltage drop.
- Twisted motor wires recommended to reduce EMI.

---

## 1.8 Future Improvements

Planned hardware upgrades:

- Motors with quadrature encoders.
- Dedicated microcontroller for real-time motor control.
- Custom PCB instead of breadboard.
- Hardware-based low-voltage cutoff or BMS integration.
- Additional distance sensors for 180° obstacle detection.
