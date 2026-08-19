# Create a media folder

Creates one folder under another media item or at the media root.

## Syntax

```text
create media folder named "<name>" at root
create media folder named "<name>" at "<parent-key>"
create media folder named "<name>" at "<parent-path>"
```

## Examples

Create a folder below Images:

```text title="UmbraScript"
create media folder named "Archive" at "/Images/"
```

Create a root folder:

```text title="UmbraScript"
create media folder named "Imports" at root
```

## Result

The result contains `summary`, `key`, `name`, `success`, and `result`. `key` is `null` when creation fails.

## Permissions

Requires access to the UmbraScript section and a signed-in backoffice user for the create operation.

## Common failures

- The folder name is empty or whitespace.
- The parent key or path cannot be resolved.
- The media path is ambiguous.
- Umbraco rejects the parent or the current user's operation.

## See also

- [Destinations](../../language/destinations.md)
- [Organize media](../../how-to/organize-media.md)
