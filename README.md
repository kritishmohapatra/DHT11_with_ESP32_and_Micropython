# 🌡️ DHT11 Temperature & Humidity Monitoring (ESP32 + MicroPython)

This project reads **temperature** and **humidity** data using a **DHT11 sensor** connected to an **ESP32** board running **MicroPython**.  
The sensor readings are printed to the Serial Console every 2 seconds.

---

## 🛠️ Hardware Components
- 🧠 ESP32 Dev Board
- 🌡️ DHT11 Temperature & Humidity Sensor
- 📏 Breadboard
- 🔌 Jumper Wires
- ⚡ (Optional) 10KΩ Pull-up Resistor (between VCC and DATA)

---

## 🧰 Wiring Diagram
| DHT11 Pin | ESP32 Pin |
|:---|:---|
| VCC (+) | 3.3V |
| GND (–) | GND |
| DATA | GPIO 4 |

> **Note:** Connect a **10KΩ resistor** between **VCC** and **DATA** for better reliability.

---

## 💻 How It Works
1. The ESP32 reads the DHT11 sensor data using MicroPython.
2. Temperature (°C) and Humidity (%) are printed to the Serial Monitor every 2 seconds.
3. Useful for creating real-time environment monitoring projects!

---

## 📂 Project Structure

---

## 🧩 Circuit Diagram
![Circuit Diagram](circuit_image_(4).png)


## 👨‍💻 Author
- ✍️ [Kritish Mohapatra]

---

## 📅 Project Date
- 🗓️ [28/04/2025]

---

# 🚀 Future Upgrades
- Display readings on a web server 🌐
- Log data to a file 📁
- Send alerts if temperature/humidity crosses threshold 🚨
