#Face Attendance System#


Overview

The Face Attendance System is a project aimed at automating the process of marking attendance using facial recognition technology. With this system, users can easily mark their attendance by simply showing their faces to a camera. The system detects and recognizes faces, logs the attendance data, and stores it for future reference.

Features

Facial Recognition: Utilizes face recognition technology to identify individuals.
Attendance Logging: Records attendance data including timestamps and user information.
User-friendly Interface: Simple and intuitive interface for ease of use.
Break Time Limit: Implements a 30-second break between attendance marks to prevent spamming.
Installation

Clone the repository:
bash
Copy code

Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage

Run the main script:

bash
Copy code
python main.py
Follow the instructions on the interface to mark your attendance.
Dependencies
os
pickle
cv2 (OpenCV)
face_recognition
numpy
cvzone
firebase_admin
Firebase Integration
The project integrates with Firebase for data storage and management. Firebase provides real-time database and storage solutions, enabling seamless handling of attendance records.

Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.
