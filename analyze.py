import librosa
import numpy as np

# 음악 로드
y, sr = librosa.load("music/input.mp3", sr=None)

# 1. 길이 (초)
duration = librosa.get_duration(y=y, sr=sr)

# 2. BPM (대충)
tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

# 3. 에너지 평균 (음량 느낌용)
rms = np.mean(librosa.feature.rms(y=y))

print("=== 음악 분석 결과 ===")
print(f"길이 (초): {duration:.2f}")
print(f"추정 BPM: {tempo[0]:.2f}")
print(f"평균 RMS 에너지: {rms:.6f}")
print("====================")
