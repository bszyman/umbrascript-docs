# References and selections

References identify one content or media item. Selections use a reference as an anchor and choose the anchor, its direct children, or all its descendants.

## Reference one item

Use a key when you need a stable identity:

```text title="UmbraScript"
show content "b01b9237-ca8d-499a-aa97-de894cab5e3b"
```

Use `at` before a path when you reference one item:

```text title="UmbraScript"
show content at "/destinations/pensacola-florida/"
```

| Form | Selects |
| --- | --- |
| `"<key>"` | The item with the specified GUID key |
| `at "<path>"` | The item at the specified path |

## Select children or descendants

Use `in` for direct children:

```text title="UmbraScript"
show content in "/destinations/"
```

Use `below` for all descendants at every depth:

```text title="UmbraScript"
show content below "/destinations/"
```

The anchor item is not included in an `in` or `below` selection.

| Scope | Path form | Key form | Selects |
| --- | --- | --- | --- |
| Self | `at "/path/"` | `"<key>"` | The referenced item |
| Children | `in "/path/"` | `in "<key>"` | Direct children |
| Descendants | `below "/path/"` | `below "<key>"` | Descendants at every depth |

Notice that `at` belongs to a single-item path reference. Do not write `in at` or `below at`.

## Content paths

A content path is an absolute Umbraco route and must begin with `/`. UmbraScript resolves the route using the website's default culture. It checks draft routes as well as published routes.

Routes can change when content is renamed or moved. Use a key when a command must continue to target the same item after structural changes.

## Media paths

A media path begins with `/` and follows media item names from the media root:

```text title="UmbraScript"
show media at "/Images/Destinations/Chicago hero.jpg"
```

Media path matching is case-insensitive. Each segment must identify exactly one item among its siblings. If siblings have the same name, the path is ambiguous; use the media key instead.

The path `/` represents the media root, not a media item. Use a [root destination](destinations.md) when a create, move, or copy command should target the media root.

## Preview a selection

Before a command that changes several items, run the corresponding `show` command with the same selection:

```text title="UmbraScript"
show content below "/news/2025/"
```

Check every returned item before replacing `show` with `publish`, `unpublish`, `set`, or `clear`.
