```markdown
> Deutsch | [English](README.md)

# EX5 — Bestellvalidierung

Ein Bestellvalidierungssystem, das Produkt-IDs, Mengen und Lagerbestände prüft, bevor eine Bestellung erstellt wird.

## Konzepte
- `try/except` zur Fehlerbehandlung
- Eingabevalidierung (positive Zahlen, gültige IDs)
- Überprüfung der Lagerverfügbarkeit vor der Bestellung
- Rückgabe strukturierter Daten (Wörterbuch) als Bestellrechnung

## Funktionen
- `get_product_by_id`: Findet ein Produkt anhand seiner ID
- `get_valid_quantity`: Wiederholt die Eingabe, bis eine gültige Menge eingegeben wird
- `validate_order`: Löst `ValueError` für ungültige Bestellungen aus
- `create_order`: Erstellt ein Bestellwörterbuch, wenn die Bestellung gültig ist

## Ausführung
```bash
python validation.py