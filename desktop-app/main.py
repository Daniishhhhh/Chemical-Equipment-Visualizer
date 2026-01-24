import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton,
    QFileDialog, QMessageBox, QWidget, QVBoxLayout,
    QHBoxLayout, QTableWidget, QTableWidgetItem,
    QHeaderView, QFrame
)

from PyQt5.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from api_client import get_latest_summary, upload_csv, get_history, download_pdf


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chemical Equipment Visualizer - Desktop")
        self.setGeometry(150, 100, 1100, 750)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # ---------------- TITLE ----------------

        title = QLabel("Chemical Equipment Visualizer")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size:22px;font-weight:bold;")
        main_layout.addWidget(title)

        # ---------------- STATUS ----------------

        self.status_label = QLabel("Backend Status: Checking...")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("color:green;font-size:13px;")
        main_layout.addWidget(self.status_label)

        # ---------------- SUMMARY CARD ----------------

        self.summary_label = QLabel("No data loaded")
        self.summary_label.setAlignment(Qt.AlignCenter)
        self.summary_label.setFrameShape(QFrame.Box)
        self.summary_label.setStyleSheet("padding:12px;font-size:14px;")
        main_layout.addWidget(self.summary_label)

        # ---------------- BUTTON BAR ----------------

        btn_layout = QHBoxLayout()

        self.upload_btn = QPushButton("Upload CSV")
        self.upload_btn.setStyleSheet("background:#2196F3;color:white;padding:8px;")
        self.upload_btn.clicked.connect(self.handle_upload)

        self.pdf_btn = QPushButton("Download PDF")
        self.pdf_btn.setStyleSheet("background:#4CAF50;color:white;padding:8px;")
        self.pdf_btn.clicked.connect(self.handle_pdf_download)

        btn_layout.addWidget(self.upload_btn)
        btn_layout.addWidget(self.pdf_btn)

        main_layout.addLayout(btn_layout)

        # ---------------- PIE CHART ----------------

        self.figure = Figure(figsize=(4, 4))
        self.canvas = FigureCanvas(self.figure)
        main_layout.addWidget(self.canvas)

        # ---------------- HISTORY ----------------

        history_title = QLabel("Upload History (Last 5 Records)")
        history_title.setAlignment(Qt.AlignCenter)
        history_title.setStyleSheet("font-size:16px;font-weight:bold;")
        main_layout.addWidget(history_title)

        self.history_table = QTableWidget()
        self.history_table.setColumnCount(6)

        self.history_table.setHorizontalHeaderLabels([
            "File",
            "Time",
            "Total",
            "Flow",
            "Pressure",
            "Temp"
        ])

        self.history_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.history_table.setEditTriggers(QTableWidget.NoEditTriggers)

        main_layout.addWidget(self.history_table)

        # ---------------- FOOTER ----------------

        footer = QLabel("Developed by Danish Sidiq")
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("color:gray;font-size:11px;")
        main_layout.addWidget(footer)

        # ---------------- INITIAL LOAD ----------------

        self.load_summary()
        self.load_history()

    # ---------------- SUMMARY ----------------

    def load_summary(self):

        data = get_latest_summary()

        if "error" in data:
            self.status_label.setText("Backend Status: NOT CONNECTED")
            self.summary_label.setText("Start Django backend")
            return

        self.status_label.setText("Backend Status: CONNECTED")

        summary = data.get("summary")
        distribution = data.get("distribution")

        text = (
            f"Total Equipment: {summary['total_equipment']}   |   "
            f"Avg Flowrate: {summary['avg_flowrate']}   |   "
            f"Avg Pressure: {summary['avg_pressure']}   |   "
            f"Avg Temperature: {summary['avg_temperature']}"
        )

        self.summary_label.setText(text)

        self.update_chart(distribution)

    # ---------------- PIE CHART ----------------

    def update_chart(self, distribution):

        if not distribution:
            return

        self.figure.clear()

        ax = self.figure.add_subplot(111)

        labels = distribution.keys()
        values = distribution.values()

        ax.pie(values, labels=labels, autopct="%1.0f%%", startangle=90)
        ax.set_title("Equipment Type Distribution")

        self.canvas.draw()

    # ---------------- HISTORY ----------------

    def load_history(self):

        history_data = get_history()

        if not isinstance(history_data, list):
            return

        self.history_table.setRowCount(len(history_data))

        for row, item in enumerate(history_data):

            summary = item["summary"]

            self.history_table.setItem(row, 0, QTableWidgetItem(item["file_name"]))
            self.history_table.setItem(row, 1, QTableWidgetItem(item["upload_time"]))
            self.history_table.setItem(row, 2, QTableWidgetItem(str(summary["total_equipment"])))
            self.history_table.setItem(row, 3, QTableWidgetItem(str(summary["avg_flowrate"])))
            self.history_table.setItem(row, 4, QTableWidgetItem(str(summary["avg_pressure"])))
            self.history_table.setItem(row, 5, QTableWidgetItem(str(summary["avg_temperature"])))

    # ---------------- UPLOAD ----------------

    def handle_upload(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select CSV File", "", "CSV Files (*.csv)"
        )

        if not file_path:
            return

        result = upload_csv(file_path)

        if "error" in result:
            QMessageBox.critical(self, "Upload Failed", str(result))
        else:
            QMessageBox.information(self, "Success", "CSV Uploaded Successfully")
            self.load_summary()
            self.load_history()

    # ---------------- PDF ----------------

    def handle_pdf_download(self):

        save_path, _ = QFileDialog.getSaveFileName(
            self, "Save Report", "equipment_report.pdf", "PDF Files (*.pdf)"
        )

        if not save_path:
            return

        success = download_pdf(save_path)

        if success:
            QMessageBox.information(self, "Success", "PDF Downloaded Successfully")
        else:
            QMessageBox.critical(self, "Error", "PDF Download Failed")


# ---------------- APP ENTRY ----------------

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
