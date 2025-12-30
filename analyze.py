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
# 4. 주요 키 (추정)
chroma = librosa.feature.chroma_stft(y=y, sr=sr)
chroma_mean = np.mean(chroma, axis=1)
key_index = np.argmax(chroma_mean)
keys = ['C', 'C#', 'D', 'D#', 'E',
        'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

print(f"추정 주요 키: {keys[key_index]}")

# 5. 스펙트럴 센트로이드 평균 (밝기 느낌용)
spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
print(f"평균 스펙트럴 센트로이드: {spectral_centroid:.2f} Hz")
# 6. 제로 크로싱 레이트 평균 (거칠기 느낌용)
zero_crossing_rate = np.mean(librosa.feature.zero_crossing_rate(y=y))
print(f"평균 제로 크로싱 레이트: {zero_crossing_rate:.6f}")
# 7. 멜-주파수 켑스트럼 계수 (MFCC) 평균
mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr), axis=1)
print("평균 MFCC:", mfcc)

# 8. 하모닉-퍼커시브 분리 후 퍼커시브 에너지 비율
y_harmonic, y_percussive = librosa.effects.hpss(y)
percussive_energy = np.sum(y_percussive**2)
total_energy = np.sum(y**2)
percussive_ratio = percussive_energy / total_energy
print(f"퍼커시브 에너지 비율: {percussive_ratio:.6f}")
# 9. 템포 변동성 (BPM 표준편차)
onset_env = librosa.onset.onset_strength(y=y, sr=sr)
tempo_variability = np.std(librosa.beat.tempo(onset_envelope=onset_env, sr=sr))
print(f"BPM 변동성 (표준편차): {tempo_variability:.2f}")
print("====================")
print("추가 음악 특성 분석 결과")
print("====================")
# 10. 스펙트럴 롤오프 평균 (음색 느낌용)
spectral_rolloff = np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr))
print(f"평균 스펙트럴 롤오프: {spectral_rolloff:.2f} Hz")
# 11. 스펙트럴 플럭스 평균 (변화감 느낌용)
spectral_flux = np.mean(librosa.onset.onset_strength(y=y, sr=sr))
print(f"평균 스펙트럴 플럭스: {spectral_flux:.6f}")
# 12. 크로마 피처의 분산 (화음 다양성 느낌용
chroma_variance = np.var(chroma, axis=1)
print("크로마 피처 분산:", chroma_variance)
print("====================")
print("분석 완료")
# 13. 템포 추정의 신뢰도 (온셋 강도 표준편차)
onset_strength_std = np.std(onset_env)
print(f"템포 추정 신뢰도 (온셋 강도 표준편차): {onset_strength_std:.6f}")
# 14. 멜 스펙트로그램 평균 (주파수 밸런스 느낌용)
mel_spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
mel_spectrogram_mean = np.mean(mel_spectrogram, axis=1)
print("평균 멜 스펙트로그램:", mel_spectrogram_mean)
# 15. 하모닉 에너지 비율