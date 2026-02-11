# Error 06 - ConfigMap / Secret no aplicado

## Síntomas

- ConfigMap creado correctamente.
- Pod no refleja variables o cambios.

---

## Diagnóstico

1. No se incluyó `envFrom`.
2. No se montó como volumen.
3. Pod no fue reiniciado tras cambio.

---

## Verificaciones

```
oc describe deployment <nombre>
```

```
oc describe pod <nombre>
```

Solución aplicada
Agregar en Deployment:

```
envFrom:
  - configMapRef:
      name: my-config
  - secretRef:
      name: my-secret
```

Luego recrear pod:

```
oc rollout restart deployment/<nombre>
```

Lección aprendida
ConfigMaps y Secrets no actualizan contenedores ya corriendo automáticamente.