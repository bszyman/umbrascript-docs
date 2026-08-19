# Copy media

Copies one media item under another media item or to the media root. The copy can be given a new name.

!!! note
    Copying file-based media duplicates the underlying media file as well as the stored property values.

## Syntax

```text
copy media <reference> to <destination> [with name "<new-name>"]
```

## Examples

Copy and rename an item:

```text title="UmbraScript"
copy media at "/Images/legacy-logo.png" to at "/Images/Archive/" with name "Legacy logo archive"
```

Copy an item to the root:

```text title="UmbraScript"
copy media "b01b9237-ca8d-499a-aa97-de894cab5e3b" to root
```

## Behavior

UmbraScript creates a new media item of the same media type, copies culture names and property values, and duplicates files recognized by Umbraco's media URL generators. When `with name` is present, the copy and rename are reported separately.

## Result

The result contains `summary`, `attempted`, `succeeded`, `failed`, and a one-item `results` array. The item distinguishes `copySucceeded` from `renameSucceeded` and includes the source, destination, copied key, and final name.

## Permissions

Requires access to the UmbraScript section and a signed-in backoffice user for the copy and optional rename operations.

## Common failures

- The source or destination cannot be resolved unambiguously.
- The requested name is empty.
- A referenced source file cannot be copied.
- A property editor exposes a file reference in an unsupported form.
- The copy succeeds but the optional rename fails.

## See also

- [Organize media](../../how-to/organize-media.md)
- [Move media](move.md)
