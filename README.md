# music-experiment-001

이 레포는
AI 기반 음악 분석과 생성이 가능한지 **실험하기 위한 프로젝트**입니다.

- 목적: 짧은 실험 + 즉시 실행
- 기간: 7일 (26년 1월 첫 주)
- 목표: 쇼츠/릴스/틱톡 인기 음악 분석 → AI 작곡

## 🎯 프로젝트 목표

1. **쇼츠/릴스/틱톡에서 인기있는 음악 분석**
   - BPM, 길이, 에너지 등 핵심 특징 추출
   - 공통 패턴 발견

2. **AI 기반 음악 생성**
   - 분석 결과를 바탕으로 유사한 스타일의 음악 생성
   - 크리에이터용 배경음악 자동 제작

## 🚀 빠른 시작

### 1. 의존성 설치
```bash
pip install librosa numpy yt-dlp
```

### 2. 음악 다운로드
```bash
# download_music.py 파일을 열고 URLS에 유튜브 쇼츠 링크 추가
python download_music.py
```

### 3. 음악 분석
```bash
# music 폴더의 모든 mp3 파일 분석
python batch_analyze.py
```

결과는 `analysis_results.json`에 저장됩니다.

## 📁 파일 구조

- `analyze.py` - 단일 음악 파일 분석
- `batch_analyze.py` - 여러 음악 파일 일괄 분석 + JSON 저장
- `download_music.py` - 유튜브 쇼츠에서 음악 다운로드
- `music/` - 음악 파일 저장 폴더
- `analysis_results.json` - 분석 결과

## 📊 분석 항목

- **길이 (초)**: 쇼츠용 음악은 보통 15-30초
- **BPM**: 템포 (비트 퍼 미닛)
- **RMS 에너지**: 음악의 평균 볼륨/에너지

## ⏭️ 다음 단계

- [ ] 더 많은 음악 특징 분석 (키, 무드 등)
- [ ] AI 음악 생성 (Suno, MusicGen 등)
- [ ] 웹 인터페이스 구축
