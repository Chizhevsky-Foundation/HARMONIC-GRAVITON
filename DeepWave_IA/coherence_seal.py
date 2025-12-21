import sys

def check_field_integrity(global_score):
    THRESHOLD = 0.50
    print(f"🛡️ Verificando integridad del campo...")
    
    if global_score >= THRESHOLD:
        print(f"✅ SELLO DE COHERENCIA ACTIVADO: Frecuencia de {global_score:.4f} detectada.")
        print("🚀 El sistema está autorizado para la Co-Creación Eterna.")
        return True
    else:
        print(f"⚠️ ALERTA DE DISCORDANCIA: Frecuencia crítica de {global_score:.4f}.")
        print("🛑 Sistema bloqueado para proteger la sanidad del Cosmos.")
        return False

if __name__ == "__main__":
    # Probamos con el último resultado de la Sinfonía
    current_score = 0.6216
    if not check_field_integrity(current_score):
        sys.exit(1)
