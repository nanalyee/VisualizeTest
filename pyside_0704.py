import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton, QFileDialog, QScrollArea
from PySide6.QtWebEngineWidgets import QWebEngineView
from temperature_test_0704 import func

class FileLoader(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("파일 로더")
        self.setGeometry(300, 300, 800, 600)  # 창 크기 조정

        # 스크롤 영역 설정
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # 스크롤 영역 안의 위젯 설정
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        
        # 스크립트 실행 버튼
        self.run_button = QPushButton("스크립트 실행", self)
        self.run_button.clicked.connect(self.run_script)
        self.scroll_layout.addWidget(self.run_button)

        # QWebEngineView 설정
        self.script_output_display = QWebEngineView(self)
        self.scroll_layout.addWidget(self.script_output_display)

        # 스크롤 영역에 스크롤 위젯 설정
        self.scroll_area.setWidget(self.scroll_widget)

        # 메인 레이아웃에 스크롤 영역 추가
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.scroll_area)
        self.setLayout(self.main_layout)

    @Slot()
    def run_script(self):
        script_path = "./temperature_test_0704.py"  # 스크립트 파일의 경로를 여기에 적습니다.

        if script_path:
            try:
                # Python 스크립트 실행
                #subprocess.run(["python", script_path], check=True)
                func()
                
                # 생성된 HTML 파일 읽기
                #with open('./temp_output.html', 'r', encoding='utf-8') as f:
                #    html_content = f.read()

                # QWebEngineView에 HTML 설정
                # self.script_output_display.setHtml(html_content)
            except Exception as e:
                self.script_output_display.setHtml(f"<h1>스크립트를 실행하는 중 오류 발생: {str(e)}</h1>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    loader = FileLoader()
    loader.show()
    sys.exit(app.exec())
