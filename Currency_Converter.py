import Exchange_Rates


def convert_usd_to_eur(amount):
    return amount * Exchange_Rates.USD_TO_EUR


def convert_usd_to_gbp(amount):
    return amount * Exchange_Rates.USD_TO_GBP


def convert_usd_to_jpy(amount):
    return amount * Exchange_Rates.USD_TO_JPY


def convert_usd_to_cad(amount):
    return amount * Exchange_Rates.USD_TO_CAD


def convert_usd_to_aud(amount):
    return amount * Exchange_Rates.USD_TO_AUD


def convert_usd_to_chf(amount):
    return amount * Exchange_Rates.USD_TO_CHF


def main():
    usd_amount = float(input("Please enter the USD amount: "))

    eur_amount = convert_usd_to_eur(usd_amount)
    gbp_amount = convert_usd_to_gbp(usd_amount)
    jpy_amount = convert_usd_to_jpy(usd_amount)
    cad_amount = convert_usd_to_cad(usd_amount)
    aud_amount = convert_usd_to_aud(usd_amount)
    chf_amount = convert_usd_to_chf(usd_amount)

    print(f"USD {usd_amount} is equal to:")
    print(f"- EUR {eur_amount}")
    print(f"- GBP {gbp_amount}")
    print(f"- JPY {jpy_amount}")
    print(f"- CAD {cad_amount}")
    print(f"- AUD {aud_amount}")
    print(f"- CHF {chf_amount}")


if __name__ == "__main__":
    main()