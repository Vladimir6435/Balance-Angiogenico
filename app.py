
# Validación de edad gestacional
while True:
    Edasem = int(input('Ingrese la Edad gestacional en semanas (24 a 42): '))
    Edadia = int(input('¿Cuántos días? (0 a 6): '))
    
    if Edasem < 24 or Edasem > 42:
        print('❌ Error: Las semanas deben estar entre 24 y 42.')
    elif Edadia < 0 or Edadia > 6:
        print('❌ Error: Los días deben estar entre 0 y 6.')
    else:
        break

def convertir_edad_gestacional(Edasem, Edadia):
    return Edasem + Edadia / 7

edad_decimal = convertir_edad_gestacional(Edasem, Edadia)
print(f"✅ Edad gestacional: {edad_decimal:.4f} semanas")

# Ingreso y validación del balance angiogénico
Balance = float(input('Ingrese el resultado del Balance Angiogénico (sFlt-1 / PlGF): '))

if Balance > 1500.0:
    print('⚠️ Verifique los valores, son inusualmente altos.')
elif Balance < 38:
    print('✅ El balance angiogénico es normal. Bajo riesgo de preeclampsia.')
elif edad_decimal < 34:
    if Balance >= 655:
        print('🔴 Niveles superiores a 655 se asocian con alto riesgo de complicaciones graves. Considere vigilancia intensiva y posible interrupción en las próximas 48 horas.')
    elif Balance >= 85:
        print('🟠 Diagnóstico de preeclampsia establecido. Se requiere vigilancia estricta. Repetir el balance en 48 horas y descartar RCIU y daño a órganos blanco.')
    elif Balance >= 38:
        print('🟡 Riesgo intermedio. Repetir el balance en una semana para monitoreo.')
    else:
        print('🟢 Balance dentro de parámetros normales.')
elif edad_decimal >= 34:
    if Balance >= 201:
        print('🔴 Niveles elevados. Mayor riesgo de deterioro materno-fetal. Se debe considerar interrupción del embarazo.')
    elif Balance > 110:
        print('🟠 Preeclampsia establecida. Evaluar condición materno-fetal.')
    elif Balance >= 38:
        print('🟡 Riesgo intermedio. Repetir el balance en una semana.')
    else:
        print('🟢 Balance dentro de parámetros normales.')
else:
    print('❓ En caso de duda, consulte a su médico.')
