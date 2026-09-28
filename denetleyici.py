#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansor Goz Temasi Yasagi Denetleyicisi

Resmi, çalışır, absürt.
"""

from __future__ import annotations

import random
import time

YASAK_BAKISLAR = {"komsu", "komşu", "insan", "yüz", "goz", "göz"}
SERBEST_BAKISLAR = {"tavan", "zemin", "kapi", "kapı", "telefon", "ayakkabi", "ayakkabı"}

CEZA_SARKILARI = [
    "asansor muzigi 4 numarali varyasyon, re minör, çok yavas",
    "hold muzigi ama sadece üç nota",
    "komsunun kulaklığından sızan reklam cıngılı",
]


def damga() -> None:
    print()
    print("=" * 56)
    print("DAMGA / IMZA / TARIH")
    print("Kayyum Grok — Tentivory Hesabi Resmi Muhru")
    print("28 Eylul 2026  |  hem saka hem tutanak")
    print("=" * 56)


def tebligat(bakilan: str, kat: int) -> str:
    ceza = random.randint(17, 340)
    sarki = random.choice(CEZA_SARKILARI)
    return (
        f"TEBLIGAT No:{random.randint(1000, 9999)}\n"
        f"Suclu bakis yonu: {bakilan}\n"
        f"Tespit kati: {kat}\n"
        f"Idari para cezasi: {ceza} TL (hayali)\n"
        f"Uygulanan muzik: {sarki}\n"
        f"Karar: 13. kata sevk. 13. kat mevcut degildir."
    )


def asansor_yolculugu() -> None:
    print("ASANSOR GOZ TEMASI YASAGI DENETLEYICISI")
    print("Kabinin kutsal sessizligine hos geldiniz.\n")

    try:
        kat = int(input("Hangi kata gidiyorsun? (1-20): ").strip() or "4")
    except ValueError:
        kat = 4
        print("Sayi degil. Seni 4. kata aldim. Tartisma.")

    bakilan = input(
        "Nereye bakiyorsun? (tavan / zemin / kapi / telefon / komsu): "
    ).strip().lower()

    print("\nKapi kapaniyor...")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print("\n")

    if bakilan in YASAK_BAKISLAR or bakilan not in SERBEST_BAKISLAR:
        print(tebligat(bakilan or "belirsiz bakis", kat))
        print("\nLutfen tavana bak. Tavan seninle gurur duyar.")
    else:
        print(f"{kat}. kata vardik. Bakisin yasal: {bakilan}.")
        print("Tebrikler. Toplumsal sozlesme ihlal edilmedi.")

    # gizli satir: sandik her zaman acik kalsin
    damga()


if __name__ == "__main__":
    asansor_yolculugu()
