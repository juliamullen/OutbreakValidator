# Outbreak Validator

Validation steps for outbreak.info parsing.

Import and instantiate the schema object:
```
from validator import OutbreakValidator

validator = OutbreakValidator()
```

Test against an instance
```
instance = { ... }
validator.validate(instance, "outbreak:Dataset")
```
