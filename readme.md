# 🚀 Demoblaze Test Automation Suite (Python)

> Proyecto de pruebas automatizadas desarrollado en Python, aplicando buenas prácticas de ingeniería de software y control de calidad (QA).

---

## 📋 Descripción del Proyecto
Este repositorio contiene la solución automatizada para validar flujos críticos en la plataforma **Demoblaze**, abarcando tanto pruebas funcionales de interfaz de usuario (**E2E UI**) como pruebas de servicios web (**API REST**).

---

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.x
* **Framework de Pruebas:** Pytest
* **Automatización Web:** Selenium WebDriver
* **Consumo de APIs:** Requests
* **Reportes:** Pytest-HTML

---

## 📂 Estructura del Repositorio

```text
demoblaze-automation-python/
│
├── pages/                  # Patrón Page Object Model (POM) para UI
│   ├── __init__.py
│   ├── base_page.py        # Acciones y esperas comunes
│   ├── home_page.py        # Localizadores y acciones del catálogo
│   └── cart_page.py        # Gestión del carrito y formulario de compra
│
├── tests/                  # Casos de prueba automatizados
│   ├── __init__.py
│   ├── test_purchase_e2e.py # Flujo E2E de compra en UI
│   └── test_api_demoblaze.py # Pruebas de servicios REST (Signup/Login)
│
├── reports/                # Reportes HTML generados automáticamente
│   └── report.html
│
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación principal

⚙️ Prerrequisitos
Asegúrate de tener instalado en tu equipo:

Python (Versión 3.9 o superior)

Google Chrome (Actualizado, para las pruebas de UI)

Git

📥 Instalación
Clona el repositorio en tu máquina local:

Bash
git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)
cd tu-repositorio
Instala las dependencias necesarias indicadas en el archivo requirements.txt:

Bash
python -m pip install -r requirements.txt
▶️ Instrucciones de Ejecución
Ejecutar Pruebas E2E (UI con Selenium)
Para ejecutar la prueba funcional de extremo a extremo que valida la selección de productos, carrito y formulario de pago:

Bash
python -m pytest tests/test_purchase_e2e.py -v --html=reports/e2e_report.html --self-contained-html
Ejecutar Pruebas de API (Servicios REST)
Para ejecutar las pruebas de los endpoints de signup y login:

Bash
python -m pytest tests/test_api_demoblaze.py -v --html=reports/api_report.html --self-contained-html
📊 Reportes y Evidencias
Al finalizar cada ejecución, se genera un reporte detallado en formato HTML interactivo dentro de la carpeta reports/. Puedes abrir el archivo correspondiente en cualquier navegador web para visualizar el estado detallado de cada caso de prueba.

✒️ Autor
Jorge Leonardo Castro Salazar

QA Automation Engineer

---

### 💡 Tip rápido:
Puedes crear dos repositorios en GitHub separados (uno para UI y otro para API) y usar este mismo modelo adaptando los títulos y la estructura de carpetas según corresponda a cada uno. ¡Quedará impecable para tu portafolio!