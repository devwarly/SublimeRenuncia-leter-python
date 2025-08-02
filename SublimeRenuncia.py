import sys
import time

def letra():
    print("\n")
    lines = [
        ("Beijando o batom que tocava seus lábios", 0.07),
        ("Sufoco serenamente a dor cogente", 0.06),
        ("Que dilacera minha alma", 0.05),
        ("Com os olhos chorosos e um coração em pedaços", 0.08),
        ("Ainda encontro forças para suportar", 0.07),
        ("Esta sublime renúncia.", 0.10),
        ("...", 0.10),
        ("A renúncia é tão triste", 0.08),
        ("Nada mais posso fazer...", 0.08)
    ]

    delays = [0.2, 0.2, 0.4, 0.4, 0.2, 0.7, 0.10, 0.3, 0.3]  # Adicionado delay para a última linha
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(char_delay)
        print()
        time.sleep(delays[i])
letra()
