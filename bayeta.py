import random

def frotar(n_frases: int = 1) -> list:

    frases_auspiciosas = [
        "Que la suerte esté siempre de tu lado.",
        "El éxito te espera en cada esquina.",
        "Tu creatividad te llevará lejos.",
        "Confía en tu intuición, te guiará hacia el triunfo.",
        "Hoy es el día perfecto para alcanzar tus metas.",
        "La prosperidad te rodea en todo momento.",
        "Cada obstáculo es una oportunidad disfrazada.",
        "Las mejores oportunidades están por llegar.",
        "Tus esfuerzos serán recompensados con creces.",
        "El universo conspira a tu favor."
    ]
    
    return random.choices(frases_auspiciosas, k=n_frases)

