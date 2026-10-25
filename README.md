# 🛡️ FortiGate Firmware Upgrade Assistant

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red.svg)
![Fortinet](https://img.shields.io/badge/Fortinet-FortiGate-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

---

# 📖 Descripción

FortiGate Firmware Upgrade Assistant es una aplicación desarrollada para ayudar a administradores e ingenieros de redes a planificar y validar procesos de actualización de firmware en dispositivos FortiGate.

La herramienta centraliza información sobre rutas de actualización, errores comunes, procedimientos recomendados y próximamente incorporará capacidades de Inteligencia Artificial para análisis de incidentes y asistencia técnica contextual.

El objetivo principal es reducir riesgos operacionales, minimizar errores humanos y acelerar procesos de troubleshooting durante actividades relacionadas con FortiOS.

---

# 🎯 Problema que Resuelve

Las actualizaciones de firmware en equipos FortiGate pueden resultar complejas debido a:

- Compatibilidad entre versiones.
- Saltos obligatorios de firmware.
- Problemas de conectividad con FortiGuard.
- Procedimientos incompletos.
- Falta de documentación centralizada.
- Riesgos de indisponibilidad durante ventanas de mantenimiento.

Cuando no se siguen las rutas correctas de actualización pueden producirse:

- Fallos de upgrade.
- Reinicios inesperados.
- Pérdida temporal de servicios.
- Problemas de compatibilidad.
- Incremento en tiempos de soporte.

---

# 👨‍💻 Usuarios Objetivo

- Administradores de Redes
- Ingenieros de Infraestructura
- Ingenieros de Seguridad
- Analistas de Operaciones
- Técnicos NOC
- Técnicos SOC
- MSP (Managed Service Providers)
- Partners Fortinet

---

# 🚀 Funcionalidades Implementadas

---

## 1. Consulta de Rutas de Upgrade

Permite validar rutas de actualización soportadas para modelos específicos.

### Ejemplo

**Modelo**

```text
FG-60F
```

**Versión actual**

```text
6.4.8
```

**Resultado**

```text
7.0.5
↓
7.0.13
↓
7.2.8
```

---

## 2. Checklist Pre-Upgrade

La aplicación genera una lista de buenas prácticas antes de realizar el cambio.

### Verificaciones recomendadas

- Backup de configuración
- Revisión de Release Notes
- Validación de acceso por consola
- Verificación de espacio disponible
- Confirmación de ventana de mantenimiento
- Revisión de HA (High Availability)

---

## 3. Checklist Post-Upgrade

Después de la actualización permite validar:

- Versión instalada
- Estado de VPNs
- Estado de OSPF
- Estado de BGP
- Acceso GUI
- Acceso SSH
- Logs del sistema
- Conectividad general

---

## 4. Analizador de Errores

Permite consultar errores frecuentes y mostrar información relevante de troubleshooting.

### Errores Soportados

#### Timeout connecting to FortiGuard

**Causa probable**

```text
Problema de conectividad hacia los servidores FortiGuard.
```

**Comandos sugeridos**

```bash
execute ping service.fortiguard.net
execute traceroute service.fortiguard.net
diagnose debug rating
```

---

#### Firmware validation failed

**Causa probable**

```text
Imagen corrupta o incompatible.
```

**Acciones recomendadas**

```text
Verificar checksum.
Descargar nuevamente el firmware.
Validar modelo del equipo.
```

---

#### No valid upgrade path found

**Causa probable**

```text
La versión requiere upgrades intermedios.
```

**Acciones recomendadas**

```text
Consultar Upgrade Path Tool.
Revisar Release Notes.
```

---

# 🤖 Integración de Inteligencia Artificial

## Estado Actual

Se ha incorporado una sección denominada:

```text
🤖 Asistente IA FortiGate
```

como base para integrar capacidades generativas utilizando Gemini.

---

## Objetivos de la IA

La IA permitirá responder preguntas como:

### Troubleshooting

```text
¿Por qué no puedo conectar con FortiGuard?
```

```text
¿Qué significa Firmware Validation Failed?
```

```text
¿Cómo diagnostico problemas de rating?
```

---

### Upgrade

```text
¿Cómo actualizo un FG-100F desde 6.4.8?
```

```text
¿Qué debo validar antes de una actualización?
```

```text
¿Cuáles son los riesgos de saltar versiones?
```

---

### Operación

```text
¿Cómo verifico el estado HA?
```

```text
¿Qué comandos usar para revisar BGP?
```

```text
¿Cómo validar VPNs después de un upgrade?
```

---

# 🧠 Roadmap de IA

## Fase 1

✅ Incorporación del módulo IA

✅ Interfaz en Streamlit

⬜ Conexión con Gemini

---

## Fase 2

Implementación de consultas técnicas mediante Gemini.

Ejemplos:

```text
Describe este error.
```

```text
Analiza este log.
```

```text
Recomiéndame acciones correctivas.
```

---

## Fase 3

Implementación de RAG (Retrieval-Augmented Generation).

Documentación prevista:

- Release Notes
- Upgrade Paths
- Compatibility Matrix
- KB Articles
- Procedimientos internos
- Manuales de operación

---

## Fase 4

Análisis automático de logs CLI.

Ejemplos:

```text
diagnose sys session stat
```

```text
get system status
```

```text
diagnose debug flow
```

```text
event logs
```

---

# 📂 Base de Conocimiento

## firmware_paths.json

Contiene las rutas de actualización soportadas.

### Ejemplo

```json
{
  "FG-60F": {
    "6.4.8": [
      "7.0.5",
      "7.0.13",
      "7.2.8"
    ]
  }
}
```

---

## known_errors.json

Contiene errores conocidos.

### Ejemplo

```json
{
  "Timeout connecting to FortiGuard": {
    "causa": "Problema de conectividad hacia los servidores FortiGuard.",
    "comandos": [
      "execute ping service.fortiguard.net",
      "execute traceroute service.fortiguard.net"
    ]
  }
}
```

---

# 🏗️ Arquitectura

```text
+---------------------+
|      Usuario        |
+----------+----------+
           |
           v
+---------------------+
| Streamlit FrontEnd  |
+----------+----------+
           |
           v
+---------------------+
|    Lógica Python    |
+----------+----------+
           |
+----------+----------+
|                     |
v                     v

firmware_paths     known_errors
      JSON              JSON

           |
           v

      Gemini AI
    (Próxima Fase)
```

---

# 📁 Estructura del Proyecto

```text
firmware-upgrade-assistant/
│
├── streamlit_app.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── firmware_paths.json
│   └── known_errors.json
│
├── capturas/adas

- Python
- Streamlit
- JSON
- Git
- GitHub

Próximamente:

- Gemini API
- LangChain
- ChromaDB
- RAG

---

# 📥 Instalación

### Clonar repositorio

```bash
git clone <URL_REPOSITORIO>
```

### Entrar al directorio

```bash
cd firmware-upgrade-assistant
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# ▶️ Ejecución

```bash
streamlit run streamlit_app.py
```

Acceder desde navegador:

```text
http://localhost:8501
```

---

# ✅ Estado del Proyecto

| Componente | Estado |
|------------|---------|
| Consulta de Upgrade | ✅ |
| Checklist Pre-Upgrade | ✅ |
| Checklist Post-Upgrade | ✅ |
| Analizador de Errores | ✅ |
| Base de Conocimiento JSON | ✅ |
| Streamlit UI | ✅ |
| Asistente IA | ✅ |
| Gemini | 🚧 |
| RAG | 🚧 |
| Análisis de Logs | 🚧 |

---

# 🔮 Futuras Mejoras

- Integración completa con Gemini
- Implementación de RAG
- Carga de documentación Fortinet
- Interpretación automática de logs
- Compatibilidad con más modelos
- Exportación de reportes
- Recomendaciones de upgrade basadas en IA
- Dashboard operacional

---

# 👤 Autor

**Luis Colón**

Máster en Inteligencia Artificial

Proyecto orientado a la automatización, asistencia técnica y reducción de riesgo operacional en procesos de actualización de firmware FortiGate.