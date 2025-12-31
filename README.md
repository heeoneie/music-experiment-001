# music-experiment-001

이 레포는
AI 기반 음악 분석과 생성이 가능한지 **실험하기 위한 프로젝트**입니다.

- 목적: 짧은 실험 + 즉시 실행
- 기간: 7일 (26년 1월 첫 주)
- 목표: 쇼츠/릴스/틱톡 인기 음악 분석 → AI 작곡

## 🎯 프로젝트 목표

**타겟 장르: 댄스/EDM 챌린지 음악** 🎧

1. **바이럴 댄스 챌린지 음악 분석**
   - 2025년 틱톡/쇼츠 TOP 트렌드 음악 (Tokyo Drift Remix, Shake It To The Max 등)
   - BPM, 드롭 타이밍, 비트 강도 등 EDM 특화 분석
   - 댄스 음악 적합도 점수 계산

2. **AI 기반 댄스 음악 생성**
   - 분석 결과를 바탕으로 유사한 스타일의 댄스 음악 생성
   - 크리에이터용 저작권 Free 배경음악 제작
   - 15-30초 쇼츠 최적화

## 🚀 빠른 시작

### 1. 의존성 설치
```bash
pip install librosa numpy yt-dlp
```

### 2. 음악 다운로드

**유튜브에서 이 키워드로 검색:**
- "Tokyo Drift Remix dance shorts"
- "Shake It To The Max MOLIY shorts"
- "Big Guy Dance Challenge shorts"

```bash
# 1. download_music.py 파일을 열고 URLS에 유튜브 쇼츠 링크 추가
# 2. 실행
python download_music.py
```

### 3. EDM 음악 분석

```bash
# 단일 파일 상세 분석 (드롭 타이밍, 댄스 적합도 등)
python analyze_edm.py music/your_song.mp3

# 여러 파일 일괄 분석
python batch_analyze.py
```

결과는 `analysis_results.json`에 저장됩니다.

## 📁 파일 구조

- `analyze.py` - 기본 음악 분석
- `analyze_edm.py` - **EDM/댄스 음악 특화 분석** (드롭, 비트 강도, 댄스 적합도)
- `batch_analyze.py` - 여러 음악 파일 일괄 분석 + JSON 저장
- `download_music.py` - 유튜브 쇼츠에서 바이럴 댄스 음악 다운로드
- `music/` - 음악 파일 저장 폴더
- `analysis_results.json` - 분석 결과

## 📊 분석 항목

### 기본 분석
- **길이**: 쇼츠용 음악은 15-30초가 이상적
- **BPM**: 댄스 음악은 120-140이 최적
- **RMS 에너지**: 음악의 평균 볼륨

### EDM 특화 분석 (analyze_edm.py)
- **드롭 타이밍**: 에너지가 급증하는 지점 (보통 3-8초)
- **비트 강도**: 4/4박자 댄스 음악 적합도
- **스펙트럴 센트로이드**: 음색의 밝기 (EDM은 높음)
- **템포 안정성**: BPM이 일정한지 (안정적일수록 댄스에 좋음)
- **에너지 변화 패턴**: 드롭 전후 에너지 변화
- **댄스 적합도 점수**: 0-100점 (80점 이상 권장)

## 🎯 2025년 바이럴 댄스 챌린지 음악

분석 타겟 음악 (틱톡/쇼츠 기준):
1. **Tokyo Drift Remix** - 45.9M+ 포스트
2. **Shake It To The Max** - MOLIY (40.8M+ 포스트)
3. **Big Guy Dance Challenge** - SpongeBob Dance

## ⏭️ 다음 단계

- [ ] 10-20개 바이럴 댄스 음악 분석 완료
- [ ] 공통 패턴 정리 (BPM, 구조, 드롭 타이밍)
- [ ] AI 음악 생성 (Suno/MusicGen)
- [ ] 수익화 전략 (구독 모델 or B2B)
