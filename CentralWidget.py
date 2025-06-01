from PyQt6.QtCharts import QChartView, QChart, QLineSeries, QDateTimeAxis, QValueAxis, QSplineSeries
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtGui import QColor


class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        # Erstellen einer Linie für Höchsttemperaturen
        series_höchsttemperatur = QSplineSeries()  # Erstellt eine Serie für eine einfache Linie
        series_höchsttemperatur.setName("Höchsttemperatur")  # Setzt den Namen der Serie
        # Datenpunkte zur Serie hinzufügen: Datum (als Zeit in ms) und Temperatur
        series_höchsttemperatur.append(QDateTime.fromString("2025-01-01", "yyyy-MM-dd").toMSecsSinceEpoch(), -3)
        series_höchsttemperatur.append(QDateTime.fromString("2025-02-01", "yyyy-MM-dd").toMSecsSinceEpoch(), -2)
        series_höchsttemperatur.append(QDateTime.fromString("2025-03-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 2)
        series_höchsttemperatur.append(QDateTime.fromString("2025-04-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 6)
        series_höchsttemperatur.append(QDateTime.fromString("2025-05-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 10)
        series_höchsttemperatur.append(QDateTime.fromString("2025-06-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 13)
        series_höchsttemperatur.append(QDateTime.fromString("2025-07-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 15)
        series_höchsttemperatur.append(QDateTime.fromString("2025-08-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 15)
        series_höchsttemperatur.append(QDateTime.fromString("2025-09-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 12)
        series_höchsttemperatur.append(QDateTime.fromString("2025-10-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 8)
        series_höchsttemperatur.append(QDateTime.fromString("2025-11-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 4)
        series_höchsttemperatur.append(QDateTime.fromString("2025-12-01", "yyyy-MM-dd").toMSecsSinceEpoch(), -2)

        series_höchsttemperatur.setColor(QColor("red"))

        # Erstellen einer Spline-Linie für Tiefsttemperaturen
        series_tiefsttemperatur = QLineSeries()  # Erstellt eine Serie für eine geglättete Linie
        series_tiefsttemperatur.setName("Tiefsttemperatur")  # Setzt den Namen der Serie
        # Datenpunkte zur Serie hinzufügen: Datum (als Zeit in ms) und Temperatur
        series_tiefsttemperatur.append(QDateTime.fromString("2025-01-01", "yyyy-MM-dd").toMSecsSinceEpoch(), -5)
        series_tiefsttemperatur.append(QDateTime.fromString("2025-02-01", "yyyy-MM-dd").toMSecsSinceEpoch(), -4)
        series_tiefsttemperatur.append(QDateTime.fromString("2025-03-01", "yyyy-MM-dd").toMSecsSinceEpoch(), -3)
        series_tiefsttemperatur.append(QDateTime.fromString("2025-04-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 1)
        series_tiefsttemperatur.append(QDateTime.fromString("2025-05-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 5)
        series_tiefsttemperatur.append(QDateTime.fromString("2025-06-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 8)
        series_tiefsttemperatur.append(QDateTime.fromString("2025-07-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 9)
        series_tiefsttemperatur.append(QDateTime.fromString("2025-08-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 10)
        series_tiefsttemperatur.append(QDateTime.fromString("2025-09-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 7)
        series_tiefsttemperatur.append(QDateTime.fromString("2025-10-01", "yyyy-MM-dd").toMSecsSinceEpoch(), 4)
        series_tiefsttemperatur.append(QDateTime.fromString("2025-11-01", "yyyy-MM-dd").toMSecsSinceEpoch(), -2)
        series_tiefsttemperatur.append(QDateTime.fromString("2025-12-01", "yyyy-MM-dd").toMSecsSinceEpoch(), -5)

        series_tiefsttemperatur.setColor(QColor("blue"))

        # Erstellen der X-Achse für die Datumsanzeige
        axis_x = QDateTimeAxis()  # Erstellt eine X-Achse, die Datum und Zeit darstellt
        axis_x.setTitleText("Datum")  # Setzt den Titel der Achse

        # Start- und Enddatum für die X-Achse definieren
        start_date = QDateTime.fromString("2025-01-01", "yyyy-MM-dd")
        end_date = QDateTime.fromString("2025-12-01", "yyyy-MM-dd")

        axis_x.setRange(start_date, end_date)  # Setzt den Bereich der X-Achse
        axis_x.setFormat("dd.MM.yyyy")  # Definiert das Format der Datumsanzeige
        axis_x.setTickCount(12)  # Setzt die Anzahl der Ticks (1 pro Monat)

        # Erstellen der Y-Achse für die Höchsttemperaturen
        axis_grad = QValueAxis()  # Erstellt eine Y-Achse für numerische Werte
        axis_grad.setTitleText("Grad")  # Setzt den Titel der Achse
        axis_grad.setRange(-20, 35)  # Setzt den Wertebereich der Y-Achse
        axis_grad.setTickCount(12)  # Setzt die Anzahl der Ticks

        # Erstellen der Y-Achse für die Tiefsttemperaturen
        axis_tage = QValueAxis()  # Zweite Y-Achse für numerische Werte
        axis_tage.setTitleText("Tage")  # Setzt den Titel der Achse
        axis_tage.setRange(0, 30)  # Setzt den Wertebereich der Achse
        axis_tage.setTickCount(12)  # Setzt die Anzahl der Ticks

        # Erstellen des Charts
        q_chart = QChart()  # Erstellt das Hauptdiagramm
        q_chart.setTitle("Wetterstation")  # Setzt den Titel des Diagramms

        # Hinzufügen der Achsen zum Chart
        q_chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)  # X-Achse unten
        q_chart.addAxis(axis_grad, Qt.AlignmentFlag.AlignLeft)  # Linke Y-Achse
        q_chart.addAxis(axis_tage, Qt.AlignmentFlag.AlignRight)  # Rechte Y-Achse

        # Hinzufügen der Datenserien zum Chart
        q_chart.addSeries(series_höchsttemperatur)  # Fügt die Serie für Höchsttemperaturen hinzu
        q_chart.addSeries(series_tiefsttemperatur)  # Fügt die Serie für Tiefsttemperaturen hinzu

        # Verknüpfen der Serien mit den Achsen
        series_höchsttemperatur.attachAxis(axis_tage)  # Verknüpft die Höchsttemperatur-Serie mit der X-Achse
        series_höchsttemperatur.attachAxis(axis_grad)  # Verknüpft die Serie mit der linken Y-Achse
        series_tiefsttemperatur.attachAxis(axis_grad)  # Verknüpft die Tiefsttemperatur-Serie mit der X-Achse
        series_tiefsttemperatur.attachAxis(axis_tage)  # Verknüpft die Serie mit der rechten Y-Achse

        # Setzen des Charts im ChartView
        self.setChart(q_chart)  # Zeigt das Diagramm im Widget an