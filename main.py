import products
import store


# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def start(store_obj: store.Store):
    """
    Startet die interaktive Store-Benutzeroberfläche.
    
    Args:
        store_obj: Das Store-Objekt zur Verwaltung von Produkten und Bestellungen
    """
    while True:
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        
        choice = input("Please choose a number: ").strip()
        
        if choice == "1":
            # Liste alle aktiven Produkte auf
            products_list = store_obj.get_all_products()
            print("------")
            for i, product in enumerate(products_list, 1):
                print(f"{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
            print("------")
        
        elif choice == "2":
            # Zeige die Gesamtmenge an
            total = store_obj.get_total_quantity()
            print(f"Total of {total} items in store")
        
        elif choice == "3":
            # Bestellungsprozess
            products_list = store_obj.get_all_products()
            print("------")
            for i, product in enumerate(products_list, 1):
                print(f"{i}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")
            print("------")
            print("When you want to finish order, enter empty text.")
            
            shopping_list = []
            
            while True:
                product_choice = input("Which product # do you want? ").strip()
                
                # Wenn der Benutzer leer eingibt, beende die Eingabe
                if product_choice == "":
                    break
                
                try:
                    product_index = int(product_choice) - 1
                    
                    # Überprüfe, ob der Index gültig ist
                    if product_index < 0 or product_index >= len(products_list):
                        print("Invalid product number. Please try again.")
                        continue
                    
                    quantity_input = input("What amount do you want? ").strip()
                    
                    # Wenn der Benutzer leer eingibt beim Preis, starte von vorne
                    if quantity_input == "":
                        break
                    
                    quantity = int(quantity_input)
                    
                    if quantity <= 0:
                        print("Quantity must be greater than 0. Please try again.")
                        continue
                    
                    # Füge das Produkt und die Menge zur Einkaufsliste hinzu
                    shopping_list.append((products_list[product_index], quantity))
                    print("Product added to list!")
                
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")
                    continue
            
            # Verarbeite die Bestellung
            if shopping_list:
                try:
                    total_price = store_obj.order(shopping_list)
                    print("********")
                    print(f"Order made! Total payment: ${total_price}")
                except ValueError as e:
                    print(f"Error: {e}")
        
        elif choice == "4":
            # Beende das Programm
            print("Thank you for shopping!")
            break
        
        else:
            print("Invalid choice. Please try again.")


def main():
    """Hauptfunktion zum Starten der Anwendung."""
    start(best_buy)


if __name__ == "__main__":
    main()