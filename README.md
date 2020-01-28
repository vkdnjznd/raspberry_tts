## 라즈베리파이 TTS
- 라즈베리파이에 마이크, 스피커를 연결하여 Speech To Text, Text To Speech 를 구현 
- SpeechRecognition 패키지를 활용하여 백그라운드에서 마이크를 통해 받아들인 목소리를 gTTS 패키지로 스피커로 출력함 

시스템 환경은 다음과 같다 
- Model = Raspberry Pi 4 4GB
- OS = Raspbian
- Language = Python 3.7.3
#
## Setup
#### Step 1 라즈비안 업데이트
    sudo apt-get update
    sudo apt-get dist-upgrade
***
#### Step 2 저장소 클론
    git clone https://github.com/vkdnjznd/raspberry_tts.git
---
#### Step 3 라즈비안에 패키지 설치
반드시 가상환경(virtualenv)에서 설치

    sudo apt-get install python3-pyaudio
    sudo apt-get install portaudio19-dev python-all-dev python3-all-dev &&sudo pip3 install pyaudio
    sudo apt-get install flac
    sudo apt-get install mpg123

    cd raspberry_tts
    pip install -r requirements.txt

***
#### Step 4 실행
    cd raspberry_tts
    python3 piTTS.py
![image](https://user-images.githubusercontent.com/54702611/73259030-3edd0600-420a-11ea-9cb9-e5edcfc4eb64.png)



