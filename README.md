OpenShift Debug Lab – Plataforma de Diagnóstico y Operación

Proyecto práctico enfocado en despliegue, operación y diagnóstico de aplicaciones en OpenShift.

El objetivo principal no es la aplicación, sino la gestión del ciclo de vida, observabilidad y resolución de fallos de plataforma, utilizando herramientas nativas de OpenShift desde la perspectiva de un DevOps / Platform Engineer / SRE.

Objetivos del Proyecto

Este laboratorio permite demostrar habilidades en:

Despliegue y operación de aplicaciones en OpenShift

Diagnóstico de fallos reales de plataforma

Uso de oc como herramienta principal de operación

Comprensión de la relación entre Pods, Deployments, Services, Routes, Configuración, Recursos, Seguridad y Networking

Documentación de runbooks operativos para cada escenario

Plataforma y Entorno

OpenShift Sandbox (efímero: 24 horas)

CI/CD: Manual

Registro de imágenes: Internal Registry

Runtime base: UBI Minimal 9 (Python 3.11)

Aplicación: Python + Flask

El entorno sandbox se utiliza para simular escenarios reales de operación y troubleshooting con restricciones intencionales.

Aplicación Base

La aplicación es simple, enfocada en pruebas de plataforma:

Python + Flask

Endpoint / → Validación básica

Endpoint /api → Health probes

Lectura de variables de entorno, ConfigMaps y Secrets

Escritura en volumen persistente (PVC)

Consumo controlado de CPU y memoria

El enfoque está en romper la aplicación desde OpenShift, no desde el código.

Componentes de OpenShift Utilizados

Core:

Deployment

Service

Route

ConfigMap

Secret

PersistentVolumeClaim (PVC)

Requests / Limits

Liveness / Readiness Probes

Operación y Debug:

Logs (oc logs)

Eventos (oc get events)

Gestión de imágenes (build, push, tag)

Troubleshooting de estados (ImagePullBackOff, CrashLoopBackOff, OOMKilled)

Validación de networking interno

Seguridad (SCC, permisos)

Documentación de Runbooks

Cada escenario se documenta en la carpeta runbook/ siguiendo este formato:

Estado inicial (fallo reproducido)

Síntomas observados

Diagnóstico con oc

Corrección aplicada

Validación final

Aprendizajes

Ejemplos de escenarios:

ImagePullBackOff (imagen incorrecta)

CrashLoopBackOff

Selector Service ↔ Pod incorrecto

Fallos de enrutamiento (Route / TLS)

Problemas de recursos (CPU / Memoria)

Configuración incorrecta (ConfigMap / Env)

Secret mal montado