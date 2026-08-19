# Property commands

Property commands inspect or change property values on content items.

| Command | Scope | Changes data |
| --- | --- | --- |
| [`show property`](show-property.md) | Item, children, or descendants | No |
| [`show properties`](show-properties.md) | Item, children, or descendants | No |
| [`set property`](set.md) | Item, children, or descendants | Yes |
| [`clear property`](clear.md) | Item, children, or descendants | Yes |

Property commands use the property's alias, not its display name. UmbraScript 1.0 property commands operate on content only.

!!! warning
    Set and clear commands save content but do not publish it. They do not select a culture or segment, so test changes carefully on variant content.
