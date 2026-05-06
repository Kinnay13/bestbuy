"""
Module für die Store-Klasse.
Verwaltet eine Kollektion von Produkten.
"""
import products


class Store:
    """
    Repräsentiert einen Store mit einer Kollektion von Produkten.
    Verwendet Komposition - "has-a"-Beziehung mit der Product-Klasse.
    """


    def __init__(self, product_list: list[products.Product]):
        """
        Konstruktor-Methode.
        
        Args:
            product_list: Eine Liste von Produkten im Store
        """
        self.products = product_list


    def add_product(self, product: products.Product):
        """
        Fügt ein Produkt zum Store hinzu.
        
        Args:
            product: Das hinzuzufügende Produkt
        """
        self.products.append(product)


    def remove_product(self, product: products.Product):
        """
        Entfernt ein Produkt aus dem Store.
        
        Args:
            product: Das zu entfernende Produkt
        """
        if product in self.products:
            self.products.remove(product)


    def get_total_quantity(self) -> int:
        """
        Gibt zurück, wie viele Artikel insgesamt im Store vorhanden sind.
        
        Returns:
            int: Die Gesamtmenge aller Produkte im Store
        """
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total


    def get_all_products(self) -> list[products.Product]:
        """
        Gibt alle aktiven Produkte im Store zurück.
        
        Returns:
            Eine Liste aller aktiven Produkte
        """
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list: list[tuple[products.Product, int]]) -> float:
        """
        Kauft die Produkte aus einer Einkaufsliste.
        
        Args:
            shopping_list: Eine Liste von Tupeln,
                          wobei jedes Tupel ein Produkt und die zu kaufende Menge enthält
        
        Returns:
            float: Der Gesamtpreis der Bestellung
            
        Raises:
            ValueError: Wenn ein Produkt nicht im Store vorhanden ist
        """
        total_price = 0
        for product, quantity in shopping_list:
            # Überprüfe, ob das Produkt im Store vorhanden ist
            if product not in self.products:
                raise ValueError(f"Das Produkt '{product.name}' befindet sich nicht im Store.")
            # Kaufe die Menge des Produkts und addiere den Preis
            total_price += product.buy(quantity)
        return total_price
