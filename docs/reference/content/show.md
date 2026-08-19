# Show content

Returns summary information for one content item or a selection from the content tree. This command does not modify content.

## Syntax

```text
show content <selection>
```

`<selection>` supports a key, `at` path, `in` selection, or `below` selection.

## Examples

Show one item by key:

```text title="UmbraScript"
show content "b01b9237-ca8d-499a-aa97-de894cab5e3b"
```

Show one item by route:

```text title="UmbraScript"
show content at "/destinations/pensacola-florida/"
```

Show every descendant of a branch:

```text title="UmbraScript"
show content below "/destinations/"
```

## Result

The `content` array contains `key`, `id`, `name`, `contentTypeAlias`, `created`, and `lastModified` for every selected item.

## Common failures

- A bare quoted value is not a valid GUID.
- A content route cannot be found in the default culture.
- Umbraco cannot load a child or descendant returned by the navigation service.

## See also

- [References and selections](../../language/references-and-selections.md)
- [Show all properties](../properties/show-properties.md)
