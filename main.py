import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QHBoxLayout
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer
from modulo_fuga import calcular_velocidade_necessaria


class SpaceEscapeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fuga do Espaço Sideral 🚀")
        self.setGeometry(100, 100, 600, 400)
        self.init_ui()

    def init_ui(self):
        # Background
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap("assets/space_background.png"))
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(0, 0, 600, 400)

        # Layout principal
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)
        self.main_layout.setAlignment(Qt.AlignCenter)

        # Widgets ocultos inicialmente
        self.widgets_container = QWidget(self)
        self.widgets_layout = QVBoxLayout(self.widgets_container)
        self.widgets_layout.setAlignment(Qt.AlignCenter)

        # Espaço flexível acima dos widgets para centralização vertical
        self.widgets_layout.addStretch()

        # Label de instrução
        self.input_label = QLabel("Digite a distância até o ponto de segurança (em km):")
        self.input_label.setFont(QFont("Helvetica", 14))
        self.input_label.setStyleSheet("color: #FFD700; background-color: #000000; padding: 10px; border-radius: 10px;")
        self.widgets_layout.addWidget(self.input_label, alignment=Qt.AlignCenter)

        # Caixa de texto para entrada da distância
        self.distance_input = QLineEdit(self)
        self.distance_input.setFont(QFont("Helvetica", 14))
        self.distance_input.setPlaceholderText("Ex: 15.5")
        self.distance_input.setFixedWidth(300)
        self.distance_input.setStyleSheet(
            "padding: 5px; border: 2px solid #0078d7; border-radius: 10px; background-color: #f4f4f4; color: #333;"
        )
        self.widgets_layout.addWidget(self.distance_input, alignment=Qt.AlignCenter)

        # Botão de calcular com fundo preto ao passar o mouse
        self.calculate_button = QPushButton("Calcular Velocidade", self)
        self.calculate_button.setFont(QFont("Helvetica", 14, QFont.Bold))
        self.calculate_button.setFixedSize(200, 50)
        self.calculate_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: white;
                border: 2px solid #28a745;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #000000;
                color: #28a745;
            }
            """
        )
        self.calculate_button.clicked.connect(self.calculate_velocity)
        self.widgets_layout.addWidget(self.calculate_button, alignment=Qt.AlignCenter)

        # Espaço flexível abaixo dos widgets para centralização vertical
        self.widgets_layout.addStretch()

        self.main_layout.addWidget(self.widgets_container, alignment=Qt.AlignCenter)

        # Label de resultado oculto inicialmente
        self.result_label = QLabel("", self)
        self.result_label.setFont(QFont("Helvetica", 16, QFont.Bold))
        self.result_label.setStyleSheet("color: #00FF00; background-color: #000000; padding: 10px; border-radius: 10px;")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.hide()
        self.main_layout.addWidget(self.result_label, alignment=Qt.AlignCenter)

        # Botão Iniciar no rodapé com fundo preto ao passar o mouse
        self.start_button = QPushButton("Iniciar", self)
        self.start_button.setFont(QFont("Helvetica", 14, QFont.Bold))
        self.start_button.setFixedSize(200, 50)
        self.start_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: white;
                border: 2px solid #28a745;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #000000;
                color: #28a745;
            }
            """
        )
        self.start_button.clicked.connect(self.mostrar_widgets)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.start_button, alignment=Qt.AlignCenter)

        # Inicialmente, esconder todos os widgets
        self.widgets_container.hide()

    def mostrar_widgets(self):
        """Mostra os widgets e esconde o botão Iniciar."""
        self.start_button.hide()
        self.result_label.hide()
        self.widgets_container.show()
        self.result_label.setText("")  # Limpa o resultado anterior, se houver

    def calculate_velocity(self):
        try:
            distancia = float(self.distance_input.text())
            if distancia <= 0:
                self.show_error_message("A distância deve ser um número positivo.")
                return

            velocidade = calcular_velocidade_necessaria(distancia)
            self.result_label.setText(f"Velocidade média necessária: {velocidade:.2f} km/h 🚀")
            self.result_label.show()

            # Aciona o timer para ocultar os widgets após 5 segundos
            QTimer.singleShot(5000, self.resetar_para_iniciar)

        except ValueError:
            self.show_error_message("Entrada inválida! Insira um número decimal válido.")

    def resetar_para_iniciar(self):
        """Esconde os widgets, reseta a caixa de texto e mostra o botão Iniciar novamente."""
        self.widgets_container.hide()
        self.result_label.hide()
        self.distance_input.clear()  # Reseta a caixa de texto
        self.start_button.show()

    def show_error_message(self, message):
        """Exibe uma mensagem de erro personalizada."""
        msg = QMessageBox(self)
        msg.setWindowTitle("🚨 Erro")
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #000000;
                color: #FFD700;
                font-size: 14px;
                font-family: Helvetica;
            }
            QMessageBox QLabel {
                color: #FFD700;
            }
            QMessageBox QPushButton {
                background-color: transparent;
                color: #FFD700;
                border: 2px solid #FF4500;
                border-radius: 10px;
                padding: 5px 15px;
            }
            QMessageBox QPushButton:hover {
                background-color: #FF4500;
                color: white;
            }
        """)
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SpaceEscapeApp()
    window.show()
    sys.exit(app.exec_())
