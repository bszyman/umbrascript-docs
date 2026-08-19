# Content commands

Content commands inspect and manage nodes in the Umbraco content tree.

| Command | Scope | Changes data |
| --- | --- | --- |
| [`show content`](show.md) | Item, children, or descendants | No |
| [`create content`](create.md) | One destination | Yes |
| [`publish content`](publish.md) | Item, children, or descendants | Yes |
| [`unpublish content`](unpublish.md) | Item, children, or descendants | Yes |
| [`rename content`](rename.md) | One item | Yes |
| [`move content`](move.md) | One item | Yes |
| [`copy content`](copy.md) | One item | Yes |
| [`trash content`](trash.md) | One item | Yes |
| [`restore content`](restore.md) | One item | Yes |

Use [property commands](../properties/index.md) to inspect or change content property values.

!!! tip
    Run `show content` with the intended reference or selection before a command that changes data.
