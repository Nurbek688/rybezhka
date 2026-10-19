"Health Calculator: BMI және тәуліктік су қажеттілігі."""


def get_float(prompt, lo, hi):
    """Санды енгізуді тексеру: қате болса қайта сұрайды."""
    while True:
        try:
            value = float(input(prompt).replace(",", "."))
            if lo <= value <= hi:
                return value
            print(f"Мән {lo}-{hi} аралығында болуы керек.")
        except ValueError:
            print("Қате: сан енгізіңіз.")


def calc_bmi(weight_kg, height_cm):
    return weight_kg / (height_cm / 100) ** 2


def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Салмақ жеткіліксіз"
    if bmi < 25:
        return "Қалыпты салмақ"
    if bmi < 30:
        return "Артық салмақ"
    return "Семіздік"


def calc_water(weight_kg, active):
    """30 мл/кг, белсенді болса +500 мл. Нәтиже литрмен."""
    ml = weight_kg * 30 + (500 if active else 0)
    return ml / 1000


def main():
    print("=== Health Calculator ===")
    weight = get_float("Салмағыңыз (кг): ", 20, 300)
    height = get_float("Бойыңыз (см): ", 100, 250)
    active = input("Бүгін спортпен айналасыз ба? (иә/жоқ): ").strip().lower() in ("иә", "ия", "да", "y")

    bmi = calc_bmi(weight, height)
    print(f"\nBMI: {bmi:.1f} - {interpret_bmi(bmi)}")
    print(f"Су қажеттілігі: шамамен {calc_water(weight, active):.1f} л/тәулік")
    print("Ескерту: нәтиже болжамды, дәрігер кеңесін алмастырмайды.")


if __name__ == "__main__":
    main()
