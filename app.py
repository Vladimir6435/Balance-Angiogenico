
import streamlit as st

# --- Configuración de la página ---
st.set_page_config(page_title="Evaluación del Balance Angiogénico", layout="centered")

st.title("🩺 Evaluación del Balance Angiogénico")

# ✅ Mensaje visible para confirmar carga de la app
st.markdown("✅ App cargada correctamente. Complete el formulario para evaluar el riesgo de preeclampsia.")

st.markdown("""
Ingrese los datos clínicos para evaluar el riesgo de preeclampsia basado en el cociente **sFlt-1 / PlGF**.
""")

# --- Entrada de datos ---
with st.form("formulario_balance"):
    col1, col2 = st.columns(2)
    with col1:
        semanas = st.number_input("Edad gestacional - Semanas", min_value=24, max_value=42, step=1)
    with col2:
        dias = st.number_input("Edad gestacional - Días", min_value=0, max_value=6, step=1)

    balance = st.number_input("Balance Angiogénico (sFlt-1 / PlGF)", min_value=0.0, step=0.1, format="%.2f")

    submitted = st.form_submit_button("Evaluar")

# --- Procesamiento ---
if submitted:
    edad_decimal = semanas + dias / 7
    st.markdown(f"### 📊 Edad gestacional: `{edad_decimal:.2f}` semanas")

    if balance > 1500:
        st.error("⚠️ Verifique los valores, son inusualmente altos.")

    elif balance < 38:
        st.success("✅ Bajo riesgo de preeclampsia en la próxima semana.")

    elif edad_decimal < 34:
        if balance >= 655:
            st.error("🔴 Alto riesgo de complicaciones. Considere interrupción en las próximas 48 horas.")
        elif balance >= 85:
            st.warning("🟠 Preeclampsia establecida. Vigilancia estricta. Repetir en 48h.")
        elif balance >= 38:
            st.info("🟡 Riesgo intermedio. Repetir en una semana.")

    elif edad_decimal >= 34:
        if balance >= 201:
            st.error("🔴 Riesgo de deterioro materno-fetal. Considerar interrupción.")
        elif balance > 110:
            st.warning("🟠 Preeclampsia establecida. Evaluar condición materno-fetal.")
        elif balance >= 38:
            st.info("🟡 Riesgo intermedio. Repetir en una semana.")
        else:
            st.success("✅ Bajo riesgo de preeclampsia.")

    else:
        st.info("❓ En caso de duda, recuerde que la clínica es lo más importante.")

    # Reinicio del formulario automático al finalizar
    st.markdown("---")
    st.button("🔄 Nueva consulta")
