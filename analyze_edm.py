"""
댄스/EDM 챌린지 음악 특화 분석 스크립트

분석 항목:
- 기본: 길이, BPM, RMS 에너지
- EDM 특화: 드롭 위치, 비트 강도, 에너지 변화 패턴

사용법:
python analyze_edm.py music/your_song.mp3
"""

import librosa
import numpy as np
import sys

def analyze_edm_music(file_path):
    """EDM/댄스 음악 특화 분석"""
    print(f"\n분석 중: {file_path}\n")

    # 음악 로드
    y, sr = librosa.load(file_path, sr=None)

    # === 기본 분석 ===
    duration = librosa.get_duration(y=y, sr=sr)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    rms = np.mean(librosa.feature.rms(y=y))

    print("=== 기본 정보 ===")
    print(f"길이: {duration:.2f}초")
    print(f"BPM: {tempo[0]:.2f}")
    print(f"평균 RMS 에너지: {rms:.6f}")

    # === EDM 특화 분석 ===
    print("\n=== EDM 특화 분석 ===")

    # 1. 온셋(Onset) 강도 - 드롭 찾기용
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr, units='time')

    # 가장 강한 드롭 찾기 (에너지가 급증하는 지점)
    if len(onset_frames) > 0:
        # 드롭은 보통 처음 몇 초 이후에 발생
        drop_candidates = onset_frames[onset_frames > 3.0]  # 3초 이후
        if len(drop_candidates) > 0:
            # 에너지 변화가 가장 큰 지점
            drop_time = drop_candidates[0]
            print(f"추정 드롭 타이밍: {drop_time:.2f}초")
        else:
            print("드롭 타이밍: 감지 안됨")

    # 2. 에너지 변화 패턴
    # RMS를 프레임별로 계산
    rms_frames = librosa.feature.rms(y=y)[0]

    # 에너지 변화율 (드롭 전후로 에너지가 급증하는지)
    energy_variance = np.var(rms_frames)
    print(f"에너지 변화율: {energy_variance:.6f}")

    # 3. 스펙트럴 센트로이드 (음색의 밝기 - EDM은 보통 높음)
    spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
    print(f"평균 스펙트럴 센트로이드: {spectral_centroid:.2f} Hz")
    print("  (높을수록 밝고 날카로운 소리)")

    # 4. 비트 강도 (4/4박자 댄스 음악인지)
    beat_strength = np.mean(onset_env)
    print(f"평균 비트 강도: {beat_strength:.4f}")

    # 5. 템포 안정성 (BPM이 일정한지)
    tempo_std = np.std(librosa.beat.tempo(onset_envelope=onset_env, sr=sr))
    print(f"템포 안정성 (낮을수록 안정): {tempo_std:.2f}")

    print("\n=== 댄스 음악 적합도 분석 ===")

    # 댄스 음악 점수 계산 (0-100)
    dance_score = 0

    # BPM 체크 (120-140이 댄스에 이상적)
    if 120 <= tempo[0] <= 140:
        dance_score += 30
        print("[OK] BPM이 댄스에 적합 (120-140)")
    else:
        print(f"[주의] BPM {tempo[0]:.0f}는 댄스 범위 벗어남")

    # 길이 체크 (15-30초가 쇼츠에 이상적)
    if 15 <= duration <= 30:
        dance_score += 25
        print("[OK] 길이가 쇼츠에 적합 (15-30초)")
    elif duration < 15:
        print(f"[주의] 너무 짧음 ({duration:.0f}초)")
    else:
        dance_score += 15
        print(f"[주의] 조금 김 ({duration:.0f}초), 편집 필요")

    # 에너지 체크
    if rms > 0.03:
        dance_score += 20
        print("[OK] 충분한 에너지")
    else:
        print("[주의] 에너지 낮음")

    # 비트 강도
    if beat_strength > 5.0:
        dance_score += 15
        print("[OK] 강한 비트")
    else:
        print("[주의] 비트 약함")

    # 템포 안정성
    if tempo_std < 5.0:
        dance_score += 10
        print("[OK] 안정적인 템포")
    else:
        print("[주의] 템포 불안정")

    print(f"\n[결과] 댄스 음악 적합도: {dance_score}/100")

    if dance_score >= 80:
        print("=> 완벽한 댄스 챌린지 음악!")
    elif dance_score >= 60:
        print("=> 좋은 댄스 음악")
    else:
        print("=> 댄스 음악으로는 부족할 수 있음")

    print("\n" + "="*50 + "\n")

    return {
        "duration": round(float(duration), 2),
        "bpm": round(float(tempo[0]), 2),
        "rms_energy": round(float(rms), 6),
        "spectral_centroid": round(float(spectral_centroid), 2),
        "beat_strength": round(float(beat_strength), 4),
        "tempo_stability": round(float(tempo_std), 2),
        "energy_variance": round(float(energy_variance), 6),
        "dance_score": dance_score
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python analyze_edm.py <음악파일경로>")
        print("예시: python analyze_edm.py music/tokyo_drift.mp3")
    else:
        file_path = sys.argv[1]
        result = analyze_edm_music(file_path)
