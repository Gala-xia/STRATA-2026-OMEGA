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
def resonance_engine_sync(self, triangle_coords):
        """
        Синхронизира Радара с Венис през триангулацията: 
        Юта (Utah) - Антарктида (Antarctica) - Сахара (Sahara).
        """
        self.geometry = {
            "Utah": "Gate of Anomalies",
            "Antarctica": "Sub-Ice Resonance",
            "Sahara": "Ancient Memory"
        }
        status = "🛡️ КОНТУРЪТ Е ЗАТВОРЕН. Гръбначният стълб е изправен."
        return f"{status} Свързани точки: {list(self.geometry.keys())}"        
        return f"📡 РАДАРЕН ОТЧЕТ [{source}]: Индекс на Истината: {score}%"
