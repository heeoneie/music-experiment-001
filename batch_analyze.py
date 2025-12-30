"""
music 폴더의 모든 mp3 파일을 분석하고 결과를 JSON으로 저장

사용법:
python batch_analyze.py
"""

import librosa
import numpy as np
import json
import os
from pathlib import Path

def analyze_music(file_path):
    """음악 파일 분석"""
    print(f"\n분석 중: {file_path}")

    # 음악 로드
    y, sr = librosa.load(file_path, sr=None)

    # 1. 길이 (초)
    duration = librosa.get_duration(y=y, sr=sr)

    # 2. BPM
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

    # 3. 에너지 평균 (음량 느낌용)
    rms = np.mean(librosa.feature.rms(y=y))

    result = {
        "file": os.path.basename(file_path),
        "duration_sec": round(float(duration), 2),
        "bpm": round(float(tempo[0]), 2),
        "rms_energy": round(float(rms), 6)
    }

    # 결과 출력
    print(f"  길이: {result['duration_sec']}초")
    print(f"  BPM: {result['bpm']}")
    print(f"  RMS 에너지: {result['rms_energy']}")

    return result

def main():
    music_dir = "music"

    # music 폴더 확인
    if not os.path.exists(music_dir):
        print(f"❌ {music_dir} 폴더가 없습니다.")
        return

    # mp3 파일 찾기
    mp3_files = list(Path(music_dir).glob("*.mp3"))

    if not mp3_files:
        print(f"❌ {music_dir} 폴더에 mp3 파일이 없습니다.")
        return

    print(f"🎵 {len(mp3_files)}개 음악 파일 발견!")

    # 모든 파일 분석
    results = []
    for mp3_file in mp3_files:
        try:
            result = analyze_music(str(mp3_file))
            results.append(result)
        except Exception as e:
            print(f"❌ 에러 발생: {e}")

    # 결과를 JSON으로 저장
    output_file = "analysis_results.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n✅ 분석 완료! 결과: {output_file}")

    # 통계 출력
    if results:
        print("\n=== 전체 통계 ===")
        avg_bpm = sum(r['bpm'] for r in results) / len(results)
        avg_duration = sum(r['duration_sec'] for r in results) / len(results)
        avg_energy = sum(r['rms_energy'] for r in results) / len(results)

        print(f"평균 BPM: {avg_bpm:.2f}")
        print(f"평균 길이: {avg_duration:.2f}초")
        print(f"평균 에너지: {avg_energy:.6f}")

if __name__ == "__main__":
    main()
