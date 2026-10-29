import streamlit as st
import json
import os
import google.generativeai as genai

# --------------------------
# Gemini
# --------------------------

api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    modelo_gemini = genai.GenerativeModel("gemini-3.8-flash")
else:
    modelo_gemini = None

# Cargar datos

with open("data/firmware_paths.json") as f:
    firmware_data = json.load(f)

with open("data/known_errors.json") as f:
    error_data = json.load(f)

# Streamlit UI

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

    if not consulta.strip():

        st.warning("Introduce una consulta.")

    elif modelo_gemini is None:

        st.error(
            "Gemini no está disponible. Verifica la API Key."
        )

    else:

        try:

            with st.spinner("Consultando asistente IA..."):

                prompt = f"""
Eres un especialista Fortinet.

Responde únicamente preguntas sobre:

- FortiGate
- FortiOS
- FortiGuard
- VPN
- Routing
- Troubleshooting
- Firmware Upgrade

Consulta:

{consulta}
"""

                respuesta = modelo_gemini.generate_content(prompt)

                if hasattr(respuesta, "text") and respuesta.text:

                    st.success("Respuesta generada")
                    st.write(respuesta.text)

                else:

                    st.warning(
                        "La IA no devolvió contenido para esta consulta."
                    )

        except Exception as e:

            error_msg = str(e)

            if "429" in error_msg:

                st.warning(
                    "⚠️ Se alcanzó el límite de consultas de Gemini. "
                    "Inténtalo nuevamente más tarde."
                )

            elif "403" in error_msg:

                st.error(
                    "🔒 La API Key no tiene permisos suficientes "
                    "o el servicio no está habilitado."
                )

            elif "401" in error_msg:

                st.error(
                    "🔑 La API Key es inválida o ha expirado."
                )

            elif "404" in error_msg:

                st.error(
                    "📌 El modelo configurado no está disponible."
                )

            elif "500" in error_msg or "503" in error_msg:

                st.error(
                    "🌐 El servicio de Gemini no está disponible temporalmente."
                )

            else:

                st.error(
                    "❌ Ocurrió un error inesperado al consultar Gemini."
                )

                with st.expander("Detalles técnicos"):
                    st.code(error_msg)
# --------------------------
# Footer
# --------------------------

st.divider()

st.caption(
    "FortiGate Firmware Upgrade Assistant v1.1 | "
    "Proyecto académico - Máster en ML e Inteligencia Artificial"
)