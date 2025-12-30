"""
쇼츠/릴스/틱톡 음악 다운로드 스크립트

사용법:
1. yt-dlp 설치: pip install yt-dlp
2. 유튜브 쇼츠 URL 리스트를 아래에 추가
3. python download_music.py 실행
"""

import subprocess
import os

# 다운로드할 유튜브 쇼츠 URL 리스트
URLS = [
    # 내일 여기에 틱톡/쇼츠 인기 음악 URL 추가
    # 예: "https://www.youtube.com/shorts/xxxxx",
]

def download_audio(url, output_dir="music"):
    """유튜브에서 오디오만 추출해서 다운로드"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # yt-dlp로 오디오만 추출 (mp3 변환)
    command = [
        "yt-dlp",
        "-x",  # 오디오만 추출
        "--audio-format", "mp3",  # mp3로 변환
        "--audio-quality", "0",  # 최고 품질
        "-o", f"{output_dir}/%(title)s.%(ext)s",  # 파일명 형식
        url
    ]

    try:
        print(f"다운로드 중: {url}")
        subprocess.run(command, check=True)
        print("✅ 완료!")
    except subprocess.CalledProcessError as e:
        print(f"❌ 에러 발생: {e}")
    except FileNotFoundError:
        print("❌ yt-dlp가 설치되지 않았습니다. 'pip install yt-dlp' 실행하세요.")

if __name__ == "__main__":
    if not URLS:
        print("⚠️  URLS 리스트가 비어있습니다!")
        print("download_music.py 파일을 열고 URLS에 유튜브 쇼츠 링크를 추가하세요.")
    else:
        for url in URLS:
            download_audio(url)
        print(f"\n🎵 총 {len(URLS)}개 음악 다운로드 완료!")
