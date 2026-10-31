# 🛡️ FortiGate AI Operations Assistant

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red.svg)
![Fortinet](https://img.shields.io/badge/Fortinet-FortiGate-orange.svg)
![AI](https://img.shields.io/badge/AI-Gemini-blueviolet.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

---

# 📖 Descripción

FortiGate AI Operations Assistant es una aplicación diseñada para asistir a administradores e ingenieros de redes en tareas relacionadas con la operación, actualización y troubleshooting de dispositivos FortiGate.

La plataforma centraliza información crítica sobre rutas de actualización de FortiOS, errores frecuentes, procedimientos operacionales y consultas mediante Inteligencia Artificial, proporcionando una experiencia unificada para actividades de soporte y mantenimiento.

El objetivo principal es reducir riesgos operacionales, mejorar los tiempos de respuesta y facilitar la toma de decisiones durante procesos de upgrade y resolución de incidentes.

---

# 🎯 Problema que Resuelve

Administrar correctamente dispositivos FortiGate requiere consultar diversas fuentes de información:

- Upgrade Paths
- Release Notes
- Errores conocidos
- Guías de troubleshooting
- Procedimientos operacionales
- Buenas prácticas

Cuando esta información se encuentra dispersa, pueden ocurrir:

- Actualizaciones fallidas
- Indisponibilidad de servicios
- Configuraciones incorrectas
- Incremento del tiempo de troubleshooting
- Mayor dependencia de soporte externo

La aplicación busca centralizar estas tareas en una única interfaz.

---

# 👨‍💻 Usuarios Objetivo

- Administradores de Redes
- Ingenieros de Seguridad
- Ingenieros de Infraestructura
- Personal NOC
- Personal SOC
- MSP (Managed Service Providers)
- Partners Fortinet
- Equipos de Operaciones

---

# 🚀 Funcionalidades Implementadas

## ✅ Upgrade Path Advisor

Permite consultar rutas de actualización soportadas para modelos FortiGate utilizando una base de conocimiento local en formato JSON.

### Ejemplo

**Modelo**

```text
FG-60F
```

**Versión Actual**

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

## ✅ Checklist Pre-Upgrade

Lista de verificaciones recomendadas antes de ejecutar la actualización.

### Incluye

- Backup de configuración
- Revisión de Release Notes
- Verificación de acceso por consola
- Confirmación de espacio disponible
- Confirmación de ventana de mantenimiento
- Validación de HA (High Availability)

---

## ✅ Checklist Post-Upgrade

Validaciones recomendadas luego de una actualización.

### Incluye

- Confirmar versión instalada
- Validar VPNs
- Validar OSPF
- Validar BGP
- Revisar logs
- Validar interfaz GUI
- Validar acceso SSH
- Verificar conectividad general

---

## ✅ Error Analyzer

Módulo diseñado para consultar errores frecuentes y recibir recomendaciones de diagnóstico.

### Capacidades

- Consulta de errores conocidos
- Identificación de causa probable
- Lista de comandos sugeridos
- Base de datos extensible mediante JSON

### Ejemplo

**Error**

```text
Timeout connecting to FortiGuard
```

**Diagnóstico**

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

## ✅ Asistente IA FortiGate

Se encuentra integrado con Gemini para responder preguntas técnicas relacionadas con el ecosistema Fortinet.

### Áreas soportadas

- FortiGate
- FortiOS
- FortiGuard
- Routing
- VPN
- Firmware Upgrade
- Troubleshooting

### Ejemplos

```text
¿Qué es FortiGuard?
```

```text
¿Cómo validar una VPN después de actualizar FortiOS?
```

```text
¿Qué debo revisar antes de migrar a la versión 7.2?
```

```text
¿Cómo diagnostico problemas con FortiGuard?
```

---

# 🤖 Estado de la Integración Gemini

## Estado Actual

✅ Integración completada

✅ Configuración mediante Streamlit Secrets

✅ Conectividad con Gemini

✅ Procesamiento de consultas

✅ Despliegue funcional en Streamlit Cloud

✅ Manejo de excepciones

---

## Limitaciones Actuales

La disponibilidad del asistente depende de la API de Gemini.

Pueden ocurrir errores temporales tales como:

```text
429 - Quota Exceeded
```

Cuando se excede la cuota disponible.

o

```text
504 - Deadline Exceeded
```

Cuando el servicio excede el tiempo máximo de respuesta.

Estos eventos no representan fallos de la aplicación sino limitaciones o condiciones temporales del proveedor de IA.

---

# 📂 Base de Conocimiento

## firmware_paths.json

Contiene rutas de actualización soportadas.

### 

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

Contiene errores conocidos y recomendaciones.

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
+------------------------+
|        Usuario         |
+------------+-----------+
             |
             v

+------------------------+
|     Streamlit UI       |
+------------+-----------+
             |
             v

+------------------------+
|     Python Backend     |
+------------+-----------+
             |
   +---------+---------+
   |                   |
   v                   v

firmware_paths     known_errors
      JSON              JSON

             |
             v

         Gemini API
             |
             v

   FortiGate AI Assistant
```

---

# 📁 Estructura del Proyecto

```text
firmware-upgrade-assistant/
├── README.md
├── requirements.txt
├── streamlit_app.py
├── app.py
├── Procfile
├── .gitignore
│
├── data/
│   ├── firmware_paths.json
│   └── known_errors.json
│
├── docs/
│   ├── compatibility-matrix/
│   ├── fortigate-release-notes/
│   └── upgrade-paths/
│
├── capturas/
│   ├── version0-home.png
│   ├── version0-upgrade-route.png
│   └── version1-error-analysis.png
│
├── static/
├── notebooks/
└── templates/
    └── index.html
```

---

# 🛠️ Tecnologías Utilizadas

## Implementadas

- Python
- Streamlit
- JSON
- Git
- GitHub
- Gemini API
- Streamlit Cloud

## En Evaluación

- LangChain
- ChromaDB
- Vector Databases
- Retrieval-Augmented Generation (RAG)

---

# 🔑 Configuración de Gemini

Crear:

```text
.streamlit/secrets.toml
```

Contenido:

```toml
GEMINI_API_KEY = "TU_API_KEY"
```

---

# 📥 Instalación

### Clonar el repositorio

```bash
git clone <URL_REPOSITORIO>
```

### Acceder al proyecto

```bash
cd firmware-upgrade-assistant
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# ▶️ Ejecución Local

```bash
streamlit run streamlit_app.py
```

Acceder desde:

```text
http://localhost:8501
```

---

# ☁️ Despliegue

Actualmente desplegado mediante:

- GitHub
- Streamlit Community Cloud

La aplicación utiliza:

- GitHub para control de versiones
- Streamlit Secrets para protección de credenciales
- Gemini API para consultas de Inteligencia Artificial

---

# ✅ Estado Actual del Proyecto

| Componente | Estado |
|------------|---------|
| Upgrade Path Advisor | ✅ |
| Checklist Pre-Upgrade | ✅ |
| Checklist Post-Upgrade | ✅ |
| Error Analyzer | ✅ |
| Base de Conocimiento JSON | ✅ |
| Streamlit UI | ✅ |
| Asistente IA | ✅ |
| Integración Gemini | ✅ |
| Streamlit Cloud Deployment | ✅ |
| Secrets Management | ✅ |
| RAG | 🚧 |
| Config Analyzer | 🚧 |
| PDF/DOCX Export | 🚧 |
| Runbook Generator | 🚧 |

---

# 🔮 Roadmap

## Próximas Mejoras

### RAG para documentación Fortinet

- Release Notes
- Upgrade Guides
- Compatibility Matrix
- Knowledge Base Articles
- Best Practices

### Config Analyzer

Análisis automático de configuraciones FortiGate.

### Runbook Generator

Generación automática de procedimientos de actualización.

### Exportación de Reportes

- PDF
- DOCX

### Historial de Consultas IA

Almacenamiento y búsqueda de consultas realizadas.

---

# 🤖 Proceso con IA

## Modelo utilizado

La aplicación integra Google Gemini como motor de Inteligencia Artificial para asistir a operadores, administradores e ingenieros durante tareas de actualización, resolución de incidencias y consulta técnica relacionada con dispositivos FortiGate.

## Conocimiento utilizado

La aplicación combina información estructurada almacenada localmente con capacidades de Inteligencia Artificial proporcionadas por Google Gemini.

Las fuentes de conocimiento utilizadas actualmente son:

- `firmware_paths.json`
- `known_errors.json`

Estas bases de conocimiento permiten consultar rutas de actualización soportadas y errores conocidos sin depender de servicios externos.

## Prompt utilizado

Las consultas enviadas a Gemini utilizan un prompt especializado que restringe las respuestas a temas relacionados con:

- FortiGate
- FortiOS
- FortiGuard
- VPN
- Routing
- Troubleshooting
- Firmware Upgrade

El objetivo es mantener las respuestas enfocadas en tecnologías Fortinet y reducir resultados fuera de contexto.

## Tareas delegadas a la IA

- Interpretación de consultas en lenguaje natural.
- Explicación de conceptos técnicos.
- Generación de recomendaciones de troubleshooting.
- Asistencia en consultas operacionales relacionadas con Fortinet.

## Tareas supervisadas por el usuario

- Validación técnica de las respuestas.
- Evaluación de riesgos operacionales.
- Ejecución de cambios sobre dispositivos.
- Aprobación final de acciones correctivas.

La aplicación no realiza cambios automáticos sobre equipos FortiGate y todas las recomendaciones requieren validación humana antes de su aplicación.

---

# 📥 Entradas y 📤 Salidas

## Entradas

La aplicación recibe uno o varios de los siguientes elementos:

- Modelo FortiGate.
- Versión actual de FortiOS.
- Consulta técnica en lenguaje natural.
- Error observado.
- Síntomas reportados por el usuario.

## Salidas

La aplicación genera:

- Ruta de actualización recomendada.
- Checklists operacionales.
- Información sobre errores conocidos.
- Comandos sugeridos.
- Recomendaciones técnicas.
- Respuestas generadas mediante IA.

---

# ✅ Criterios de Aceptación

La aplicación cumple con los requisitos cuando:

- Proporciona rutas de actualización disponibles para modelos registrados.
- Muestra errores conocidos y recomendaciones asociadas.
- Permite consultas técnicas mediante Gemini.
- Gestiona correctamente errores de comunicación con la API.
- Mantiene disponibles las funciones locales aunque la IA no esté disponible.

## Casos límite

### Modelo no registrado

**Entrada**

```text
FG-XYZ
```

**Resultado esperado**

```text
No se encontraron rutas de actualización para el modelo solicitado.
```

### Error desconocido

**Entrada**

```text
Unknown Error
```

**Resultado esperado**

```text
No existe información suficiente para emitir una recomendación confiable.
```

### API no disponible

**Entrada**

Consulta técnica mediante Gemini.

**Resultado esperado**

```text
Servicio temporalmente no disponible.
```

---

# 🧪 Pruebas y Mejoras

## Metodología de prueba

La aplicación fue evaluada mediante escenarios reales relacionados con administración, actualización y troubleshooting de dispositivos FortiGate.

## Casos evaluados

- Consulta de rutas de actualización.
- Validación de checklist pre-upgrade.
- Validación de checklist post-upgrade.
- Consulta de errores conocidos.
- Generación de recomendaciones mediante IA.
- Manejo de errores de Gemini.

## Resultados

Las pruebas demostraron que la aplicación centraliza información operativa relevante y simplifica la consulta de rutas de actualización, errores conocidos y asistencia técnica mediante IA.

## Mejoras implementadas

Durante las pruebas se identificaron oportunidades de mejora relacionadas con la precisión y relevancia de las respuestas.

Como resultado se realizaron los siguientes ajustes:

- Refinamiento de prompts.
- Mejora de manejo de excepciones.
- Optimización de la estructura de respuestas.
- Ampliación de la base de conocimiento.
- Mejora de la experiencia de usuario.

---

# ⚠️ Limitaciones

- La calidad de las respuestas depende de la información disponible.
- Las respuestas generadas por IA requieren validación humana.
- La aplicación no ejecuta cambios automáticos en dispositivos FortiGate.
- La disponibilidad de la IA depende de la disponibilidad del servicio Gemini.
- La cobertura actual está enfocada principalmente en tecnologías Fortinet.

---

# 🎤 Pitch Ejecutivo

Los ingenieros de redes invierten tiempo consultando múltiples fuentes de información para planificar actualizaciones y resolver incidencias en dispositivos FortiGate.

FortiGate AI Operations Assistant centraliza rutas de actualización, errores conocidos, procedimientos operacionales y asistencia técnica en una única plataforma.

La integración con Inteligencia Artificial permite responder consultas técnicas especializadas, generar recomendaciones de troubleshooting y asistir en tareas operacionales relacionadas con FortiGate mediante procesamiento de lenguaje natural.

Las pruebas realizadas permitieron optimizar los prompts y mejorar la precisión de las recomendaciones generadas.

Como siguiente paso se implementará una arquitectura RAG basada en documentación oficial de Fortinet para ampliar la cobertura y precisión de las respuestas.

---

## Próximas Mejoras

### RAG para documentación Fortinet

Fuentes previstas:

- Release Notes
- Upgrade Guides
- Compatibility Matrix
- Knowledge Base Articles
- Best Practices

### Config Analyzer

Análisis automático de:

```text
.conf
.txt
```

### Runbook Generator

Generación automática de procedimientos de actualización.

### Exportación de Reportes

Formatos previstos:

```text
PDF
DOCX
```

### Historial de Consultas IA

Almacenamiento y búsqueda de consultas realizadas.

---

# 👤 Autor

**Luis Colón**

Máster en Machine Learning e Inteligencia Artificial

Proyecto enfocado en automatización operativa, asistencia técnica mediante IA y reducción de riesgos durante procesos de administración y actualización de dispositivos FortiGate.