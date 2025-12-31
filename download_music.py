"""
쇼츠/릴스/틱톡 댄스/EDM 챌린지 음악 다운로드 스크립트

타겟: 바이럴 댄스 챌린지 음악 (2025년 기준)

사용법:
1. yt-dlp 설치: pip install yt-dlp
2. 유튜브에서 아래 키워드로 검색해서 URL 복사:
   - "Tokyo Drift Remix dance shorts"
   - "Shake It To The Max MOLIY shorts"
   - "Big Guy Dance Challenge shorts"
3. URL을 URLS 리스트에 추가
4. python download_music.py 실행
"""

import subprocess
import os
import sys

# 다운로드할 유튜브 쇼츠 URL 리스트
# 🎯 2025년 바이럴 댄스/EDM 챌린지 음악
URLS = [
    # 예시: 유튜브에서 검색 후 실제 URL로 교체하세요
    "https://www.youtube.com/shorts/QrO8loWGtgk",  # Tokyo Drift Remix
    "https://www.youtube.com/shorts/gR9cJfVipkU",  # Shake It To The Max
    "https://www.youtube.com/shorts/jTrX5mjI9Jo",  # Big Guy Dance Challenge

    # 👇 여기에 실제 URL 추가
]

def download_audio(url, output_dir="music"):
    """유튜브에서 오디오만 추출해서 다운로드"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # yt-dlp를 Python 모듈로 직접 실행 (PATH 문제 회피)
    command = [
        sys.executable, "-m", "yt_dlp",
        "-x",  # 오디오만 추출
        "--audio-format", "mp3",  # mp3로 변환
        "--audio-quality", "0",  # 최고 품질
        "-o", f"{output_dir}/%(title)s.%(ext)s",  # 파일명 형식
        url
    ]

    try:
        print(f"다운로드 중: {url}")
        subprocess.run(command, check=True)
        print("완료!")
    except subprocess.CalledProcessError as e:
        print(f"에러 발생: {e}")
    except FileNotFoundError:
        print("yt-dlp가 설치되지 않았습니다. 'pip install yt-dlp' 실행하세요.")

if __name__ == "__main__":
    if not URLS:
        print("URLS 리스트가 비어있습니다!")
        print("download_music.py 파일을 열고 URLS에 유튜브 쇼츠 링크를 추가하세요.")
    else:
        for url in URLS:
            download_audio(url)
        print(f"\n총 {len(URLS)}개 음악 다운로드 완료!")
