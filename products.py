class Product:
    """
    Repräsentiert einen Produkttyp im Geschäft.
    """
    
    def __init__(self, name, price, quantity):
        """
        Konstruktor-Methode.
        Erstellt die Instanzvariablen (aktiv wird auf True gesetzt).
        
        Args:
            name (str): Der Name des Produkts
            price (float): Der Preis des Produkts
            quantity (int): Die verfügbare Menge
            
        Raises:
            ValueError: Wenn Name leer, Preis oder Menge negativ sind
        """
        if not name or name.strip() == "":
            raise ValueError("Der Produktname darf nicht leer sein.")
        if price < 0:
            raise ValueError("Der Preis darf nicht negativ sein.")
        if quantity < 0:
            raise ValueError("Die Menge darf nicht negativ sein.")
        
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
    
    def get_quantity(self) -> int:
        """
        Getter-Methode für die Menge.
        
        Returns:
            int: Die aktuelle Menge des Produkts
        """
        return self.quantity
    
    def set_quantity(self, quantity):
        """
        Setter-Methode für die Menge.
        Wenn die Menge 0 erreicht, wird das Produkt deaktiviert.
        
        Args:
            quantity (int): Die neue Menge
            
        Raises:
            ValueError: Wenn Menge negativ ist
        """
        if quantity < 0:
            raise ValueError("Die Menge darf nicht negativ sein.")
        
        self.quantity = quantity
        
        if self.quantity == 0:
            self.active = False
    
    def is_active(self) -> bool:
        """
        Getter-Methode für aktiv.
        
        Returns:
            bool: True, wenn das Produkt aktiv ist, andernfalls False
        """
        return self.active
    
    def activate(self):
        """Aktiviert das Produkt."""
        self.active = True
    
    def deactivate(self):
        """Deaktiviert das Produkt."""
        self.active = False
    
    def show(self):
        """
        Gibt einen String, der das Produkt repräsentiert, auf der Konsole aus.
        Format: "Name, Price: Preis, Quantity: Menge"
        """
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")
    
    def buy(self, quantity) -> float:
        """
        Kauft eine bestimmte Menge des Produkts.
        
        Args:
            quantity (int): Die zu kaufende Menge
            
        Returns:
            float: Der Gesamtpreis des Kaufs
            
        Raises:
            ValueError: Wenn die gewünschte Menge größer als verfügbar ist,
                       wenn die Menge 0 oder negativ ist,
                       oder wenn das Produkt nicht aktiv ist
        """
        if quantity <= 0:
            raise ValueError("Die Kaufmenge muss größer als 0 sein.")
        if not self.active:
            raise ValueError("Das Produkt ist nicht aktiv und kann nicht gekauft werden.")
        if quantity > self.quantity:
            raise ValueError(f"Nicht genügend Menge verfügbar. Verfügbar: {self.quantity}, Angefordert: {quantity}")
        
        self.quantity -= quantity
        
        if self.quantity == 0:
            self.active = False
        
        return quantity * self.price


def main():
    """Test-Funktion für die Product-Klasse."""
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()