# PACKAGE_MANIFEST accounting example

Use explicit accounting so operators can reconcile the manifest with the ZIP without guessing.

Example:

```text
Payload files listed and hashed: 41
PACKAGE_MANIFEST self-hash: intentionally omitted to avoid circular hashing
Total archive file entries: 42
Reference assets included: 10
```

Rules:
- payload count excludes `PACKAGE_MANIFEST.md` only when its self-hash is intentionally omitted,
- total archive entry count includes every file actually stored in the ZIP,
- folder directory entries, if emitted by the ZIP writer, should not be confused with file-entry count,
- the reported count must be checked against the produced archive before delivery.
