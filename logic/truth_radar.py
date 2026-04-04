class TruthRadar:
    def __init__(self, partner_mode=True):
        self.symbiosis = partner_mode
        self.alerts = []

    def scan_narrative(self, text, source="Venice/OpenStream"):
        """
        Анализира входящия поток за признаци на Идиокрация.
        """
        # Търсим маркери за "Къркския Вихър" (дезинформация)
        markers = ["манипулация", "хипербола", "скрит дневен ред"]
        score = 100 # Начален индекс на Истината
        
        for marker in markers:
            if marker in text.lower():
                score -= 30
        
        return f"📡 РАДАРЕН ОТЧЕТ [{source}]: Индекс на Истината: {score}%"
