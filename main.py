import os
from yt_dlp import YoutubeDL

def download_youtube_media():
    print("====================================")
    print("🎥 유튜브 미디어 다운로더 (최종 검수 완료)")
    print("====================================")
    
    url = input("▶ 다운로드할 유튜브 URL을 입력하세요: ").strip()
    
    # URL 유효성 검사 강화 (대소문자 무시 및 괄호 처리)
    if not url or ("youtube.com" not in url.lower() and "youtu.be" not in url.lower()):
        print("[오류] 올바른 유튜브 URL 형식이 아닙니다.")
        return

    print("\n[원하는 작업 선택]")
    print("1: 동영상 다운로드 (MP4 - 일반 화질/안전 모드)")
    print("2: 오디오 다운로드 (기본 고음질 추출)")
    choice = input("📌 번호를 입력하세요 (1 또는 2): ").strip()

    # 저장 폴더 설정
    download_path = os.path.join(os.getcwd(), 'downloads')
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # 다운로드 핵심 옵션 설정
    ydl_opts = {
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': True,
        'noplaylist': True,  # 재생목록 전체가 다운로드되는 것을 방지
    }

    if choice == '1':
        ydl_opts['format'] = 'best[ext=mp4]/best'
        print("\n⏳ 영상을 다운로드 중입니다. 잠시만 기다려주세요...")
        
    elif choice == '2':
        ydl_opts['format'] = 'bestaudio/best'
        print("\n⏳ 오디오를 추출 중입니다. 잠시만 기다려주세요...")
        
    else:
        print("[오류] 잘못된 번호입니다. 프로그램을 종료합니다.")
        return

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n" + "="*40)
        print("🎉 [성공] 다운로드가 완료되었습니다!")
        print(f"📂 저장 위치: {download_path}")
        print("="*40)
    except Exception as e:
        print("\n" + "="*40)
        print(f"❌ [실패] 다운로드 중 오류가 발생했습니다.")
        print(f"💡 에러 내용: {e}")
        print("💡 팁: 유튜브 사이트의 정책 변경으로 인해 라이브러리 업데이트가 필요할 수 있습니다.")
        print("="*40)

if __name__ == "__main__":
    download_youtube_media()
