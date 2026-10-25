import streamlit as st
import json

# --------------------------
# Cargar datos
# --------------------------

with open("data/firmware_paths.json") as f:
    firmware_data = json.load(f)

with open("data/known_errors.json") as f:
    error_data = json.load(f)

# --------------------------
# Cabecera
# --------------------------

st.set_page_config(
    page_title="FortiGate Firmware Upgrade Assistant",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ FortiGate Firmware Upgrade Assistant")

st.info(
    "Herramienta para validar rutas de actualización de FortiOS "
    "y analizar errores comunes."
)

# --------------------------
# Ruta de Upgrade
# --------------------------

st.header("Ruta de Upgrade")

modelo = st.selectbox(
    "Modelo",
    list(firmware_data.keys())
)

version = st.text_input(
    "Versión Actual",
    placeholder="Ejemplo: 6.4.8"
)

if st.button("Buscar Ruta de Upgrade"):

    try:

        resultado = firmware_data[modelo][version]

        st.success("Ruta encontrada")

        st.write(f"**Modelo:** {modelo}")
        st.write(f"**Versión:** {version}")

        st.subheader("Ruta Recomendada")

        for paso in resultado:
            st.write(f"✅ {paso}")

        st.subheader("Checklist Pre-Upgrade")

        st.markdown("""
- ✅ Backup de configuración
- ✅ Revisar Release Notes
- ✅ Confirmar acceso por consola
- ✅ Validar espacio disponible
- ✅ Confirmar ventana de mantenimiento
- ✅ Verificar estado HA
""")

        st.subheader("Checklist Post-Upgrade")

        st.markdown("""
- ✅ Confirmar versión instalada
- ✅ Verificar VPNs
- ✅ Validar OSPF/BGP
- ✅ Revisar logs
- ✅ Verificar GUI y SSH
- ✅ Validar conectividad general
""")

    except KeyError:

        st.error(
            "No se encontró una ruta definida para esa versión."
        )
# --------------------------
# Analizador de errores
# --------------------------

st.divider()

st.header("Analizador de Errores")

error = st.selectbox(
    "Seleccione un error",
    [""] + list(error_data.keys())
)

if st.button("Analizar Error"):

    if error:

        info = error_data[error]

        st.warning("Causa Probable")

        st.write(info["causa"])

        st.subheader("Comandos Sugeridos")

        for cmd in info["comandos"]:
            st.code(cmd)

# --------------------------
# Asistente IA
# --------------------------

st.divider()

st.header("🤖 Asistente IA FortiGate")

consulta = st.text_area(
    "Describe un problema o consulta FortiGate"
)

if st.button("Consultar IA"):

    st.info("Procesando consulta...")

    st.write(f"Consulta recibida: {consulta}")

# --------------------------
# Footer
# --------------------------

st.divider()

st.caption(
    "FortiGate Firmware Upgrade Assistant v1.0 | "
    "Proyecto académico - Máster en Inteligencia Artificial"
)