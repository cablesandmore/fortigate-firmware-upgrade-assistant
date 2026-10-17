# FortiGate Firmware Upgrade Assistant

## Descripción

FortiGate Firmware Upgrade Assistant es una aplicación web desarrollada en Flask para ayudar a administradores e ingenieros de redes a planificar, validar y ejecutar actualizaciones de firmware en dispositivos FortiGate de forma segura.

El objetivo es reducir errores durante los procesos de actualización mediante la validación de rutas de upgrade, el análisis de problemas comunes y la generación de listas de verificación antes y después de cada actualización.

---

## Problema

Las actualizaciones de firmware en dispositivos FortiGate suelen fallar o retrasarse debido a:

- Rutas de actualización incorrectas.
- Incompatibilidades entre versiones.
- Dependencias desconocidas.
- Problemas de conectividad con FortiGuard.
- Falta de validaciones previas.

Esto provoca tiempo de inactividad, riesgos operacionales y retrasos en las ventanas de mantenimiento.

---

## Usuarios Objetivo

- Administradores de red.
- Ingenieros de redes.
- Técnicos de infraestructura.
- Proveedores de servicios gestionados (MSP).
- Equipos de soporte que administran dispositivos FortiGate.

---

## Funcionalidades Actuales (Versión 0)

### Consulta de Ruta de Upgrade

Permite seleccionar:

- Modelo FortiGate
- Versión actual

Y devuelve:

- Ruta de actualización recomendada.

### Checklist Pre-Upgrade

Genera recomendaciones antes de actualizar:

- Backup de configuración.
- Verificación de acceso por consola.
- Validación de espacio disponible.
- Revisión de Release Notes.
- Verificación de alta disponibilidad (HA).
- Confirmación de ventana de mantenimiento.

### Checklist Post-Upgrade

Permite verificar:

- Versión instalada.
- Funcionamiento de VPNs.
- Conectividad general.
- Estado de protocolos de routing.
- Acceso GUI y SSH.
- Revisión de logs.

---

## Funcionalidades Futuras

### Análisis de Errores

Interpretación automática de errores comunes como:

- Timeout connecting to FortiGuard
- No valid upgrade path found
- Firmware validation failed

### Integración con IA

Implementación de un sistema RAG (Retrieval-Augmented Generation) basado en:

- Release Notes de Fortinet
- Upgrade Path Tool
- Compatibility Matrix
- Documentación oficial de FortiOS

La IA podrá:

- Responder preguntas técnicas.
- Recomendar rutas de actualización.
- Analizar errores.
- Generar procedimientos personalizados.

---

## Tecnologías Utilizadas

- Python
- Flask
- HTML5
- Bootstrap
- JSON

---

## Estructura del Proyecto

```text
firmware-upgrade-assistant
├── README.md
├── app.py
├── requirements.txt
├── backups
├── capturas
├── data
│   ├── firmware_paths.json
│   └── known_errors.json
├── docs
│   ├── compatibility-matrix
│   ├── fortigate-release-notes
│   └── upgrade-paths
├── notebooks
├── static
└── templates
    └── index.html
```

## Instalación

Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
```

Entrar al proyecto:

```bash
cd firmware-upgrade-assistant
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución

Iniciar la aplicación:

```bash
python app.py
```

Abrir en el navegador:

```text
http://127.0.0.1:5000
```

---

## Ejemplo de Uso

Modelo:

```text
FG-100F
```

Versión:

```text
6.4.8
```

Resultado:

```text
7.0.5
7.0.13
7.2.8
```

---

## Estado del Proyecto

✅ Versión 0 completada

✅ Aplicación Flask funcional

✅ Consulta de rutas de upgrade

✅ Checklists pre y post actualización

⬜ Análisis automático de errores

⬜ Integración con IA mediante RAG

⬜ Consulta de documentación oficial de Fortinet