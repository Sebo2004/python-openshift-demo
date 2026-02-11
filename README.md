# OpenShift Troubleshooting & Deployment Lab

---

## Descripción

Este repositorio documenta un laboratorio práctico de OpenShift donde se implementaron aplicaciones, se configuraron servicios, rutas, almacenamiento persistente y se resolvieron múltiples escenarios reales de troubleshooting.

El objetivo es demostrar:

- Conocimiento sólido en Linux
- Administración práctica de Kubernetes / OpenShift
- Capacidad de diagnóstico
- Documentación estructurada tipo Runbook
- Buenas prácticas DevOps

---

# Arquitectura General

Pod → Service → Route  
Pod → PVC → StorageClass  
Pod → ConfigMap / Secret  

Se trabajó con:

- Deployments
- Services
- Routes (TLS edge)
- PersistentVolumeClaims
- ConfigMaps
- Secrets
- Image Registry interno
- Debugging con `oc`

---
