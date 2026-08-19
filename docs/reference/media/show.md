# Show media

Returns summary information for one media item or a selection from the media tree. This command does not modify media.

## Syntax

```text
show media <selection>
```

## Examples

Show one item by key:

```text title="UmbraScript"
show media "b01b9237-ca8d-499a-aa97-de894cab5e3b"
```

Show one item by media path:

```text title="UmbraScript"
show media at "/Images/Destinations/Chicago hero.jpg"
```

Show direct children of a folder:

```text title="UmbraScript"
show media in "/Images/Destinations/"
```

## Result

The `content` array contains `key`, `id`, `name`, `contentTypeAlias`, `created`, `lastModified`, `width`, `height`, and `fileType`. Dimension and file-type fields can be `null` when the media type does not supply them.

## Common failures

- A bare quoted value is not a valid GUID.
- A media path segment does not exist.
- A media path is ambiguous because siblings share a name.
- The path `/` is used as an item reference.

## See also

- [Media paths](../../language/references-and-selections.md#media-paths)
- [Organize media](../../how-to/organize-media.md)
