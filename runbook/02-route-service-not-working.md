# Error 02 - Route / Service no conecta con el Pod

## Síntomas

- El Pod está en estado `Running`
- `oc get pods` muestra todo OK
- El navegador muestra:

Application is not available

- `oc port-forward` funciona correctamente

---

## Diagnóstico

1. Labels del Pod no coinciden con el selector del Service.
2. Service configurado con `targetPort` incorrecto.
3. Route apuntando a un Service incorrecto.
4. Route sin TLS configurado en entorno sandbox.

---

## Verificaciones

```
oc get svc
```

```
oc describe svc <nombre>
```

```
oc get route
```

```
oc describe route <nombre>
```

```
oc get pods --show-labels
```

Verificar que:

spec.selector del Service coincida con los labels del Pod.

targetPort del Service coincida con el puerto expuesto por el contenedor.

La Route apunte al Service correcto.

Solución aplicada
Corregir selector del Service.

Ajustar targetPort.

Configurar TLS en la Route:

yaml
Copiar código
```
spec:
  tls:
    termination: edge
```
    
Lección aprendida
Pod funcionando ≠ aplicación accesible.
Siempre validar la cadena completa:

Pod → Service → Route